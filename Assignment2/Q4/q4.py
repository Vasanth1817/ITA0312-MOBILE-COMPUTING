"""Q4: OFDMA per-user subcarrier scheduling and efficiency/fairness trade-off."""
from pathlib import Path
import csv
import numpy as np
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent; D=ROOT/'data'; F=ROOT/'figures'; D.mkdir(exist_ok=True); F.mkdir(exist_ok=True)
# Report-supported scheme range; intermediate values are explicitly illustrative.
rows=[('Round-robin',34.2,.98),('Proportional-fair',62.0,.88),('Channel-aware',89.4,.64)]
with (D/'ofdma_scheme_reference.csv').open('w',newline='') as f:
 w=csv.writer(f); w.writerow(['scheme','sum_throughput_mbps','jain_fairness','data_status']);
 for name,t,j in rows: w.writerow([name,t,j,'reported endpoint' if name!='Proportional-fair' else 'illustrative midpoint'])
fig,ax=plt.subplots(figsize=(7,4.5)); ax.scatter([r[2] for r in rows],[r[1] for r in rows],s=90)
for name,t,j in rows: ax.annotate(name,(j,t),xytext=(6,6),textcoords='offset points')
ax.set_xlabel("Jain's fairness index"); ax.set_ylabel('Sum throughput (Mbps)'); ax.set_title('Q4 — OFDMA efficiency–fairness comparison'); ax.grid(alpha=.3); fig.tight_layout(); fig.savefig(F/'throughput_fairness.png',dpi=180); fig.savefig(F/'throughput_fairness.svg'); plt.close(fig)
print('The assignment reports sum throughput spanning 34.2–89.4 Mbps and fairness spanning 0.98–0.64 across schemes.')
