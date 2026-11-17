# Q4 — Applications of Mobile IP and Routing Requirements

## Aim
Evaluate Mobile IP in a real application and identify the routing requirements created by mobility.

## Applications
Mobile employees roaming between Wi-Fi and cellular, trains and buses, emergency response, mobile healthcare, intelligent transportation, fleet monitoring, field maintenance and temporary networks can benefit from mobility support.

## Selected scenario: mobile healthcare
An ambulance transmits patient ECG, SpO₂ and blood-pressure telemetry to a hospital while moving between networks. Patient sensors connect to an ambulance mobile router over an in-vehicle WLAN. Roadside access points/cell towers act as foreign agents; the hospital gateway hosts the Home Agent; the doctor's console is the Correspondent Node.

## Communication flow
Sensors → ambulance router → current FA → Internet → doctor (uplink/reverse tunnel). Downlink instructions travel doctor → HA → tunnel → FA → ambulance. The hospital continues using the ambulance's home address after the CoA changes.

## Design targets and model checks
- Voice/video one-way delay target: ≤150 ms. Example HA path: 40+30+12 = 82 ms; route-optimised path ≈40 ms.
- ECG delivery target: ≥99%. With 20 ms ECG frames and a 160 ms handoff window, 8 frames may be affected per handoff; buffering reduces loss.
- Continuous connectivity up to 30 m/s requires overlapping coverage and timely agent advertisements.
- Security requires authenticated registration and end-to-end IPsec/VPN protection for patient data.
- Reliability requires a standby HA and dual-network connectivity.

## Conclusion
Mobile IP is suitable because it hides address changes from applications. Its HA detour and handoff interruption should be reduced with route optimisation, pre-registration, buffering, authentication and HA redundancy. Routing must detect link loss quickly, avoid loops/stale routes and provide alternate paths.

## Run
Run `python q4.py` after installing the listed requirements.