from pathlib import Path
import csv
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent; DATA=ROOT/'data'; FIG=ROOT/'figures'; DATA.mkdir(exist_ok=True); FIG.mkdir(exist_ok=True)
rows=[[0,86.3,86.3,2.30,1.38,39.4,39.7],[2,87.5,89.8,2.41,1.52,34.1,41.5],[5,87.1,94.0,2.63,1.40,28.4,36.3],[10,79.4,95.6,2.98,1.67,26.9,36.5],[20,66.7,95.3,3.62,2.31,26.2,41.5],[30,59.6,94.2,4.26,2.84,25.2,43.4]]
with (DATA/'dsdv_aodv_mobility.csv').open('w',newline='') as f:
 w=csv.writer(f); w.writerow(['speed_mps','dsdv_delivery_pct','aodv_delivery_pct','dsdv_overhead_kBps','aodv_overhead_kBps','dsdv_delay_ms','aodv_delay_ms']); w.writerows(rows)
fig,ax=plt.subplots(figsize=(7.5,4.8)); ax.plot([r[0] for r in rows],[r[1] for r in rows],marker='o',label='DSDV'); ax.plot([r[0] for r in rows],[r[2] for r in rows],marker='s',label='AODV'); ax.set_xlabel('Maximum node speed (m/s)'); ax.set_ylabel('Packet delivery ratio (%)'); ax.set_title('Q6 — DSDV vs AODV delivery under mobility'); ax.grid(alpha=.3); ax.legend(); fig.tight_layout(); fig.savefig(FIG/'q6_results.png',dpi=180); fig.savefig(FIG/'q6_results.svg'); plt.close(fig)
print('Saved DSDV/AODV simulation comparison dataset and chart')