import json
from pathlib import Path
p = Path("outputs/cp_mini_debug/metrics.json")
m = json.loads(p.read_text()) if p.exists() else {}
m["eval_ran"] = True
p.write_text(json.dumps(m, indent=2))
print("[eval_cp] updated", p)
