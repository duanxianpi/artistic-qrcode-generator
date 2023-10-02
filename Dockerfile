FROM pytorch/pytorch:2.0.1-cuda11.7-cudnn8-runtime

WORKDIR /app

# Get NodeJS
COPY --from=node:20-slim /usr/local/bin /usr/local/bin
# Get npm
COPY --from=node:20-slim /usr/local/lib/node_modules /usr/local/lib/node_modules

COPY models/ models/

RUN pip install diffusers --upgrade
RUN pip install omegaconf transformers accelerate safetensors invisible_watermark xformers compel opencv-python-headless boto3
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install ffmpeg libsm6 libxext6 curl -y

COPY node-qrcode-toolkit/ node-qrcode-toolkit/
WORKDIR /app/node-qrcode-toolkit
RUN npm install && npx tsc --build
WORKDIR /app/

RUN curl -L "https://huggingface.co/monster-labs/control_v1p_sd15_qrcode_monster/resolve/main/v2/diffusion_pytorch_model.safetensors" --output diffusion_pytorch_model.safetensors
RUN curl -L "https://huggingface.co/monster-labs/control_v1p_sd15_qrcode_monster/resolve/main/v2/config.json" --output config.json
RUN mkdir models/monster -p && mv diffusion_pytorch_model.safetensors config.json models/monster

RUN curl -L "https://civitai.com/api/download/models/9208?type=Model&format=SafeTensor&size=full&fp=fp16" --output easynegative.safetensors
RUN curl -L "https://civitai.com/api/download/models/5637?type=Model&format=PickleTensor&size=full&fp=fp16" --output ng_deepnegative_v1_75t.pt
RUN mv easynegative.safetensors ng_deepnegative_v1_75t.pt models

COPY src/ src/

WORKDIR /app/src

ENTRYPOINT ["python3", "app.py"]

CMD ["--codido", "False"]