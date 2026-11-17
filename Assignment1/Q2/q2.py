"""Q2: Illustrate the governing parameter for each strategy."""
import matplotlib.pyplot as plt
names = ["Fixed reuse", "Sectorised", "Cell splitting", "Dynamic borrowing"]
params = ["Cluster size N", "Sector count / beamwidth", "Cell radius R", "Offered load A/C"]
why = ["Capacity ↔ SIR trade-off", "Controls active interferers", "Controls site density (1/R²)", "Controls load imbalance"]
fig, ax = plt.subplots(figsize=(9, 4.8))
ax.axis("off")
for i, (n,p,w) in enumerate(zip(names,params,why)):
    y=0.88-i*0.22
    ax.text(.03,y,n,weight="bold",fontsize=12,transform=ax.transAxes)
    ax.text(.35,y,p,fontsize=11,transform=ax.transAxes)
    ax.text(.68,y,w,fontsize=10,transform=ax.transAxes)
ax.set_title("Q2 — Governing design parameters", pad=18)
plt.tight_layout(); plt.savefig("Assignment1/Q2/figures/output.png",dpi=160); plt.show()
