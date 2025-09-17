FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive PIP_NO_CACHE_DIR=1 PYTHONUNBUFFERED=1 MPLBACKEND=Agg

# Base packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 python3-pip python3-dev git ffmpeg libgl1 libglib2.0-0 && \
    rm -rf /var/lib/apt/lists/*

# PyTorch (CUDA 12.1 wheels)
RUN pip3 install --index-url https://download.pytorch.org/whl/cu121 torch torchvision torchaudio

# Project deps (these may drag numpy up; that's OK for now)
RUN pip3 install nuscenes-devkit==1.1.11 opencv-python tqdm pyyaml einops imageio

# ---- FINAL, AUTHORITATIVE PINS (must be last) ----
# Lock to ABI-safe versions known to work with these wheels
RUN pip3 install --upgrade --no-cache-dir \
    numpy==1.26.4 matplotlib==3.8.4 pandas==2.1.4

# Build-time sanity print (lets you see versions during `make up`)
RUN python3 - <<'PY'
import numpy, matplotlib, pandas, torch
print("numpy =", numpy.__version__)
print("matplotlib =", matplotlib.__version__)
print("pandas =", pandas.__version__)
print("torch =", torch.__version__)
PY

WORKDIR /workspace
