"""
Description:

Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Example:
Input: s = "Was it a car or a cat I saw?"

Output: true
"""


def isPalindrome(s):
    # Make the string alphanumeric
    s = [c.lower() for c in s if c.isalnum()]
    l = 0
    r = len(s)-1
    while l<r:
        # Ignore non alphanumeric

        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

if __name__ == "__main__":
    s = input()
    result = isPalindrome(s)
    print(result)