# Node QRCode Toolkit
A cli app to generate QR Code according to the configs of [Anthony's QRCode Toolkit](https://github.com/antfu/qrcode-toolkit).  

## Build
```bash
git https://github.com/duanxianpi/qrcode-toolkit-node
npm install
tsc --build
```

## Usage
### Step 1.
Customize the qr code style from [Anthony's QRCode Toolkit](https://qrcode.antfu.me/), download the config
![image](https://github.com/duanxianpi/qrcode-toolkit-node/assets/97914968/81c290e8-3f1a-420d-84f5-e41fa6be2272)

### Step 2.
```text
$ node build/index.js -h
Usage: index [options]

Options:
  -i, --input <string>        Input text to be encoded to qrcode, it will override the text in the config file
  -c, --config <string>       Config to control the style of qr code
  -o, --output_path <string>  the output path of result image, defualt value is current directory
  -n, --filename <string>     the filename result image, defualt value is qrcode
  -h, --help                  display help for command
```
