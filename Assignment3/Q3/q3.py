from pathlib import Path
import csv
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent; DATA=ROOT/'data'; FIG=ROOT/'figures'; DATA.mkdir(exist_ok=True); FIG.mkdir(exist_ok=True)
rows=[["Infrastructure",5,1],["Infrastructure independence",1,5],["Multi-hop resilience",2,5],["Planned wide-area coverage",5,2],["Rapid disaster deployment",2,5]]
with (DATA/"cellular_adhoc_comparison.csv").open('w',newline='') as f:
 w=csv.writer(f); w.writerow(["criterion","cellular_score","adhoc_score"]); w.writerows(rows)
fig,ax=plt.subplots(figsize=(8,4.8)); ax.axis('off'); ax.set_title("Q3 — Cellular vs ad hoc comparison",pad=20); table=ax.table(cellText=rows,colLabels=["criterion","cellular_score","adhoc_score"],loc='center'); table.auto_set_font_size(False); table.set_fontsize(9); table.scale(1,1.5); fig.tight_layout(); fig.savefig(FIG/"q3_results.png",dpi=180); fig.savefig(FIG/"q3_results.svg"); plt.close(fig)
print('Wrote dataset:', "cellular_adhoc_comparison.csv"); print('Charts saved in figures/')
