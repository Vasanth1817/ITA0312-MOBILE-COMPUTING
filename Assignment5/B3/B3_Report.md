# B3 — Exact vs Approximate UI Optimisation

## Aim
Investigate exact configuration search versus approximate/adaptive strategies for UI performance and cache/resource tuning.

## Experiment
Enumerate five quality levels and four cache levels. The full search evaluates 20 combinations. An adaptive heuristic can restrict candidate choices based on current device conditions, reducing decision work at the cost of potentially missing the global optimum.

## Output
Run `python b3.py` to generate the 20-row results CSV. The cost function is synthetic for comparative reasoning, not a measured Android cost model.

## Trade-off
Exact search is suitable for offline tuning and small regression instances. Adaptive selection is suitable for quick runtime response when bounded complexity and low overhead matter.
