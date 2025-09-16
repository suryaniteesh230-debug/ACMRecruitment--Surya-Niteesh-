# bubble_sort.py
# Bubble Sort implementation with comments

def bubble_sort(nums):
    n = len(nums)
    # Outer loop: repeat passes over the list
    for i in range(n - 1):
        # Inner loop: compare adjacent elements
        for j in range(n - i - 1):
            # If the current element is greater than the next, swap them
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    # Return the sorted list
    return nums


# Test the function
if __name__ == "__main__":
    numbers = [5, 2, 9, 1, 5, 6]              # Example list
    print("Original list:", numbers)          # Show original
    sorted_numbers = bubble_sort(numbers.copy())  # Sort a copy of the list
    print("Sorted list:  ", sorted_numbers)   # Show result


