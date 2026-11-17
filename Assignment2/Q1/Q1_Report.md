# Q1 — Mobile Communication vs. Mobile Computing: Field-Service Technology Audit

## Problem context
A utility company uses five setups: (a) a ruggedised tablet fetching work orders over cellular data; (b) a laptop connected to Ethernet at different offices; (c) a fixed wireless router at a remote substation; (d) a push-to-talk handset; and (e) a tablet app that records meter readings offline and synchronises later.

## Classification framework
Classify each setup using user mobility (stationary, nomadic or fully mobile), wireless-link usage, intermittent-connectivity tolerance, and application-level behaviour. Wireless communication alone does not make a system mobile computing; the application must also adapt to movement, disconnection or changing context.

## Engineering decision
- (a) Cache assigned work orders so field work can continue in dead zones.
- (b) Treat the office Ethernet laptop as ordinary networked computing; mobile-specific engineering adds little.
- (c) Treat the fixed substation router primarily as a link-budget problem: antenna gain, mounting height and signal margin.
- (d) Give push-to-talk users coverage planning and priority channel access because timely delivery matters more than buffering.
- (e) Use offline-first meter capture, local persistence, queued synchronisation, retry and conflict handling.

## Experiment
The document evaluates 1,000 updates under link availability of 90%, 60% and 30%. The Q1 reference result states that at 30% availability immediate sending delivers 300 updates, whereas store-and-forward delivers 910 with none lost in the reported run. The included script creates a reproducible illustrative availability comparison and labels its generated results separately from the report's reference observation.

## Result
A radio link is necessary but not sufficient. The application layer must buffer and synchronise updates when connectivity is intermittent. See `data/store_forward_results.csv` and `figures/delivery_comparison.png`.

## Run
`pip install -r Assignment2/Q1/requirements.txt` then `python Assignment2/Q1/q1.py` from the repository root.
