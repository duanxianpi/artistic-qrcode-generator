# Artistic Qr Code Docker
Generate your own artisitic Qr Code in 5 mins! Artistic Qr Code Docker allows you to generate artisitic Qr Code. It use [Diffuser](https://github.com/huggingface/diffusers) to invoke the stable diffusion model and ControlNet instead of the widely used [stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui). This allows us to do the generation from the command line instead of the GUI.

## Try out
[Try it in CODIDO](https://www.codido.co/marketplace/browse) or [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://https://colab.research.google.com/drive/1EHrv2QLe-RICMl1z72h5YBSEIKg7Fdje?usp=sharing)

## How to use?
### Build
```bash
git clone https://github.com/duanxianpi/artistic_qrcode_docker
cd artistic_qrcode_docker
docker image build -t artistic_qrcode .
```
### Usage
```
docker container run --gpus all artistic_qrcode_docker -h

usage: app.py [-h] [--input INPUT] [--output OUTPUT] [--codido CODIDO] [--text TEXT] [--prompt PROMPT] [--negative_prompt NEGATIVE_PROMPT]
              [--qr_code_style QR_CODE_STYLE] [--control_net CONTROL_NET] [--art_style ART_STYLE] [--noise NOISE] [--CN_Scale CN_SCALE]
              [--CN_Start CN_START] [--CN_End CN_END]

options:
  -h, --help            show this help message and exit
  --input INPUT         input file will be downloaded from AWS
  --output OUTPUT       output will be upload from AWS to
  --codido CODIDO       running on codido
  --text TEXT           The text you want to encode in QR Code.
  --prompt PROMPT       What do you want your QR Code to look like?
  --negative_prompt NEGATIVE_PROMPT
                        What you don't want to appear on the qr code
  --qr_code_style QR_CODE_STYLE
                        What should the basic qr_code look like?
  --control_net CONTROL_NET
                        Which QR Code ControlNet to use
  --art_style ART_STYLE
                        Two art styles to choose from.
  --noise NOISE         Whether to generate noise in the margins, which would be more favorable for qrcode to hide into the drawing. "true" or
                        "false"
  --CN_Scale CN_SCALE   The weight of the ControlNet. The higher the weight, the more the output will be affected
  --CN_Start CN_START   The percentage of the generation process when the ControlNet starts to take effect.
  --CN_End CN_END       The percentage of the generation process when the ControlNet stops taking effect.
```
