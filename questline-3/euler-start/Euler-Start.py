# Problem 1: sum of multiples of 3 or 5 below 1000
def multiple_sum():
    sum = 0
    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

print(f"The sum of all multiples of 3 or 5 below 1000 is {multiple_sum()}")
# Problem 2: sum of even-valued Fibonacci numbers below 4,000,000:
def fibonacci():
    n1, n2 = 0, 1
    sum = 0
    while n1 <= 4000000:
        if n1 % 2 == 0:
            sum += n1
        n1, n2 = n2, n1 + n2
    return sum

print(f"The sum of even Fibonacci numbers below 4,000,000 is {fibonacci()}")

