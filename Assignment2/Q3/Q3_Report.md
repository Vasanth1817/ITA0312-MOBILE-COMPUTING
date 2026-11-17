# Q3 — CDMA: Orthogonality, Spreading and the Near-Far Problem

## Problem context and model
A crowded stadium uplink uses DS-CDMA: multiple handsets share the same frequency band while spreading their data with unique Walsh orthogonal or pseudo-random noise (PN) codes. The assignment evaluates code lengths 8, 16 and 64.

## Principle
A data bit is multiplied by an N-chip code. Despreading with the intended code yields N times the desired bit. A second user's contribution is proportional to the cross-correlation of the two codes; it vanishes for perfectly aligned orthogonal codes. Walsh-Hadamard matrices are constructed recursively and provide N mutually orthogonal codes of length N.

## Predictions and results
Synchronous orthogonal codes are error-free up to the code limit. Random non-orthogonal codes experience multiple-access interference. A 10× stronger interferer creates the near-far problem. Table 4.1 reports:

| N | Processing gain | BER random codes | BER at 10× power imbalance |
|---:|---:|---:|---:|
| 8 | 9 dB | 3.2e-2 | 1.8e-1 |
| 16 | 12 dB | 1.1e-2 | 9.4e-2 |
| 64 | 18 dB | 4.1e-4 | 1.2e-2 |

Synchronous orthogonal BER is zero for all three code lengths. Processing gain is 10 log10(N). Increasing N from 8 to 64 reduces random-code BER by roughly two orders of magnitude.

## Discussion
Orthogonality breaks when users are not chip-synchronised because time offsets cause partial correlations. Large power differences can overwhelm weak users after despreading. Power control is therefore essential; spreading gain alone does not solve near-far interference.

## Run
`pip install -r Assignment2/Q3/requirements.txt` then `python Assignment2/Q3/q3.py`.
