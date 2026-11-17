from pathlib import Path
import csv
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent; DATA=ROOT/'data'; FIG=ROOT/'figures'; DATA.mkdir(exist_ok=True); FIG.mkdir(exist_ok=True)
rows=[['one_way_delay',150,82,'ms'],['ECG_delivery',99,99.47,'%'],['handoff_interruption',200,160,'ms'],['maximum_speed',30,30,'m/s']]
with (DATA/'healthcare_targets.csv').open('w',newline='') as f:
 w=csv.writer(f); w.writerow(['metric','target','model_value','unit']); w.writerows(rows)
fig,ax=plt.subplots(figsize=(8,4.8)); labels=[r[0] for r in rows]; vals=[r[2] for r in rows]; ax.bar(labels,vals); ax.set_title('Q4 — Mobile healthcare model checks'); ax.set_ylabel('Model value (see units in CSV)'); ax.tick_params(axis='x',rotation=20); ax.grid(axis='y',alpha=.3); fig.tight_layout(); fig.savefig(FIG/'q4_results.png',dpi=180); fig.savefig(FIG/'q4_results.svg'); plt.close(fig)
print('Saved healthcare_targets.csv and q4_results charts')