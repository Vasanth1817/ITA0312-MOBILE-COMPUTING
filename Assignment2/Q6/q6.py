"""Q6: Weighted decision matrix for selecting a multiple-access technique.
Scores below are explicit qualitative engineering ratings, not measured values from the report.
"""
from pathlib import Path
import csv
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent; D=ROOT/'data'; F=ROOT/'figures'; D.mkdir(exist_ok=True); F.mkdir(exist_ok=True)
weights={'capacity':25,'spectral_efficiency':20,'fairness':20,'complexity':20,'cost':15}
# Transparent 1–5 design scores for an illustrative weighted decision matrix.
scores={'FDMA':[2,2,3,4,5],'TDMA':[3,3,3,4,4],'CDMA':[4,4,3,2,3],'OFDMA':[5,5,4,3,2],'SDMA':[4,4,3,2,2]}
scenarios={'Baseline':weights,'Spectrum-heavy':{'capacity':30,'spectral_efficiency':30,'fairness':15,'complexity':15,'cost':10},'Cost-dominant':{'capacity':15,'spectral_efficiency':10,'fairness':10,'complexity':25,'cost':40}}
with (D/'weighted_decision_matrix.csv').open('w',newline='') as f:
 w=csv.writer(f); w.writerow(['technique','capacity_score','spectral_efficiency_score','fairness_score','complexity_score','cost_score']+list(scenarios))
 for tech,vals in scores.items():
  totals=[sum(v*wt/100 for v,wt in zip(vals,sw.values())) for sw in scenarios.values()]; w.writerow([tech]+vals+[round(x,3) for x in totals])
fig,ax=plt.subplots(figsize=(8,4.8)); techs=list(scores)
for i,(name,sw) in enumerate(scenarios.items()):
 vals=[sum(v*wt/100 for v,wt in zip(scores[t],sw.values())) for t in techs]; ax.bar([j+(i-1)*.25 for j in range(len(techs))],vals,.25,label=name)
ax.set_xticks(range(len(techs)),techs); ax.set_ylabel('Weighted score (1–5)'); ax.set_title('Q6 — Multiple-access technique selection'); ax.legend(); ax.grid(axis='y',alpha=.25); fig.tight_layout(); fig.savefig(F/'selection_scores.png',dpi=180); fig.savefig(F/'selection_scores.svg'); plt.close(fig)
print('Weights (baseline):',weights); print('Illustrative ratings are documented in the script and CSV.')
