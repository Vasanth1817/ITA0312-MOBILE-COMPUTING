"""B4 illustrative encoding policy and resource estimates."""
from pathlib import Path
import csv
D=Path(__file__).parent/'data';D.mkdir(exist_ok=True);(Path(__file__).parent/'figures').mkdir(exist_ok=True)
rows=[]
for name,cores,battery,mbps in [('Low-end',2,22,1.5),('Mid-range',4,58,6),('Flagship',8,78,20),('Mid-range B',6,42,12)]:
 quality='360p' if battery<30 or mbps<3 else ('720p' if mbps<10 or cores<6 else '1080p')
 bitrate={'360p':500,'720p':1800,'1080p':3500}[quality]
 secs=round(10*bitrate/(mbps*1000),2);energy=round(secs*(0.05+cores*0.02),2)
 rows.append({'device':name,'cores':cores,'battery_pct':battery,'network_mbps':mbps,'quality':quality,'bitrate_kbps':bitrate,'estimated_upload_seconds':secs,'energy_proxy':energy})
with (D/'results.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
print(rows)
