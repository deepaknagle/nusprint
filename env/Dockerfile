FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive PIP_NO_CACHE_DIR=1 PYTHONUNBUFFERED=1

# Base packages for Python + image I/O
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 python3-pip python3-dev git ffmpeg libgl1 libglib2.0-0 && \
    rm -rf /var/lib/apt/lists/*

# PyTorch (CUDA 12.1 wheels)
RUN pip3 install --index-url https://download.pytorch.org/whl/cu121 torch torchvision torchaudio

# Project deps, including nuscenes-devkit
RUN pip3 install nuscenes-devkit==1.1.11 opencv-python matplotlib tqdm pyyaml pandas einops imageio

WORKDIR /workspace
