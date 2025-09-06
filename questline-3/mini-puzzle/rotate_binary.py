# File: rotate_binary.py

def rotate_binary(binary, k, direction="left"):
    """
    Rotate a binary string k steps (left or right)
    and return its decimal value.

    Parameters:
        binary (str): A string of '0' and '1', e.g. "1011"
        k (int): Number of steps to rotate
        direction (str): "left" or "right" (default is "left")

    Returns:
        int: Decimal value of the rotated binary string
    """

    n = len(binary)           # length of binary string
    k = k % n                 # keep k within range

    # Rotate according to direction
    if direction == "left":
        rotated = binary[k:] + binary[:k]
    elif direction == "right":
        rotated = binary[-k:] + binary[:-k]
    else:
        raise ValueError("Direction must be 'left' or 'right'")

    # Convert rotated binary string into decimal number
    return int(rotated, 2)


# -------------------- Examples --------------------
if __name__ == "__main__":
    binary_str = "1011"
    print("Original binary:", binary_str)

    # Left rotations
    print("Left rotate by 1:", rotate_binary(binary_str, 1, "left"))
    print("Left rotate by 2:", rotate_binary(binary_str, 2, "left"))
    print("Left rotate by 3:", rotate_binary(binary_str, 3, "left"))

    # Right rotations
    print("Right rotate by 1:", rotate_binary(binary_str, 1, "right"))
    print("Right rotate by 2:", rotate_binary(binary_str, 2, "right"))
    print("Right rotate by 3:", rotate_binary(binary_str, 3, "right"))

