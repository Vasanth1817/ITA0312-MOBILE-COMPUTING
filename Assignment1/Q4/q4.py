"""Q4: Compare relative SIR at best, average and worst positions."""
import numpy as np, matplotlib.pyplot as plt
N=7; n=4; Q=np.sqrt(3*N)
positions=["Near BS (best)","Mid-cell (typical)","Cell edge (worst)"]
# Normalized received desired signal relative to the cell-edge value.
r=np.array([0.1,0.5,1.0])
relative_db=10*n*np.log10(1/r)
fig,ax=plt.subplots(figsize=(7,4.5))
bars=ax.bar(positions,relative_db)
ax.set_ylabel("Desired-signal advantage vs cell edge (dB)")
ax.set_title(f"Q4 — Spatial variation (N={N}, n={n}, Q={Q:.2f})")
ax.grid(axis="y",alpha=.25)
for b,v in zip(bars,relative_db): ax.text(b.get_x()+b.get_width()/2,v+.5,f"{v:.1f}",ha="center")
plt.xticks(rotation=12,ha="right"); plt.tight_layout()
plt.savefig("Assignment1/Q4/figures/output.png",dpi=160); plt.show()
print(f"Worst-case geometric SIR expression from the report: (Q - 1)^n = {(Q-1)**n:.2f} (linear ratio).")
