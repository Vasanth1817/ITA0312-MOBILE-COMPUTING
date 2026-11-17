# Q6 — Reactive Routing and DSDV–AODV Comparison

## Aim
Explain reactive routing using AODV and compare it with proactive DSDV under changing mobility.

## AODV operation
AODV creates routes only when needed. The source floods a Route Request (RREQ); nodes record reverse routes and discard duplicate requests. The destination (or a node with a sufficiently fresh route) returns a Route Reply (RREP) along the reverse path. When an active link breaks, a Route Error (RERR) invalidates the route and the source can rediscover it. Sequence numbers help maintain loop-free routes.

## Comparison
| Aspect | DSDV | AODV |
|---|---|---|
| Discovery | Periodic/triggered table updates | RREQ flood and RREP on demand |
| State | Route to every node | Active destinations and reverse routes |
| Overhead | O(N²), independent of traffic | Depends on traffic and mobility |
| First packet | No discovery delay | Discovery delay |
| Mobility | Can use stale routes until update | RERR and rediscovery |
| Best fit | Small, low-mobility, continuous traffic | Dynamic networks with intermittent traffic |

## Simulation results from assignment
For 30 nodes and 8 flows, AODV delivery remains around 94–96% from 5–30 m/s, while DSDV falls from 87.1% at 5 m/s to 59.6% at 30 m/s. At 30 m/s, DSDV overhead is 4.26 kB/s and AODV is 2.84 kB/s. AODV has greater mean delay (43.4 ms vs 25.2 ms) because of route discovery, but delivers more packets. At 20 simultaneous flows, AODV overhead can exceed DSDV due to repeated floods.

## Decision
Choose AODV for high mobility and intermittent traffic; choose DSDV for small, mostly static networks with continuous traffic and strict first-packet delay requirements.

## Run
Run `python q6.py` to export the assignment comparison dataset and chart.