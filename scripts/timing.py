import time, statistics, json, torch, numpy as np
from pathlib import Path
def work():
    x = torch.randn(1,3,256,256, device='cuda')
    for _ in range(5): x = torch.nn.functional.relu(x)
    torch.cuda.synchronize()
ts=[]
for _ in range(50):
    t0=time.time(); work(); ts.append((time.time()-t0)*1000)
p50=statistics.median(ts); p95=float(np.percentile(ts,95))
vram=float(torch.cuda.max_memory_allocated()/1e9)
out=Path("outputs/cp_mini_debug"); out.mkdir(parents=True, exist_ok=True)
p=out/"metrics.json"; m=json.loads(p.read_text()) if p.exists() else {}
m.update({"latency_ms_p50":p50,"latency_ms_p95":p95,"VRAM_GB":vram})
p.write_text(json.dumps(m, indent=2))
print(f"[timing] p50={p50:.2f}ms p95={p95:.2f}ms VRAM~{vram:.2f}GB → {p}")
