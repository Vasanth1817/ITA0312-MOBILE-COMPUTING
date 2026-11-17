"""Q3: DS-CDMA processing gain and near-far BER comparison."""
from pathlib import Path
import csv
import numpy as np
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent; D=ROOT/'data'; F=ROOT/'figures'; D.mkdir(exist_ok=True); F.mkdir(exist_ok=True)
rows=[(8,0,3.2e-2,1.8e-1),(16,0,1.1e-2,9.4e-2),(64,0,4.1e-4,1.2e-2)]
with (D/'cdma_ber_results.csv').open('w',newline='') as f:
 w=csv.writer(f); w.writerow(['code_length','processing_gain_db','ber_orthogonal_sync','ber_random_codes','ber_10x_near_far']);
 for n,_,b1,b2 in rows: w.writerow([n,10*np.log10(n),0,b1,b2])
x=np.array([r[0] for r in rows]); gains=10*np.log10(x)
fig,ax=plt.subplots(figsize=(7,4.5)); ax.semilogy(x,[r[2] for r in rows],marker='o',label='Random PN codes'); ax.semilogy(x,[r[3] for r in rows],marker='s',label='10× near-far'); ax.set_xlabel('Spreading code length N'); ax.set_ylabel('Bit error rate (BER)'); ax.set_title('Q3 — CDMA BER vs code length'); ax.grid(True,which='both',alpha=.25); ax.legend(); fig.tight_layout(); fig.savefig(F/'ber_comparison.png',dpi=180); fig.savefig(F/'ber_comparison.svg'); plt.close(fig)
print('N | processing gain dB | BER random | BER 10x near-far')
for n,g,b1,b2 in rows: print(n,f'{10*np.log10(n):.2f}',b1,b2)
