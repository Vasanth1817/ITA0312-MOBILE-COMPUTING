"""Q7: Closed-form splitting rounds and power/cost interpretation."""
import math, csv, os, matplotlib.pyplot as plt
C0=19; targets=[19,76,304,1216,4864]
rows=[]
for target in targets:
    k=math.ceil(math.log(target/C0,4)) if target>C0 else 0
    rows.append((target,k,C0*4**k,4**k,1/(16**k)))
os.makedirs("Assignment1/Q7/data",exist_ok=True)
os.makedirs("Assignment1/Q7/figures",exist_ok=True)
with open("Assignment1/Q7/data/splitting_rounds.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(["target_sites","minimum_rounds","achieved_sites","relative_site_cost","relative_power_n4"]); w.writerows(rows)
ks=range(0,5); cost=[4**k for k in ks]; power=[16**(-k) for k in ks]
fig,ax=plt.subplots(figsize=(7,4.5))
ax.plot(list(ks),cost,marker="o",label="Relative site count / cost")
ax.plot(list(ks),power,marker="s",label="Relative transmit power (n=4)")
ax.set_yscale("log"); ax.set(xlabel="Splitting rounds k",ylabel="Relative factor (log scale)",title="Q7 — Closed-form scaling trade-off")
ax.grid(alpha=.3); ax.legend(); plt.tight_layout()
plt.savefig("Assignment1/Q7/figures/output.png",dpi=160); plt.show()
print("C_k=C0*4^k; k=ceil(log_4(D_target/C0)); P_k=P0/16^k for n=4.")
