# Pattern Hunt — Sequence

**Given sequence:**  
2, 6, 12, 20, ...

Next two terms:  
30, 42

::Explanation of pattern::
The differences between consecutive terms are 4, 6, 8, ... (increasing by 2 each step).  
So the next differences are 10 and 12, giving the terms 30 and 42.

Another way to see it: each term is given by the formula [ n × (n+1)], i.e., the product of consecutive integers:
- 1×2 = 2  
- 2×3 = 6  
- 3×4 = 12  
- 4×5 = 20  
- 5×6 = 30  
- 6×7 = 42

