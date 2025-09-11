# 4×4 Sudoku — Logical solving steps

Given grid:
R1: - - 3 -
R2: - 3 - 1
R3: 3 - - -
R4: - 1 - -

Two valid completions exist; both satisfy rows, columns and 2×2 boxes.

## Steps

1. Box1 (rows1–2, cols1–2):must contain {1,2,4}.  
   Column2 already has 1 at R4C2, so R1C2 cannot be 1.  
   Therefore R1C1 = **1**.

2. Box4 (rows3–4, cols3–4): must contain the missing 1.  
   Column4 already has a 1 at R2C4, so it must be R3C3 = 1.

3. Column4 needs a 3. Since rows1–3 already hold 3s elsewhere, the 3 goes to R4C4 = 3.

4. The remaining empty cells reduce to pairs {2,4}.  
   There are two consistent ways to fill them, producing two solutions.

## Final solutions

**Solution A**
1 2 3 4  
4 3 2 1  
3 4 1 2  
2 1 4 3  

**Solution B**
1 4 3 2  
2 3 4 1  
3 2 1 4  
4 1 2 3  

