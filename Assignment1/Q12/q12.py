from pathlib import Path
import csv
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent; (ROOT/'data').mkdir(exist_ok=True); (ROOT/'figures').mkdir(exist_ok=True)
scenarios=['Normal day','Event arrival','Peak halftime','Dispersal']; demand=[0.55,0.85,1.35,0.95]; capacity=[1.0]*4
with (ROOT/'data'/'stadium_surge.csv').open('w',newline='') as f:
 w=csv.writer(f); w.writerow(['scenario','normalized_demand','normalized_capacity','overload']); w.writerows((s,d,c,max(0,d-c)) for s,d,c in zip(scenarios,demand,capacity))
fig,ax=plt.subplots(figsize=(8,4.5)); x=range(len(scenarios)); ax.plot(list(x),demand,marker='o',label='Demand'); ax.plot(list(x),capacity,linestyle='--',label='Available capacity'); ax.set_xticks(list(x),scenarios); ax.set_ylabel('Normalized load'); ax.set_title('Q12 — Stadium surge capacity stress test'); ax.legend(); ax.grid(alpha=.3); fig.tight_layout(); fig.savefig(ROOT/'figures'/'stadium_surge.png',dpi=170); plt.close(fig)
print('Peak surge overload:',max(0,max(demand)-1.0)); print('Mitigation: temporary microcells, sectorisation, dynamic borrowing and admission control.')