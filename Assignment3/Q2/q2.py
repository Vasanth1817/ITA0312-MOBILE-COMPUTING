from pathlib import Path
import csv
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent; DATA=ROOT/'data'; FIG=ROOT/'figures'; DATA.mkdir(exist_ok=True); FIG.mkdir(exist_ok=True)
rows=[["registration_rtt",89,"ms"],["ipip_header",20,"bytes"],["overhead_1000B_payload",2,"%"],["overhead_200B_payload",10,"%"],["triangular_route_delay",82,"ms"],["direct_route_delay",40,"ms"],["packets_affected_at_50pps",8,"packets"]]
with (DATA/"mobile_ip_calculations.csv").open('w',newline='') as f:
 w=csv.writer(f); w.writerow(["metric","value","unit"]); w.writerows(rows)
fig,ax=plt.subplots(figsize=(8,4.8)); ax.axis('off'); ax.set_title("Q2 — Mobile IP worked calculations",pad=20); table=ax.table(cellText=rows,colLabels=["metric","value","unit"],loc='center'); table.auto_set_font_size(False); table.set_fontsize(9); table.scale(1,1.5); fig.tight_layout(); fig.savefig(FIG/"q2_results.png",dpi=180); fig.savefig(FIG/"q2_results.svg"); plt.close(fig)
print('Wrote dataset:', "mobile_ip_calculations.csv"); print('Charts saved in figures/')
