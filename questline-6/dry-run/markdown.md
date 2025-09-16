**Dry Run:Pseudocode Execution
**Pseudocode**
A = 5
B = 3
SUM = 0

print("Initial: A =", A, ", B =", B, ", SUM =", SUM)

for i in range(1, B + 1):
print(f"\nStep {i}:")
print("Before: SUM =", SUM)
SUM = SUM + A
print(f"Operation: SUM = SUM + A → {SUM}")

print("\nFinal Output:", SUM)

## Step-by-Step Execution (Trace Table)

| Iteration (i) | Before SUM | Operation Performed | After SUM |
|---------------|------------|---------------------|-----------|
| Initial       | -          | A=5, B=3, SUM=0     | 0         |
| Step 1        | 0          | SUM = 0 + 5         | 5         |
| Step 2        | 5          | SUM = 5 + 5         | 10        |
| Step 3        | 10         | SUM = 10 + 5        | 15        |

## Final Output (Predicted)

Initial: A = 5 , B = 3 , SUM = 0

Step 1:
Before: SUM = 0
Operation: SUM = SUM + A → 5

Step 2:
Before: SUM = 5
Operation: SUM = SUM + A → 10

Step 3:
Before: SUM = 10
Operation: SUM = SUM + A → 15

Final Output: 15

