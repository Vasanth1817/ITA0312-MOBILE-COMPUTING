"""B3 comparison of exhaustive configuration enumeration."""
from pathlib import Path
import csv
D=Path(__file__).parent/'data';D.mkdir(exist_ok=True);(Path(__file__).parent/'figures').mkdir(exist_ok=True)
rows=[]
for q in [0.5,0.75,1.0,1.25,1.5]:
 for c in [1,2,4,8]: rows.append({'quality':q,'cache_units':c,'estimated_cost':round(20+10*(1.5-q)+2*c+abs(q-1)*8,2)})
with (D/'results.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
print('Configurations evaluated:',len(rows));print(rows)
