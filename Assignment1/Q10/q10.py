from pathlib import Path
import csv
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent; (ROOT/'data').mkdir(exist_ok=True); (ROOT/'figures').mkdir(exist_ok=True)
labels=['Reuse ratio Q (N=7)','SIR (n=4, dB)','Q7 Jain fairness']
theory=[(3*7)**0.5,10*__import__('math').log10((3*7)**2/6),0.90]
simulation=[4.58,21.65,0.91]
with (ROOT/'data'/'theory_vs_simulation.csv').open('w',newline='') as f:
 w=csv.writer(f); w.writerow(['metric','theoretical_or_target','simulation_or_reference']); w.writerows(zip(labels,theory,simulation))
x=range(len(labels)); fig,ax=plt.subplots(figsize=(8,4.5)); ax.bar([i-.18 for i in x],theory,width=.36,label='Theory / target'); ax.bar([i+.18 for i in x],simulation,width=.36,label='Simulation / reference'); ax.set_xticks(list(x),labels); ax.set_title('Q10 — Theory versus simulation'); ax.legend(); ax.grid(axis='y',alpha=.25); fig.tight_layout(); fig.savefig(ROOT/'figures'/'theory_vs_simulation.png',dpi=170); plt.close(fig)
print('Theory/simulation comparison saved.')