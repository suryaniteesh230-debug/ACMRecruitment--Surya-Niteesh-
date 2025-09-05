def longest_palindrome(s: str) -> str:
    if not s:
        return ""

    start, end = 0, 0

    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    for i in range(len(s)):
        # Odd-length palindrome
        l1, r1 = expand(i, i)
        # Even-length palindrome
        l2, r2 = expand(i, i + 1)

        if r1 - l1 > end - start:
            start, end = l1, r1
        if r2 - l2 > end - start:
            start, end = l2, r2

    return s[start:end + 1]


# Usage examples
if __name__ == "__main__":
    print(longest_palindrome("babad"))             # "bab" or "aba"
    print(longest_palindrome("cbbd"))              # "bb"
    print(longest_palindrome("a"))                 # "a"
    print(longest_palindrome("forgeeksskeegfor"))  # "geeksskeeg"
