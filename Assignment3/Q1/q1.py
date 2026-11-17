from pathlib import Path
import csv
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent; DATA=ROOT/'data'; FIG=ROOT/'figures'; DATA.mkdir(exist_ok=True); FIG.mkdir(exist_ok=True)
rows=[[1,0.5,0.04,0.17],[5,2.5,0.21,0.83],[10,5,0.42,1.67],[15,7.5,0.63,2.5],[20,10,0.83,3.33],[30,15,1.25,5]]
with (DATA/"mobility_results.csv").open('w',newline='') as f:
 w=csv.writer(f); w.writerow(["speed_mps","handoffs_per_min","loss_l2_pct","loss_l2_mobile_ip_pct"]); w.writerows(rows)
fig,ax=plt.subplots(figsize=(8,4.8))
ax.plot([r[0] for r in rows],[r[2] for r in rows],marker='o',label="loss_l2_pct")
ax.plot([r[0] for r in rows],[r[3] for r in rows],marker='o',label="loss_l2_mobile_ip_pct")
ax.set_xlabel("Speed (m/s)"); ax.set_ylabel('Percent'); ax.set_title("Q1 — Mobility speed and packet loss"); ax.grid(alpha=.3); ax.legend(); fig.tight_layout(); fig.savefig(FIG/"q1_results.png",dpi=180); fig.savefig(FIG/"q1_results.svg"); plt.close(fig)
print('Wrote dataset:', "mobility_results.csv"); print('Charts saved in figures/')
