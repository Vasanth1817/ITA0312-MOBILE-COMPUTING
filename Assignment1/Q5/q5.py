"""Q5: Scaling analysis with Erlang-B blocking and subscriber growth."""
import numpy as np, csv, os, matplotlib.pyplot as plt
def erlang_b(A,C):
    b=1.0
    for c in range(1,C+1): b=A*b/(c+A*b)
    return b
subs=[1000,10000,20000,100000,150000,250000]
load=[s*.025 for s in subs]
sites=19; channels_per_site=171
per_site=np.array(load)/sites
blocking=[100*erlang_b(a,channels_per_site) for a in per_site]
os.makedirs("Assignment1/Q5/data",exist_ok=True)
os.makedirs("Assignment1/Q5/figures",exist_ok=True)
with open("Assignment1/Q5/data/scaling_data.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(["subscribers","offered_traffic_erlang","load_per_site_erlang","blocking_percent"])
    w.writerows(zip(subs,load,per_site,blocking))
fig,ax=plt.subplots(figsize=(7,4.5))
ax.plot(subs,blocking,marker="o")
ax.axhline(2,color="red",linestyle="--",label="2% target")
ax.set(xlabel="Subscribers",ylabel="Blocking probability (%)",title="Q5 — Subscriber scaling (19 sites, 171 channels/site)")
ax.grid(alpha=.3); ax.legend(); plt.tight_layout()
plt.savefig("Assignment1/Q5/figures/output.png",dpi=160); plt.show()
