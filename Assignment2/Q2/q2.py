"""Q2: Compare FDMA and TDMA capacity and traffic utilisation."""
from pathlib import Path
import csv
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent; D=ROOT/'data'; F=ROOT/'figures'; D.mkdir(exist_ok=True); F.mkdir(exist_ok=True)
# Values transcribed from the assignment's Table 3.1.
rows=[('Continuous Voice',88.5,2.1,85.0,3.2),('Bursty Data (10% duty)',14.2,0.0,78.4,1.1),('70/30 Voice-Data Mix',65.0,4.5,82.1,2.0),('Synchronized Bursts',42.0,18.5,91.2,6.4)]
with (D/'fdma_tdma_results.csv').open('w',newline='') as f:
 w=csv.writer(f); w.writerow(['traffic_condition','fdma_utilisation_pct','fdma_blocking_pct','tdma_utilisation_pct','tdma_blocking_pct']); w.writerows(rows)
fig,axs=plt.subplots(1,2,figsize=(11,4.5)); labels=[r[0] for r in rows]; x=range(len(rows)); width=.36
axs[0].bar([i-width/2 for i in x],[r[1] for r in rows],width,label='FDMA'); axs[0].bar([i+width/2 for i in x],[r[3] for r in rows],width,label='TDMA'); axs[0].set_title('Channel utilisation'); axs[0].set_ylabel('%'); axs[0].legend()
axs[1].bar([i-width/2 for i in x],[r[2] for r in rows],width,label='FDMA'); axs[1].bar([i+width/2 for i in x],[r[4] for r in rows],width,label='TDMA'); axs[1].set_title('Blocking probability'); axs[1].set_ylabel('%'); axs[1].legend()
for ax in axs: ax.set_xticks(list(x),labels,rotation=20,ha='right'); ax.grid(axis='y',alpha=.25)
fig.suptitle('Q2 — FDMA vs TDMA under different traffic conditions'); fig.tight_layout(); fig.savefig(F/'fdma_tdma_comparison.png',dpi=180); fig.savefig(F/'fdma_tdma_comparison.svg'); plt.close(fig)
print('FDMA usable channels=floor(2000/(25+1))=76; TDMA=floor(10*8*(1-.12))=70.')
