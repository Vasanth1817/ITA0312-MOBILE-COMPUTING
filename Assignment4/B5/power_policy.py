"""Illustrative mobile power policy with threshold hysteresis."""
def choose(battery, charging, network, thermal):
 if charging: return "normal sampling; upload when network permits"
 if thermal>=2: return "reduced sampling; defer bulk upload"
 if battery<15: return "critical: sparse sampling; defer bulk upload"
 if battery<30: return "low: batch upload; sparse sampling"
 if network=="offline": return "queue data; no upload"
 return "balanced sampling; opportunistic upload"
tests=[(80,False,"wifi",0),(25,False,"metered",0),(12,False,"wifi",1),(60,False,"offline",0),(50,True,"wifi",0)]
for x in tests: print(x,"->",choose(*x))
