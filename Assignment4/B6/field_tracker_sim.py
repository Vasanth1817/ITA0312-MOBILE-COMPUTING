"""Battery-aware tracker policy simulation. Illustrative, not device telemetry."""
from random import seed
seed(7)
def interval(battery,thermal,moving):
 if thermal>=2 or battery<15: return 120
 if battery<30: return 60
 return 10 if moving else 30
records=0; uploads=0
for step,(battery,thermal,moving,network) in enumerate([(90,0,1,"wifi"),(65,0,1,"metered"),(28,0,0,"wifi"),(12,2,1,"wifi"),(50,0,1,"offline")],1):
 seconds=interval(battery,thermal,moving); records+=1
 sent= network=="wifi" and battery>=20 and thermal<2
 uploads+=int(sent)
 print(f"step {step}: battery={battery}% thermal={thermal} moving={moving} net={network} interval={seconds}s upload={'yes' if sent else 'deferred'}")
print(f"records queued/created={records}, uploaded={uploads}, deferred={records-uploads}")
print("Encrypt queued records and protect upload transport in a production implementation.")
