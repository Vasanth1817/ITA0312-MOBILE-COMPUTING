# Q2 — Sharing the Channel: FDMA vs. TDMA Under Different Traffic

## Problem context
A cellular cell has a 2 MHz band per direction. FDMA uses 25 kHz channels with 1 kHz guard bands. TDMA uses 200 kHz carriers, each with 8 slots and 12% frame overhead. Both begin with 80 nominal channels.

## Capacity calculation
FDMA: floor(2000/(25+1)) = 76 usable channels. TDMA: 10 carriers × 8 slots × (1−0.12) = 70.4, rounded down to 70 equivalent channels. FDMA therefore has a six-channel (8.6%) advantage for usable voice circuits, but needs 76 radio transceivers versus 10 for TDMA.

## Traffic experiment
The report compares continuous voice, bursty data (10% duty cycle), a 70/30 voice-data mix and synchronized bursts. The transcribed Table 3.1 values are in `data/fdma_tdma_results.csv`.

## Result and discussion
For bursty data, FDMA utilisation is 14.2% while TDMA reaches 78.4%, because dedicated FDMA channels remain idle while TDMA shares carrier slots. For continuous voice FDMA slightly leads (88.5% vs 85.0%). The result depends on traffic shape: dedicated channels suit steady voice, while shared time slots suit bursty sources. TDMA's trade-off is timing and frame overhead.

## Run
`pip install -r Assignment2/Q2/requirements.txt` then `python Assignment2/Q2/q2.py`.
