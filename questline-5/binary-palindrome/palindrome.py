# palindrome.py
numbers = [9, 10]
for n in numbers:
    binary = bin(n)[2:]   # get binary without 0b
    rev = binary[::-1]    # reverse string
    if binary == rev:
        print(n, "in binary is", binary, "-> Palindrome")
    else:
        print(n, "in binary is", binary, "-> Not Palindrome")
