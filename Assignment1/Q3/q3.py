"""Q3: Calculate hexagonal geometry, reuse ratio and SIR curves."""
import numpy as np, csv, os
import matplotlib.pyplot as plt
N = np.array([3,4,7,12])
R = 0.5
n_values = [2.5,3.0,4.0]
area = (3*np.sqrt(3)/2)*R**2
q = np.sqrt(3*N)
os.makedirs("Assignment1/Q3/data",exist_ok=True)
os.makedirs("Assignment1/Q3/figures",exist_ok=True)
with open("Assignment1/Q3/data/reuse_data.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(["cluster_N","reuse_ratio_Q","SIR_omni_n2_5_dB","SIR_omni_n3_dB","SIR_omni_n4_dB"])
    for i,qi in zip(N,q):
        w.writerow([i,qi,*[10*np.log10((3*i)**(n/2)/6) for n in n_values]])
fig,ax=plt.subplots(figsize=(7,4.5))
for n in n_values: ax.plot(N,10*np.log10((3*N)**(n/2)/6),marker="o",label=f"n={n}")
ax.set(xlabel="Cluster size N",ylabel="Analytical SIR (dB)",title=f"Q3 — SIR vs cluster size (cell area={area:.3f} km²)")
ax.grid(alpha=.3); ax.legend(); plt.tight_layout()
plt.savefig("Assignment1/Q3/figures/output.png",dpi=160); plt.show()
print(f"Hexagonal cell area={area:.4f} km²; reuse ratio Q=sqrt(3N).")
