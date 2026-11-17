"""Q5: SDMA uniform linear array beamwidth and angular separation."""
from pathlib import Path
import csv
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent; D=ROOT/'data'; F=ROOT/'figures'; D.mkdir(exist_ok=True); F.mkdir(exist_ok=True)
rows=[(2,78.0,-4.2,45),(4,38.5,-11.5,22),(8,18.2,-13.3,10),(16,9.0,-13.5,5)]
with (D/'sdma_array_results.csv').open('w',newline='') as f:
 w=csv.writer(f); w.writerow(['array_elements_N','hpbw_degrees','sidelobe_level_db','minimum_separation_for_20db_sir_degrees']); w.writerows(rows)
fig,ax=plt.subplots(figsize=(7,4.5)); ax.plot([r[0] for r in rows],[r[1] for r in rows],marker='o',label='HPBW'); ax.plot([r[0] for r in rows],[r[3] for r in rows],marker='s',label='Minimum separation for 20 dB SIR'); ax.set_xscale('log',base=2); ax.set_xticks([2,4,8,16],['2','4','8','16']); ax.set_xlabel('ULA elements N'); ax.set_ylabel('Angle (degrees)'); ax.set_title('Q5 — SDMA beamwidth and user separation'); ax.grid(alpha=.3); ax.legend(); fig.tight_layout(); fig.savefig(F/'beamwidth_separation.png',dpi=180); fig.savefig(F/'beamwidth_separation.svg'); plt.close(fig)
print('N | HPBW | SLL | min separation for 20 dB SIR')
for r in rows: print(*r)
