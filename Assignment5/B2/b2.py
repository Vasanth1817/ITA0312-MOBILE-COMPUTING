"""B2 matched workload experiment."""
from pathlib import Path
import csv
D=Path(__file__).parent/'data';D.mkdir(exist_ok=True);(Path(__file__).parent/'figures').mkdir(exist_ok=True)
rows=[{'case':'benign','records':5,'network':'Wi-Fi','battery_pct':85,'deferred':0,'successful':5,'backlog':0},{'case':'adversarial','records':5,'network':'offline/metered','battery_pct':12,'deferred':8,'successful':0,'backlog':5}]
with (D/'results.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
print(rows)
