
# Check if a string is a palindrome using recursion
def is_palindrome(s, left, right):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return is_palindrome(s, left + 1, right - 1)

print(is_palindrome("racecar", 0, len("racecar") - 1))
