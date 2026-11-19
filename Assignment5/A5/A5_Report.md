# A5 — UI Performance Approximation
Exact search enumerates quality q, cache c, prefetch p and device profiles; evaluates cost 100×frame drops + energy + memory penalty subject to frame time ≤16 ms. Complexity O(DN|Q||C||P|).

Pseudocode: enumerate combinations; evaluate; retain lowest feasible cost.

Adaptive controller: measure p95 frame time, drops, battery, memory and bandwidth each window. If infeasible or battery <20%, lower quality, evict oldest, reduce prefetch. If frame <10ms, battery >60% and memory headroom, raise one quality step/grow cache/increase prefetch; otherwise hold.

Heuristic is reactive/myopic, can oscillate and does not guarantee global energy optimum; exact is useful offline as oracle for small instances.
