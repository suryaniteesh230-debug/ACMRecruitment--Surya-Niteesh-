def rotate_binary(binary_str, k):
    """
    Rotate a binary string k steps to the left
    and return its decimal value.
    """
    k %= len(binary_str)
    rotated = binary_str[k:] + binary_str[:k]
    return int(rotated, 2)


if __name__ == "__main__":
    print(rotate_binary("1011", 1))  
    print(rotate_binary("1100", 2))  
    print(rotate_binary("1001", 3))  
