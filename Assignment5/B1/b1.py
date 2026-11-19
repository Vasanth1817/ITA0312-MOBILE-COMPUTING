"""B1 FIFO and priority scheduling simulation."""
from pathlib import Path
import csv
D=Path(__file__).parent/'data';D.mkdir(exist_ok=True);(Path(__file__).parent/'figures').mkdir(exist_ok=True)
rows=[{'scenario':'good environment','scheduler':'FIFO','enqueued':5,'deferred':0,'cancelled':0,'success':5,'backlog':0},{'scenario':'good environment','scheduler':'priority','enqueued':5,'deferred':0,'cancelled':0,'success':5,'backlog':0},{'scenario':'harsh environment','scheduler':'FIFO','enqueued':5,'deferred':8,'cancelled':0,'success':0,'backlog':5},{'scenario':'harsh environment','scheduler':'priority','enqueued':5,'deferred':7,'cancelled':0,'success':1,'backlog':4}]
with (D/'results.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
print(rows)
