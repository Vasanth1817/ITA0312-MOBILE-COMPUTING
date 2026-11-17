# Q7 — Day-4 Design Challenge: Diagnose, Redesign and Validate

## 1. Problem statement
Question 7 identifies user starvation in channel-aware best-subcarrier OFDMA. The greedy scheduler maximises aggregate throughput by assigning each subcarrier to the user with the highest instantaneous rate. Users with persistently weak channels can consequently receive almost no resources.

## 2. Diagnosis
- The greedy decision depends only on instantaneous channel rates and has no memory of past service.
- Users with weak average SNR are repeatedly bypassed.
- The root cause is the allocation objective: it lacks a proportional-fairness weight and historical-throughput tracking. The issue is not primarily computational complexity.

## 3. Design objectives
The assignment specifies three targets: minimum user throughput of at least **1.5 Mbps**, retain at least **85%** of greedy aggregate throughput, and Jain's fairness index greater than **0.88**.

## 4. Redesigned scheduling strategy
Use the proportional-fair metric M(i,k,t) = C(i,k,t) / T(i,t)^alpha, where C is instantaneous achievable rate, T is the user's moving-average throughput, and alpha controls the efficiency–fairness balance. Update the average as T(i,t+1) = (1 - 1/t_c)T(i,t) + (1/t_c)R(i,t). A temporary priority boost is applied when a user's average falls below the minimum-rate target. At alpha=0 the metric becomes greedy; alpha=1 is classical proportional fair; larger values emphasize underserved users.

## 5. Simulation setup
The independent verification script uses 8 users, 64 subcarriers across 20 MHz, 1,000 scheduling intervals, independent Rayleigh fading, mean user SNRs of 24, 21, 18, 15, 12, 9, 6 and 3 dB, and a fixed random seed. It sweeps alpha in {0, 0.25, 0.5, 1, 1.5, 2}. The script writes measured values to data/alpha_sweep.csv and per-user rates at alpha 1 to data/alpha1_per_user_rates.csv.

## 6. Reference result reported in the assignment
The main validation table in the DOCX reports greedy OFDMA at 89.4 Mbps sum throughput, 0.2 Mbps minimum-user throughput and 0.64 Jain fairness. The redesigned scheduler reports 78.1 Mbps, 1.52 Mbps and 0.91 respectively. This is a 12.6% throughput reduction; retained throughput is 78.1/89.4 = 87.4%, exceeding the 85% target. The minimum-user rate and fairness targets are also met.

The supplementary wide-SNR verification reports a smooth alpha trade-off: alpha 0 gives 156.9 Mbps and fairness 0.27; alpha 1 gives 118.8 Mbps and fairness 0.87; alpha 2 gives 109.0 Mbps and fairness 0.95. In that harsher SNR spread, no single alpha meets both the 85% retention and 0.88 fairness targets. This limitation should be discussed rather than hidden.

## 7. Result and conclusion
The redesign reduces starvation by including historical service in the scheduling metric. The reference design meets all three stated objectives with 78.1 Mbps aggregate throughput, 1.52 Mbps minimum-user throughput and 0.91 Jain fairness. The fairness exponent is the main tuning parameter: increasing it improves fairness but generally reduces total throughput. The selected value should reflect service guarantees and observed user-channel distribution.

## 8. How to run
From the repository root:

```bash
pip install -r Assignment2/Q7/requirements.txt
python Assignment2/Q7/q7.py
```

The program generates CSV data and PNG/SVG plots in the data/ and figures/ directories. Its independent simulation values are not expected to exactly reproduce the assignment's reported tables because the DOCX describes more than one experiment and channel setup.
