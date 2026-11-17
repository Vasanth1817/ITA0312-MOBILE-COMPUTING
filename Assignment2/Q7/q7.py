"""Q7: Diagnose, redesign and validate OFDMA user starvation.
Run from repository root: python Assignment2/Q7/q7.py
"""
from pathlib import Path
import csv
import numpy as np
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent
DATA,FIG=ROOT/'data',ROOT/'figures'
DATA.mkdir(exist_ok=True); FIG.mkdir(exist_ok=True)
SEED,USERS,K,BW,INTERVALS=731,8,64,20e6,1000
SNR_DB=np.array([24,21,18,15,12,9,6,3],dtype=float)
ALPHAS=[0.0,0.25,0.5,1.0,1.5,2.0]
FLOOR=1.5

def jain(x):
    x=np.asarray(x,dtype=float); d=len(x)*np.sum(x*x)
    return float(np.sum(x)**2/d) if d else 0.0

def simulate(alpha):
    rng=np.random.default_rng(SEED); mean_snr=10**(SNR_DB/10)
    avg=np.full(USERS,1e-3); total=np.zeros(USERS)
    sub_bw=BW/K/1e6
    for _ in range(INTERVALS):
        fading=rng.exponential(1.0,size=(USERS,K))
        rates=sub_bw*np.log2(1+mean_snr[:,None]*fading)
        metric=rates/np.maximum(avg[:,None],1e-3)**alpha
        below=avg<FLOOR
        if np.any(below): metric[below]*=2.5
        winners=np.argmax(metric,axis=0)
        allocated=np.bincount(winners,weights=rates[winners,np.arange(K)],minlength=USERS)
        total+=allocated; avg=.9*avg+.1*allocated
    x=total/INTERVALS
    return float(x.sum()),float(x.min()),jain(x),x

rows=[(a,*simulate(a)) for a in ALPHAS]; greedy=rows[0][1]
with (DATA/'alpha_sweep.csv').open('w',newline='') as f:
    w=csv.writer(f); w.writerow(['alpha','sum_throughput_mbps','minimum_user_mbps','jain_fairness','sum_retained_percent'])
    for a,s,m,j,_ in rows: w.writerow([a,f'{s:.4f}',f'{m:.4f}',f'{j:.4f}',f'{100*s/greedy:.2f}'])
selected=next(r for r in rows if r[0]==1.0)
with (DATA/'alpha1_per_user_rates.csv').open('w',newline='') as f:
    w=csv.writer(f); w.writerow(['user','mean_snr_db','average_throughput_mbps'])
    for i,v in enumerate(selected[4],1): w.writerow([i,SNR_DB[i-1],f'{v:.4f}'])
fig,ax=plt.subplots(figsize=(8,5)); ax.plot([r[0] for r in rows],[r[1] for r in rows],marker='o',label='Sum throughput (Mbps)')
ax.set_xlabel('Fairness exponent alpha'); ax.set_ylabel('Sum throughput (Mbps)'); ax.grid(alpha=.3)
ax2=ax.twinx(); ax2.plot([r[0] for r in rows],[r[3] for r in rows],marker='s',label="Jain's fairness"); ax2.set_ylabel("Jain's fairness index"); ax2.set_ylim(0,1.05)
lines=ax.get_lines()+ax2.get_lines(); ax.legend(lines,[x.get_label() for x in lines]); plt.title('Q7 — Throughput–fairness trade-off'); fig.tight_layout()
fig.savefig(FIG/'alpha_tradeoff.png',dpi=180); fig.savefig(FIG/'alpha_tradeoff.svg'); plt.close(fig)
print('alpha | sum Mbps | min-user Mbps | Jain fairness | retained %')
for a,s,m,j,_ in rows: print(f'{a:4.2f} | {s:8.3f} | {m:13.3f} | {j:12.3f} | {100*s/greedy:9.2f}')
print('Independent simulation; values need not exactly match the DOCX reference tables.')
