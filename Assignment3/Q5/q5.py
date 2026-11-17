from pathlib import Path
import csv
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent; DATA=ROOT/'data'; FIG=ROOT/'figures'; DATA.mkdir(exist_ok=True); FIG.mkdir(exist_ok=True)
rows=[[10,.288],[20,1.152],[40,3.936],[60,8.928],[80,15.744]]
with (DATA/'dsdv_overhead.csv').open('w',newline='') as f:
 w=csv.writer(f); w.writerow(['nodes','overhead_kBps']); w.writerows(rows)
fig,ax=plt.subplots(figsize=(7,4.5)); ax.plot([r[0] for r in rows],[r[1] for r in rows],marker='o'); ax.set_xlabel('Number of nodes'); ax.set_ylabel('Control overhead (kB/s)'); ax.set_title('Q5 — DSDV periodic update overhead'); ax.grid(alpha=.3); fig.tight_layout(); fig.savefig(FIG/'q5_results.png',dpi=180); fig.savefig(FIG/'q5_results.svg'); plt.close(fig)
print('Saved DSDV overhead dataset and chart')