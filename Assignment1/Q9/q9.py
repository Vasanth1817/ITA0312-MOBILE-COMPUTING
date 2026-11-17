from pathlib import Path
import csv
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent; (ROOT/'data').mkdir(exist_ok=True); (ROOT/'figures').mkdir(exist_ok=True)
# Key measured/reported evidence consolidated from the assignment's experiment summary.
rows=[('Q1 store-and-forward',300,910),('Q2 bursty utilisation',14.2,78.4),('Q3 BER comparison',0.032,0.00041),('Q7 fairness',0.64,0.91)]
with (ROOT/'data'/'performance_summary.csv').open('w',newline='') as f:
 w=csv.writer(f); w.writerow(['experiment','baseline_value','improved_value']); w.writerows(rows)
fig,axs=plt.subplots(2,2,figsize=(9,6));
for ax,(name,a,b) in zip(axs.flat,rows): ax.bar(['Baseline','Improved'],[a,b]); ax.set_title(name); ax.grid(axis='y',alpha=.25)
fig.suptitle('Q9 — Experimental performance summary'); fig.tight_layout(); fig.savefig(ROOT/'figures'/'performance_summary.png',dpi=170); plt.close(fig)
print('Summary saved. Note: metrics use their own units/scales; compare within each experiment only.')