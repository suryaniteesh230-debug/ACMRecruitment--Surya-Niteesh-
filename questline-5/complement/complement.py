# complement.py
num = -42
bits = 8
if num < 0:
    val = (1 << bits) + num
else:
    val = num

binary = format(val, '08b')
print("Number:", num)
print(f"{bits}-bit 2's complement =", binary)
