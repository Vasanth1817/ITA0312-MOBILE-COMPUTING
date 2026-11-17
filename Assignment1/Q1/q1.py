"""Q1: Compare four frequency-planning strategies from the assignment."""
import matplotlib.pyplot as plt
strategies = ["Fixed reuse", "120° sectoring", "Macro/micro", "Dynamic borrowing"]
features = [48, 48, 48, 48]  # baseline N=7 channels/cell; qualitative comparison
interferers = [6, 2, 6, 6]
fig, ax = plt.subplots(figsize=(8, 4.8))
bars = ax.bar(strategies, interferers)
ax.set_ylabel("Effective first-tier interferers")
ax.set_title("Q1 — Frequency-planning strategy comparison")
ax.set_ylim(0, 7)
ax.grid(axis="y", alpha=.25)
for b, v in zip(bars, interferers): ax.text(b.get_x()+b.get_width()/2, v+.12, str(v), ha="center")
plt.xticks(rotation=15, ha="right"); plt.tight_layout()
plt.savefig("Assignment1/Q1/figures/output.png", dpi=160); plt.show()
print("N=7 gives 336/7 = 48 channels per cell. 120° sectoring reduces effective interferers from 6 to 2.")
