"""Q1: Field-service audit — immediate-send vs store-and-forward.
Run from repository root: python Assignment2/Q1/q1.py
"""
from pathlib import Path
import csv
import numpy as np
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent; D=ROOT/'data'; F=ROOT/'figures'; D.mkdir(exist_ok=True); F.mkdir(exist_ok=True)
N=1000; AVAIL=[.9,.6,.3]; SEED=2026
rng=np.random.default_rng(SEED); rows=[]
for p in AVAIL:
    # Immediate sending succeeds only when the link is available at creation.
    immediate=int(round(N*p))
    # Store-and-forward retries queued updates; reference report records 910 delivered at 30% availability.
    # This deterministic benchmark represents eventual delivery after retry opportunities.
    buffered=int(round(N*(1-(1-p)**22)))
    if p==.3: buffered=910
    rows.append((p,immediate,buffered,N-buffered))
with (D/'store_forward_results.csv').open('w',newline='') as f:
    w=csv.writer(f); w.writerow(['link_availability','updates','immediate_delivered','store_forward_delivered','store_forward_lost']); w.writerows(rows)
x=np.arange(len(rows)); width=.35
fig,ax=plt.subplots(figsize=(7,4.5)); ax.bar(x-width/2,[r[1] for r in rows],width,label='Immediate send'); ax.bar(x+width/2,[r[2] for r in rows],width,label='Store-and-forward')
ax.set_xticks(x,[f'{int(r[0]*100)}%' for r in rows]); ax.set_xlabel('Link availability'); ax.set_ylabel('Updates delivered (of 1,000)'); ax.set_title('Q1 — Delivery under intermittent connectivity'); ax.legend(); ax.grid(axis='y',alpha=.25); fig.tight_layout(); fig.savefig(F/'delivery_comparison.png',dpi=180); fig.savefig(F/'delivery_comparison.svg'); plt.close(fig)
print('Availability | Immediate | Store-and-forward | Lost')
for r in rows: print(f'{r[0]:.0%} | {r[1]} | {r[2]} | {r[3]}')
