# River riddle — step-by-step solution

**Goal:** Move Wolf (W), Goat (G) and Cabbage (C) from **Left bank** to **Right bank**. Boat holds the Farmer (F) and **one** item.  
**Forbidden pairs (when Farmer is absent):** W + G (wolf eats goat), G + C (goat eats cabbage).

**Initial state:**  
Left: F, W, G, C — Right: (empty)

**Safe sequence of crossings (7 moves):**

1. **F takes G → Right.**  
   Left: W, C — Right: F, G  

2. **F returns ← alone.**  
   Left: F, W, C — Right: G  

3. **F takes W → Right.**  
   Left: C — Right: F, W, G  

4. **F brings G ← back to Left.**  
   Left: F, G, C — Right: W  

5. **F takes C → Right.**  
   Left: G — Right: F, W, C  

6. **F returns ← alone.**  
   Left: F, G — Right: W, C  

7. **F takes G → Right.**  
   Left: (empty) — Right: F, W, G, C — **All across safely.**
