from pathlib import Path
import csv
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent; (ROOT/'data').mkdir(exist_ok=True); (ROOT/'figures').mkdir(exist_ok=True)
criteria=['Capacity','Interference control','Scalability','Implementation simplicity']
# Transparent qualitative engineering scores on a 1–5 scale.
scores={'Fixed reuse':[3,3,2,5],'Sectorised reuse':[4,5,3,3],'Macro-micro + dynamic allocation':[5,4,5,2]}
with (ROOT/'data'/'design_scores.csv').open('w',newline='') as f:
 w=csv.writer(f); w.writerow(['design']+criteria); [w.writerow([k]+v) for k,v in scores.items()]
fig,ax=plt.subplots(figsize=(8,4.5)); width=.24; x=list(range(len(criteria)))
for j,(name,vals) in enumerate(scores.items()): ax.bar([i+(j-1)*width for i in x],vals,width,label=name)
ax.set_xticks(x,criteria); ax.set_ylim(0,5.5); ax.set_ylabel('Engineering score (1–5)'); ax.set_title('Q11 — Multi-criteria design recommendation'); ax.legend(fontsize=8); ax.grid(axis='y',alpha=.25); fig.tight_layout(); fig.savefig(ROOT/'figures'/'design_scores.png',dpi=170); plt.close(fig)
print('Recommended hybrid: macro-micro capacity layer with sectorisation and dynamic channel allocation.')