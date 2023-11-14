![logo](https://github.com/duanxianpi/artistic-qrcode-generator/assets/97914968/0a12f493-78c4-4aa6-b5b7-bd6c4ee7d57d)
# Artistic Qr Code Generator
Artistic Qr Code Generator uses [Diffuser](https://github.com/huggingface/diffusers) to invoke the stable diffusion model and ControlNet. It allows you to do the generation from the command line instead of the GUI.

## Try out
[Try it in CODIDO](https://www.codido.co/marketplace/browse) or [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1EHrv2QLe-RICMl1z72h5YBSEIKg7Fdje?usp=sharing)

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
    <td width="32%"><img src="https://github.com/duanxianpi/artistic-qrcode-generator/assets/97914968/df526118-023c-4372-99f1-dbea1815547b"></td>
    <td width="32%"><img src="https://github.com/duanxianpi/artistic-qrcode-generator/assets/97914968/19fbecca-9547-4d3b-8e49-4837f2cbe818"></td>
    <td width="32%"><img src="https://github.com/duanxianpi/artistic-qrcode-generator/assets/97914968/a100a34f-e34c-44dd-a57b-3e3ed927850e"></td>
  </tr>
  <tr>
    <td width="32%"><img src="https://github.com/duanxianpi/artistic-qrcode-generator/assets/97914968/f7404540-9cd7-47d4-a444-8eae6dd5d696"></td>
    <td width="32%"><img src="https://github.com/duanxianpi/artistic-qrcode-generator/assets/97914968/baa4a1aa-2d8c-4e6d-9b5c-cf5afadb03a3"></td>
    <td width="32%"><img src="https://github.com/duanxianpi/artistic-qrcode-generator/assets/97914968/86d18b4e-c1e7-4086-b052-eb0975a54fbb"></td>
  </tr>
  <tr>
    <td width="32%"><img src="https://github.com/duanxianpi/artistic-qrcode-generator/assets/97914968/6507d016-1ebd-469c-b5a7-8d72010e31f7"></td>
    <td width="32%"><img src="https://github.com/duanxianpi/artistic-qrcode-generator/assets/97914968/8b316605-e944-42e1-9dd6-67881bce3341"></td>
    <td width="32%"><img src="https://github.com/duanxianpi/artistic-qrcode-generator/assets/97914968/c7a87897-73f6-40a3-a628-99f30b793768"></td>
  </tr>
</table>
