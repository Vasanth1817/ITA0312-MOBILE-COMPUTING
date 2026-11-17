"""Q6: Repeated cell-splitting recurrence."""
import csv, os, matplotlib.pyplot as plt
C0=19; rounds=range(0,6); n=4
cells=[C0*4**k for k in rounds]
power=[1/(2**(n*k)) for k in rounds]
os.makedirs("Assignment1/Q6/data",exist_ok=True)
os.makedirs("Assignment1/Q6/figures",exist_ok=True)
with open("Assignment1/Q6/data/recurrence_data.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(["round_k","cells_C0_times_4_power_k","relative_transmit_power_n4"])
    w.writerows(zip(rounds,cells,power))
fig,ax=plt.subplots(figsize=(7,4.5))
ax.plot(list(rounds),cells,marker="o",label="Cell count C₀·4ᵏ")
ax.set_yscale("log"); ax.set(xlabel="Splitting round k",ylabel="Number of sites (log scale)",title="Q6 — Cell count growth")
ax.grid(alpha=.3); ax.legend(); plt.tight_layout()
plt.savefig("Assignment1/Q6/figures/output.png",dpi=160); plt.show()
print("C_k=4 C_(k-1); selective splitting: C_k=(1+3α)C_(k-1); P_k=P_(k-1)/2^n.")
