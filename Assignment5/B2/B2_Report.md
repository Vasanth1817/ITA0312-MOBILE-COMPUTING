# B2 — Adversarial Workload Investigation

## Aim
Compare equal-sized workloads under favorable and adversarial resource conditions.

## Experiment
Both cases start with five records. Benign conditions use strong battery and Wi-Fi. Adversarial conditions combine weak battery and unavailable/metered connectivity. The policy safely defers rather than repeatedly wasting radio work.

## Results
|Case|Records|Battery|Network|Deferred|Successful|Backlog|
|---|---:|---:|---|---:|---:|---:|
|Benign|5|85%|Wi-Fi|0|5|0|
|Adversarial|5|12%|Offline/metered|8|0|5|

Run `python b2.py` for CSV output. This is a reproducible model, not a handset benchmark.
