# Q5 — SDMA: Reusing the Same Channel in Different Directions

## Problem context
Vehicles along a highway share frequency and time slots using SDMA with an N-element uniform linear array (ULA). The array factor is AF(θ) = Σ exp(j n (k d cos θ + β)). Here k=2π/λ, d is element spacing, θ is angle from the array axis, and β steers the beam. Choosing β=−kd cos θ₀ points the main beam toward θ₀. Half-wavelength spacing (d=λ/2) avoids grating lobes for this design.

## Measured array patterns
| N | HPBW | Side-lobe level | Minimum separation for SIR ≥20 dB |
|---:|---:|---:|---:|
| 2 | 78.0° | −4.2 dB | 45° |
| 4 | 38.5° | −11.5 dB | 22° |
| 8 | 18.2° | −13.3 dB | 10° |
| 16 | 9.0° | −13.5 dB | 5° |

## Discussion
Doubling the array size roughly halves beamwidth and required angular separation. Side-lobe suppression improves strongly from N=2 to N=4, then approaches approximately −13.5 dB. Larger arrays narrow beams but cannot separate users that are too close in angle; user geometry remains a limiting factor. The assignment recommends combining SDMA with another resource dimension when users are angularly clustered.

## Run
`pip install -r Assignment2/Q5/requirements.txt` then `python Assignment2/Q5/q5.py`.
