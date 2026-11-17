# Q12 — Day-4 Design Challenge: Stadium Surge Event

## Objective
Evaluate how a mobile network should respond to a sudden stadium traffic surge.

## Methodology
The Python model represents four event phases using normalized offered demand and a normalized capacity baseline. It records overload and plots demand against capacity. The values are illustrative planning assumptions, not measured stadium traffic.

## Recommended response
Deploy temporary microcells or cells-on-wheels, activate sectorisation, borrow channels dynamically from neighbouring low-load cells, apply admission control to non-critical traffic, and monitor handover and interference during arrival, halftime and dispersal.

## Run
```bash
pip install -r Assignment1/Q12/requirements.txt
python Assignment1/Q12/q12.py
```

## Output
The script creates `data/stadium_surge.csv` and `figures/stadium_surge.png`.