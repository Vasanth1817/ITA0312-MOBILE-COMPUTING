"""Deterministic illustrative simulation for A4: Local vs Cloud vs Hybrid Processing."""
from pathlib import Path
import csv
ROOT=Path(__file__).resolve().parent
DATA=ROOT/'data'; FIG=ROOT/'figures'; DATA.mkdir(exist_ok=True); FIG.mkdir(exist_ok=True)
rows=[]
items=[('Image classification','local','low latency'),('Speech recognition','cloud/hybrid','network and privacy trade-off'),('P2P file sharing','hybrid','authenticated resumable transfer'),('Messaging','local/hybrid','encrypt locally'),('Game state','hybrid','reconcile authority'),('Offline maps','local/hybrid','cached data')]
rows=[{'workload':a,'placement':b,'reason':c} for a,b,c in items]
with (DATA/'results.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print(*rows,sep='\\n')
print('CSV saved:',DATA/'results.csv')
