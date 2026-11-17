# Q4 — OFDMA: Giving Each User the Subcarriers They Can Use Best

## Experiment setup
The assignment's Appendix A specifies 8 users, 64 subcarriers and 1,000 realisations. OFDMA divides the channel into orthogonal subcarriers and schedules users on time-frequency resources. The cyclic-prefix example uses 64 symbol samples, a 16-sample prefix and a 20 MHz sample rate.

## Comparison and evidence
The report's synthesis states that sum throughput spans 34.2 to 89.4 Mbps across the tested schemes, while Jain's fairness falls from 0.98 to 0.64. The full scheme-by-scheme table is not reproduced in the available summary, so the CSV marks the endpoints as report-supported and the middle proportional-fair point as illustrative rather than presenting it as a source result.

## Discussion
Channel-aware best-subcarrier assignment exploits multi-user diversity and raises aggregate throughput, but it can repeatedly bypass users whose channels are weak across the band. Round-robin allocation tends to distribute resources more evenly but may not exploit favourable channel conditions. A proportional-fair objective balances instantaneous rate against historical average throughput. This fairness issue motivates Q7.

## Run
`pip install -r Assignment2/Q4/requirements.txt` then `python Assignment2/Q4/q4.py`.
