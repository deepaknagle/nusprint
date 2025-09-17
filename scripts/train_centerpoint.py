import json, time
from pathlib import Path
out = Path("outputs/cp_mini_debug"); out.mkdir(parents=True, exist_ok=True)
print("[train_cp] stub training…"); time.sleep(2)
(out/"metrics.json").write_text(json.dumps({"NDS":0.07,"mAP":0.06}, indent=2))
print("[train_cp] wrote", out/"metrics.json")
