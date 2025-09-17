import os, sys, pathlib, torch
root = os.environ.get("NUSCENES") or os.environ.get("NUSCENES_DIR")
print("NUSCENES root:", root)
need = ["samples","sweeps","maps","v1.0-mini"]
missing = [d for d in need if not (pathlib.Path(root)/d).exists()]
print("CUDA available:", torch.cuda.is_available())
if missing:
    print("Missing dirs:", missing); sys.exit(2)
print("OK: dataset structure looks right.")
