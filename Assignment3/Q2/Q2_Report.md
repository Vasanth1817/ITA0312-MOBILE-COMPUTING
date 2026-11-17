# Q2 — Mobile IP and Mobility Management

## Aim
Explain how Mobile IP maintains communication when a mobile node changes its network of attachment.

## Architecture and entities
- Mobile Node (MN): moves but retains its permanent home address.
- Home Agent (HA): stores the binding Home Address → Care-of Address (CoA), intercepts packets and tunnels them.
- Foreign Agent (FA): advertises the visited network, supplies/relays the CoA registration and decapsulates packets.
- Correspondent Node (CN): communicates with the MN using its home address.

## Operation
1. The MN discovers an agent through advertisements (or sends a solicitation).
2. It obtains a CoA and sends a registration request through the FA to the HA.
3. The HA authenticates the request and updates its binding table.
4. Packets addressed to the home address are intercepted and encapsulated (IP-in-IP) to the CoA.
5. The FA removes the outer header and delivers the original packet to the MN.

## Worked example
MN home address 10.1.1.5; HA 10.1.1.1; CoA/FA 130.5.2.1; CN 203.0.113.9. The CN sends to 10.1.1.5. The HA tunnels with outer header 10.1.1.1 → 130.5.2.1 while the inner packet remains 203.0.113.9 → 10.1.1.5.

## Performance calculations
Registration RTT = 12 + 30 + 5 + 30 + 12 = 89 ms. A 20-byte IP-in-IP header adds 2% to a 1000-byte payload and 10% to a 200-byte payload. Triangular route delay in the example is 82 ms versus 40 ms for a direct route. A 160 ms loss window at 50 packets/s can affect 8 packets per handoff.

## Challenges and improvements
Use pre-registration and buffering/forwarding for handoff loss; regional registration for signalling; route optimisation to reduce triangular routing; short binding lifetimes and hysteresis to avoid stale bindings and ping-pong; authentication and replay protection for security.

## Run
Install requirements, then run `python q2.py` to generate the calculation dataset and chart.