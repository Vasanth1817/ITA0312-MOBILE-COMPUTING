# Q6 — Choosing Multiple-Access Techniques for Real Deployments

## Objective
Select an appropriate access technique for a stated deployment by comparing FDMA, TDMA, CDMA, OFDMA and SDMA. The assignment uses five criteria with weights 25%, 20%, 20%, 20% and 15% (Appendix A).

## Decision method
Use a weighted decision matrix: total score = Σ(scoreᵢ × weightᵢ)/100. The accompanying script provides transparent illustrative 1–5 ratings for capacity, spectral efficiency, fairness, complexity and cost, then evaluates baseline, spectrum-heavy and cost-dominant weight profiles. These qualitative ratings are modelling assumptions in this implementation, not measured scores transcribed from the DOCX.

## Source-supported conclusion
The report's cross-technique synthesis says OFDMA ranks first under baseline and spectrum-heavy weights, while FDMA ranks first when cost dominates. Sensitivity analysis is important because a recommendation can change when deployment priorities change.

## Engineering interpretation
OFDMA is suitable when high capacity and spectral efficiency are priorities; FDMA can remain attractive when simplicity and cost dominate. CDMA offers processing gain but requires power control. TDMA shares carriers efficiently for bursty traffic. SDMA reuses spectrum spatially but depends on angular separation and array complexity. The final choice should follow the actual deployment requirements rather than a universal ranking.

## Run
`pip install -r Assignment2/Q6/requirements.txt` then `python Assignment2/Q6/q6.py`.
