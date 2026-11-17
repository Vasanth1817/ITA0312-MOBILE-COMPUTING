from pathlib import Path
import csv
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent; (ROOT/'data').mkdir(exist_ok=True); (ROOT/'figures').mkdir(exist_ok=True)
strategies=['Fixed reuse N=7','120-degree sectoring N=3','Macro-micro layering']
channels=[336/7,336/3,336/3]
interferers=[6,2,2]
with (ROOT/'data'/'strategy_test.csv').open('w',newline='') as f:
 w=csv.writer(f); w.writerow(['strategy','channels_per_cell_before_control_reservation','first_tier_interferers']); w.writerows(zip(strategies,channels,interferers))
fig,ax=plt.subplots(figsize=(8,4.5)); ax.bar(strategies,channels); ax.set_ylabel('Channels per cell / sector (theoretical)'); ax.set_title('Q8 — Implemented strategy comparison'); ax.tick_params(axis='x',rotation=15); ax.grid(axis='y',alpha=.3); fig.tight_layout(); fig.savefig(ROOT/'figures'/'strategy_test.png',dpi=170); plt.close(fig)
print('Q8 test data written to data/strategy_test.csv')