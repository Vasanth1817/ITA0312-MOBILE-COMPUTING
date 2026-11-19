"""Deterministic illustrative simulation for A2: Incremental and Constraint-Aware Synchronisation."""
from pathlib import Path
import csv
ROOT=Path(__file__).resolve().parent
DATA=ROOT/'data'; FIG=ROOT/'figures'; DATA.mkdir(exist_ok=True); FIG.mkdir(exist_ok=True)
rows=[]
scenarios=[('Wi-Fi healthy',85,'wifi',False,True),('Offline low battery',12,'offline',True,True),('Metered Doze',18,'metered',True,True),('Permission revoked',60,'wifi',False,False)]
for name,battery,network,doze,permission in scenarios:
    ok=permission and battery>=20 and network!='offline' and not doze
    rows.append({'scenario':name,'battery_pct':battery,'network':network,'doze':doze,'permission':permission,'decision':'execute' if ok else ('cancel' if not permission else 'defer')})
with (DATA/'results.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print(*rows,sep='\\n')
print('CSV saved:',DATA/'results.csv')
