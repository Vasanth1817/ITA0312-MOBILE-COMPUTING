"""Model-based Android/iOS lifecycle and resource validation; not device measurements."""
from dataclasses import dataclass
@dataclass
class Policy:
    platform:str; background_allowed:bool; memory_pressure_kill:bool; scheduled_work:bool
cases=[("foreground",True),("background",False),("memory pressure",False),("scheduled task",True)]
policies=[Policy("Android",True,True,True),Policy("iOS",False,True,True)]
print("Scenario | Android model | iOS model")
for name,_ in cases:
    a=("active" if name=="foreground" else "restricted/conditional" if name in ("background","scheduled task") else "may be reclaimed")
    i=("active" if name=="foreground" else "suspended/limited" if name in ("background","scheduled task") else "may be reclaimed")
    print(f"{name:18} | {a:22} | {i}")
print("\nModel assumptions only; validate on target devices with lifecycle logs.")
