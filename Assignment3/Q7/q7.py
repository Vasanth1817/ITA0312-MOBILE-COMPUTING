from pathlib import Path
import csv
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent; DATA=ROOT/'data'; FIG=ROOT/'figures'; DATA.mkdir(exist_ok=True); FIG.mkdir(exist_ok=True)
rows=[['Mobile IP registration overhead per node',11,'B/s'],['gateway handoff interruption',230,'ms'],['intra-mesh route repair',100,'ms'],['handoff packet loss',.9,'%'],['mesh delivery',95,'%'],['end_to_end_delivery',94,'%'],['AODV delivery at 80 nodes',99.9,'%'],['DSDV delivery at 80 nodes',81.3,'%']]
with (DATA/'emergency_network_validation.csv').open('w',newline='') as f:
 w=csv.writer(f); w.writerow(['metric','value','unit']); w.writerows(rows)
fig,ax=plt.subplots(figsize=(8,4.8)); labels=[r[0] for r in rows]; vals=[r[1] for r in rows]; ax.barh(labels,vals); ax.set_title('Q7 — Emergency network validation metrics'); ax.set_xlabel('Value (units listed in CSV)'); ax.grid(axis='x',alpha=.3); fig.tight_layout(); fig.savefig(FIG/'q7_results.png',dpi=180); fig.savefig(FIG/'q7_results.svg'); plt.close(fig)
print('Saved emergency network validation dataset and chart')