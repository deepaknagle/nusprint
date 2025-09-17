from pathlib import Path
import imageio.v2 as imageio, numpy as np
out = Path("outputs/demos"); out.mkdir(parents=True, exist_ok=True)
frames = [(np.random.rand(256,256,3)*255).astype('uint8') for _ in range(30)]
imageio.mimsave(out/"cp_demo.gif", frames, duration=0.05)
print("[demo] wrote", out/"cp_demo.gif")
