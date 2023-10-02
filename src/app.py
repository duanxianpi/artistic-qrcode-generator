import os
import argparse

import zipfile
import glob
import boto3

import sys
import time
import psutil
from pathlib import Path
from sd import sd_qrcode


def prepare_codido_input(args,input_folder_path,isZip=False):

    if args.codido == 'True':
        
        s3 = boto3.client('s3')

        # downloads codido input file into the folder specified by input_folder_path
        input_file_path = os.path.join(input_folder_path, args.input.split('_SPLIT_')[-1])
        s3.download_file(os.environ['S3_BUCKET'], args.input, input_file_path)

    if isZip:
        with zipfile.ZipFile(input_file_path, 'r') as zip_ref:
            zip_ref.extractall(input_folder_path)
        os.remove(input_file_path) # remove the zip file

    return True

def prepare_codido_output(args,output_folder_path):
    if args.codido == 'True':
    # create zip with all the saved outputs
        s3 = boto3.client('s3')

        zip_name = output_folder_path + '.zip'
        with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zip_ref:
            for folder_name, subfolders, filenames in os.walk(output_folder_path):
                for filename in filenames:
                    file_path = os.path.join(folder_name, filename)
                    zip_ref.write(file_path, arcname=os.path.relpath(file_path, output_folder_path))

        # upload
        s3.upload_file(zip_name, os.environ['S3_BUCKET'], args.output)

    raise SystemExit

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="input file will be downloaded from AWS")
    parser.add_argument("--output", help="output will be upload from AWS to ")
    parser.add_argument("--codido", help="running on codido", default= 'False')
    parser.add_argument("--text", help="The text you want to encode in QR Code.")
    parser.add_argument("--prompt", help="What do you want your QR Code to look like?")
    parser.add_argument("--negative_prompt", help="What you don't want to appear on the qr code")
    parser.add_argument("--qr_code_style",help="What should the basic qr_code look like?")
    parser.add_argument("--control_net",help="Which QR Code ControlNet to use")
    parser.add_argument("--art_style",help="Two art styles to choose from.")
    parser.add_argument("--noise",help="Whether to generate noise in the margins, which would be more favorable for qrcode to hide into the drawing. \"true\" or \"false\"")
    parser.add_argument("--CN_Scale",help="The weight of the ControlNet. The higher the weight, the more the output will be affected")
    parser.add_argument("--CN_Start", help="The percentage of the generation process when the ControlNet starts to take effect.")
    parser.add_argument("--CN_End",help="The percentage of the generation process when the ControlNet stops taking effect.")

    args = parser.parse_args()

    input_folder_path = os.path.join(os.sep, 'app/src', 'inputs')
    output_folder_path = os.path.join(os.sep, 'app/src', 'outputs')

    os.makedirs(input_folder_path, exist_ok=True)
    os.makedirs(output_folder_path, exist_ok=True)

    pid = os.getpid()
    p = psutil.Process(pid)
    info_start = p.memory_full_info().uss/1024/1024
    start_time = time.time()

    # main(prompt)
    sd_qrcode(args)

    over_time = time.time()
    info_end = p.memory_full_info().uss/1024/1024
    total_time = over_time - start_time

    print("Took "+str(info_end-info_start)+" MB, " + str(total_time) + "s")

    prepare_codido_output(args,output_folder_path)