![logo](https://github.com/duanxianpi/artistic-qrcode-generator/assets/97914968/f6c7c05e-e40b-49f1-8363-a9f904b336f0)
# Artistic Qr Code Generator
Artistic Qr Code Generator uses [Diffuser](https://github.com/huggingface/diffusers) to invoke the stable diffusion model and ControlNet. It allows you to do the generation from the command line instead of the GUI.

## Try out
[Try it in CODIDO](https://www.codido.co/marketplace/browse) or [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://https://colab.research.google.com/drive/1EHrv2QLe-RICMl1z72h5YBSEIKg7Fdje?usp=sharing)

## How does it work?
If you are interesting how the Stable Diffusion and Control Net work together, here is some greate articles to start
- [Stable Diffusion QR Code 101](https://antfu.me/posts/ai-qrcode-101)
- [Refining AI Generated QR Code](https://antfu.me/posts/ai-qrcode-refine)

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
## Gallery
<table>
  <tr>
    <td>First Screen Page</td>
     <td>Holiday Mention</td>
     <td>Present day in purple and selected day in pink</td>
  </tr>
  <tr>
    <td><img src="https://github.com/duanxianpi/artistic-qrcode-generator/assets/97914968/87c0de45-83ce-4a6d-b13c-0f89f2eb5aac" width=270 height=480></td>
    <td><img src="https://github.com/duanxianpi/artistic-qrcode-generator/assets/97914968/4bc67f92-4d6e-452e-9c43-4b175375f744" width=270 height=480></td>
    <td><img src="https://github.com/duanxianpi/artistic-qrcode-generator/assets/97914968/44bf0098-06f1-41f3-a6a2-b9a5b8fbff8a" width=270 height=480></td>
  </tr>
</table>

