def bubble_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

if __name__ == "__main__":
    numbers = [5, 2, 9, 1, 5, 6]
    print("Original:", numbers)
    print("Sorted:", bubble_sort(numbers.copy()))

