# Q7 — Design a Mobile Emergency Communication Network

## Scenario
During a natural disaster, ambulances, police vehicles, rescue teams and medical personnel move continuously. Fixed communication infrastructure may be unavailable, but critical information must still reach nearby teams and the command centre.

## Independent proposals
A gateway-centred design uses mobile gateway vehicles, surviving cellular towers or satellite, and Mobile IP for continuity. A distributed design uses a multi-hop ad hoc mesh and reactive AODV routing, with buffering and route repair when links fail.

## Final hybrid design
Use a mobile ad hoc mesh as the resilient local network. Ambulances, police and rescue nodes communicate over Wi-Fi/ad hoc radios with approximately 250 m range. Mobile gateway vehicles connect the mesh to the command centre through surviving cellular or satellite links. A standby Home Agent improves reliability.

## Mobility management
Use AODV for movement inside the mesh; do not trigger Mobile IP for every local hop. Invoke Mobile IP only when a node changes gateway/foreign agent. The MN registers its CoA with the HA through the FA using authenticated messages (60 s lifetime, refreshed every 30 s). Downlink packets are tunnelled; uplink uses reverse tunnelling.

## Failure handling
- Node/link failure: detect missed hello/link-layer failure, send RERR, locally repair or rediscover with RREQ.
- Gateway/backhaul loss: attach to another gateway, re-register, or use satellite; standby HA takes over.
- Network partition: buffer critical messages by priority, retry when a route returns, and reposition relay vehicles. Local mesh traffic continues.

## Validation results from assignment
Registration overhead is approximately 11 B/s per node. A gateway handoff interruption is approximately 230 ms; local mesh route repair is approximately 100 ms. Handoff loss is approximately 0.9%; mesh delivery around 95% yields end-to-end delivery around 94%. In simulation, AODV achieved 99.9% delivery at 80 nodes compared with DSDV 81.3%, with overhead 3.83 vs 20.54 kB/s.

## Conclusion
The hybrid design combines AODV's resilience for local mobility with Mobile IP's session continuity across gateways. It should be avoided for strict sub-20 ms control, very large flat networks without clustering, dense high-flow conditions where AODV floods dominate, or deployments lacking any gateway for external access.

## Run
Run `python q7.py` to create the simplified validation dataset and chart.