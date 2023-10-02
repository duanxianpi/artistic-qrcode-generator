from diffusers import ControlNetModel, StableDiffusionControlNetPipeline, DPMSolverMultistepScheduler
from diffusers.utils import load_image
from compel import Compel, DiffusersTextualInversionManager
import torch
import os,subprocess
import cv2
import numpy as np

def sd_qrcode(options):
    # Choose ControlNet
    contorlnet_url = "/app/models/monster" if "CREATIVE" in options.control_net.strip().upper() else "Nacholmo/controlnet-qr-pattern-v2"
    # controlnet = ControlNetModel.from_pretrained("Nacholmo/controlnet-qr-pattern-v2")
    # controlnet = ControlNetModel.from_pretrained("monster-labs/control_v1p_sd15_qrcode_monster")
    controlnet = ControlNetModel.from_pretrained(contorlnet_url)

    # Choose the style of base mode
    if "ANIME" in options.art_style.strip().upper():
        # Anime Style
        pipeline = StableDiffusionControlNetPipeline.from_single_file(
            "https://huggingface.co/Meina/MeinaMix/blob/main/Meina V10 - baked VAE.safetensors",
            controlnet=controlnet,
            use_safetensors=True
        )
    
    else:
        # Realistic
        pipeline = StableDiffusionControlNetPipeline.from_single_file(
            "https://huggingface.co/Lykon/DreamShaper/blob/main/DreamShaper_8_pruned.safetensors",
            controlnet=controlnet,
            use_safetensors=True
        )

    pipeline.to('cuda')

    pipeline.load_textual_inversion("/app/models/easynegative.safetensors")
    pipeline.load_textual_inversion("/app/models/ng_deepnegative_v1_75t.pt")
    pipeline.load_lora_weights("OedoSoldier/detail-tweaker-lora")

    pipeline.scheduler = DPMSolverMultistepScheduler.from_config(pipeline.scheduler.config, use_karras_sigmas=True)

    print("Finished Loading SD")
    print("Start Generatring QR Code...")
    # Define the script path
    script_path = "/app/node-qrcode-toolkit/build/index.js"

    # Define your arguments
    mode = "minimalist" if "MINIMALIST" in options.qr_code_style.strip().upper() else ("square" if "SQUARE" in options.qr_code_style.strip().upper() else "round") 
    noise = "-noise" if "TRUE" in options.noise.strip().upper() else ""
    config = f"/app/src/configs/{mode}{noise}.json"
    text = options.text

    # Call the Node.js script with arguments
    result = subprocess.run(["node", script_path, "-c" ,f"{config}", "-i" ,f"{text}", "-o", "/app/src/outputs"], capture_output=False, text=False)

    print("Finished Generatring QR Code...")
    print(result)

    qr_code_image = load_image(
        "/app/src/outputs/qrcode.png"
    )

    style_pprompt = ""
    if "ANIME" in options.art_style.strip().upper():
        style_pprompt = "(Anime Style)+," 
    elif "REALISTIC" in options.art_style.strip().upper():
        style_pprompt = "(Realistic Style)+,"

    fix_prompt = """(Masterpiece, best quality, Exquisite Beauty)++,"""
    prompt = options.prompt

    nprompt = options.negative_prompt
    fix_nprompt = """nsfw,nude,<easynegative>+, <ng_deepnegative_v1_75t>+,(worst quality, low quality)++, 
                zombie,overexposure, watermark,text,bad anatomy,
                bad hand,extra hands,extra fingers,too many fingers,fused fingers,bad arm,distorted arm,
                extra arms,fused arms,extra legs,missing leg,disembodied leg,extra nipples, detached arm,
                liquid hand,inverted hand,disembodied limb, oversized head,extra body,
                completely nude, extra navel,(hair between eyes)+,sketch, duplicate, ugly,
                huge eyes, text, logo, worst face, (bad and mutated hands)++, (blurry)++, horror, geometry,
                bad_prompt, (bad hands)+, (missing fingers)+, multiple limbs, bad anatomy, (interlocked fingers:)++,
                Ugly Fingers, (extra digit and hands and fingers and legs and arms)+,
                (deformed fingers)+, (long fingers)+, bad-artist, bad hand, extra legs,"""
    
    textual_inversion_manager = DiffusersTextualInversionManager(pipeline)

    compel = Compel(
        tokenizer=pipeline.tokenizer, text_encoder=pipeline.text_encoder,
        textual_inversion_manager=textual_inversion_manager)

    conditioning = compel.build_conditioning_tensor(style_pprompt+fix_prompt+prompt)
    nconditioning = compel.build_conditioning_tensor(fix_nprompt+nprompt)

    # generator = torch.Generator(device="cuda")
    # generator.manual_seed(0)

    CN_Scale = float(options.CN_Scale.strip())
    CN_Start = float(options.CN_Start.strip())
    CN_End = float(options.CN_End.strip())

    for i in range(1,2):
        image = pipeline(prompt_embeds=conditioning, negative_prompt_embeds =nconditioning,
                        image=qr_code_image,
                        num_inference_steps=30,
                        #  guidance_scale=0.5,
                        controlnet_conditioning_scale=CN_Scale,
                        control_guidance_start=CN_Start,control_guidance_end=CN_End,
                        cross_attention_kwargs={"scale": 0.8},
                        width=1024,height=1024).images[0]

        torch.cuda.empty_cache()

        cv_img = cv2.cvtColor(np.asarray(image),cv2.COLOR_RGB2BGR)
        os.makedirs(os.path.dirname(f"/app/src/outputs/{str(i)}/result"), exist_ok=True)

        cv2.imwrite(f"outputs/{str(i)}/result 1024x1024.png",cv_img)
        cv2.imwrite(f"outputs/{str(i)}/result 512x512.png",cv2.resize(cv_img, (512, 512)))
        cv2.imwrite(f"outputs/{str(i)}/result 256x256.png",cv2.resize(cv_img, (256, 256)))

    return 0
