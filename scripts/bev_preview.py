import os
from pathlib import Path
from nuscenes.nuscenes import NuScenes
from nuscenes.utils.data_classes import LidarPointCloud
import numpy as np, matplotlib.pyplot as plt

root = os.environ.get("NUSCENES_DIR", "/workspace")
nusc = NuScenes(version='v1.0-mini', dataroot=root, verbose=False)
sample = nusc.sample[0]
lidar_tok = sample['data']['LIDAR_TOP']
sd = nusc.get('sample_data', lidar_tok)
pc = LidarPointCloud.from_file(str(Path(root)/sd['filename']))
xy = pc.points[:2]
res, lim = 0.1, 50
bins = np.linspace(-lim, lim, int(2*lim/res))
H, _, _ = np.histogram2d(xy[0], xy[1], bins=[bins,bins])
H = np.clip(H, 0, np.percentile(H, 99))
img = (H / (H.max() + 1e-6))
Path("outputs/figs").mkdir(parents=True, exist_ok=True)
plt.figure(figsize=(6,6)); plt.imshow(img.T, origin='lower', cmap='gray')
plt.title('nuScenes LIDAR_TOP — BEV density (mini)')
plt.tight_layout(); plt.savefig("outputs/figs/sanity_bev.png"); print("wrote outputs/figs/sanity_bev.png")
