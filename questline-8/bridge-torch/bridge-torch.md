# Bridge & Torch — Optimal Crossing (1, 2, 7, 10 minutes)
People speeds (minutes):(1, 2, 7, 10) 
Constraints:Bridge holds ≤ 2 people; torch required; when two cross together they move at the slower person's time; someone must bring the torch back if people remain.

## Optimal sequence (total = **17 minutes**)

1.1 and 2 cross→ takes 2 minutes.  
 - Left: 7, 10. Right: 1, 2. Elapsed = 2.

2. 1 returns → takes 1 minute.  
  - Left: 1, 7, 10. Right: 2. Elapsed =3.

3. 7 and 10 cross together→ takes 10 minutes.  
   - Left: 1. Right: 2, 7, 10. Elapsed =13.

4. 2 returns → takes 2 minutes.  
   - Left: 1, 2. Right: 7, 10. Elapsed = 15.

5. 1 and 2 cross → takes 2 minutes.  
   - Left: —. Right: 1, 2, 7, 10. Elapsed =17.

Total time = 17 minutes.

## Reasoning / proof of optimality (short)

There are two common classes of strategies for 4 people:

**Strategy A — send the two fastest first:**  
(1) fastest two cross, fastest returns, two slowest cross together, second-fastest returns, fastest two cross again.  
Total time for this pattern = 3·t₂ + t₁ + t₄(where t₁ ≤ t₂ ≤ t₃ ≤ t₄).  
For our numbers: `3·2 + 1 + 10 = 17`.

**Strategy B — fastest escorts each slow person individually:**  
(fastest shuttles each slow person across one by one)  
Total time for this pattern = 2·t₁ + t₂ + t₃ + t₄.  
For our numbers: `2·1 + 2 + 7 + 10 = 21`.

Compare the two: Strategy A gives 17, Strategy B gives 21. There are no better patterns because any optimal plan must either (a) send the two slowest together at some point (so Strategy A type helps), or (b) send slowest separately (Strategy B type). Checking both classes shows 17 is the minimum achievable.

Hence the sequence above (Strategy A) is more beneficial to use
