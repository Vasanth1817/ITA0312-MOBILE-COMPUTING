# Q1 — Wireless Network Architecture and Mobility Analysis

## Aim
Study the components of a wireless network and analyse how user mobility affects handoff, delay and packet loss.

## Architecture
A mobile node (MN) communicates over a radio link with an access point/base station (AP/BS). The AP forwards traffic through wired backhaul to a gateway/core router and then to the correspondent server. The reverse path carries replies. The AP is the attachment point; changing AP requires handoff.

## Main constraints
- Bandwidth is shared among active users; the model uses 20 Mbit/s effective AP throughput.
- Wireless links experience fading, interference, obstacles and variable error rates.
- Coverage is finite; a moving node may leave one cell before attaching to another.
- Mobile devices have limited battery and processing resources.

## User-load calculation
Per-user throughput = 20/N Mbit/s. For 1, 5, 10 and 20 active users the rates are 20, 4, 2 and 1 Mbit/s. A 1500-byte packet therefore takes approximately 0.6, 3, 6 and 12 ms to transmit, excluding protocol overhead.

## Mobility scenario
A user moves from AP1 to AP2 at 10 m/s. AP spacing is 200 m and handoff begins at 100 m. At t=10.0 s, a 200 ms interruption occurs; packets 100 and 101 are lost. Service resumes at t=10.2 s. The model records 198 of 200 packets delivered (99%) and a largest gap of 200 ms.

## Handoff logic
Measure current AP signal; scan when it falls below the scan threshold; switch only if a candidate exceeds the current signal by a hysteresis margin (e.g. 5 dB). Hysteresis prevents ping-pong between neighbouring APs.

## Result
Mobility introduces short interruption windows. Faster movement increases handoff frequency and cumulative loss. Overlapping coverage, hysteresis, buffering and fast reassociation reduce the impact.

## Run
Install dependencies with `pip install -r requirements.txt`, then run `python q1.py`. The script creates a CSV and PNG/SVG chart in the data/ and figures/ folders.