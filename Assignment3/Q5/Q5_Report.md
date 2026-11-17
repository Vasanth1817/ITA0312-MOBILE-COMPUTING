# Q5 — Proactive Routing Protocols in Mobile Networks

## Aim
Study proactive (table-driven) routing and demonstrate DSDV route maintenance after a topology change.

## Principle
A proactive protocol maintains routes to all destinations before data is sent. DSDV uses destination-generated sequence numbers. A higher sequence number is fresher; for equal sequence numbers, the smaller hop count wins. Even sequence numbers represent valid routes; odd sequence numbers advertise broken routes with infinite metric.

## Example topology
Initially links are A–B, A–C, B–D, C–D and D–E. A reaches E through B in three hops with sequence 508. When D–E breaks, D advertises E as unreachable with odd sequence 509. E attaches to C and advertises sequence 510. C forwards the fresh route; A replaces the stale entry and reaches E via C in two hops. The higher sequence number rejects the older broken-route update and prevents a loop.

## Overhead calculation
With N nodes, 24-byte update header, 12-byte entries and a full table every 5 seconds, control rate = N(24+12N)/5 bytes/s. This gives 288 B/s at N=10, 3.936 kB/s at N=40 and 15.744 kB/s at N=80. Periodic updates give immediate route availability but can leave stale routes between updates.

## Advantages and limitations
Advantages: no route-discovery delay and simple forwarding. Limitations: continuous control traffic, table overhead growing with network size, and stale routes under rapid mobility. Triggered updates improve convergence but add messages.

## Run
Execute `python q5.py` to generate the overhead dataset and graph.