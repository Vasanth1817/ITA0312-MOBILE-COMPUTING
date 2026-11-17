# Q3 — Cellular Networks versus Ad Hoc Wireless Networks

## Aim
Compare infrastructure-based cellular networks with infrastructure-less ad hoc wireless networks and select an architecture for disaster response.

## Cellular network
The service area is divided into cells. Each cell is served by a base station connected to a controller/core network. Mobile nodes communicate through the base station. The network manages authentication, channel allocation, location tracking, handoff and routing. It provides planned coverage and scales through cell splitting and frequency reuse, but a base-station or backhaul failure can remove service from a whole cell.

## Ad hoc network
Nodes communicate directly when in range and relay packets for distant nodes over multiple hops. Every node acts as both host and router. There is no fixed controller; routes change as nodes move. The design is resilient to infrastructure loss but multi-hop forwarding consumes bandwidth and battery and adds delay.

## Comparison
| Parameter | Cellular | Ad hoc |
|---|---|---|
| Infrastructure | Required BS and core | Not required |
| Communication | Centralised, usually one radio hop to BS | Peer-to-peer, often multi-hop |
| Mobility | Network-controlled handoff | Route discovery/repair |
| Failure | BS/backhaul can be a single point of failure | Alternate peer routes possible |
| Applications | Public voice and broadband | Disaster relief, military, sensors, temporary events |

## Design decision
When fixed infrastructure is unavailable and immediate deployment is required, choose an ad hoc multi-hop mesh. Add an optional gateway to surviving cellular or satellite service when external connectivity is available. Accept lower per-node throughput and higher relay energy use in exchange for resilience.

## Run
Install requirements and execute `python q3.py` to create the comparison dataset and visual chart.