# B4 — Multimedia Framework Decision

## Aim
Design a device-aware multimedia encoding strategy balancing quality, upload time, battery and CPU capacity.

## Strategy
Choose 360p when battery is low or network is slow; 720p on intermediate devices; 1080p when device and network conditions are favorable. The simulated bitrate values are 500, 1800 and 3500 kbps respectively. Estimate transfer time for a 10 MB clip and use a simple energy proxy for comparison.

## Procedure
1. Run `python b4.py`.
2. Inspect `data/results.csv`.
3. Discuss how the heuristic prioritizes reliable transfer and battery conservation over maximum quality.

## Limitations and production decision
These are illustrative estimates, not codec measurements. Exact search is useful for offline tuning/device certification; adaptive policy is useful for runtime decisions. Production should measure upload latency, energy, encode success, thermal throttling, dropped frames, retries and user-visible quality, and provide fallback settings.
