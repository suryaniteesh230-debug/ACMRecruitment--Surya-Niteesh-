# xor_riddle.py

# Given: N XOR 23 = 45
# Using XOR property: N = 45 XOR 23

N = 45 ^ 23   # ^ is XOR in Python

print("Secret number (N):", N)

# Verification step
print("Verification (N XOR 23 == 45):", N ^ 23 == 45)
