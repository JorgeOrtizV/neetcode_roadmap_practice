"""
Description:
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
"""

# Complexity : O(n)

def is_anagram(s, t):
    if len(s) != len(t):
        return False
    
    s_dict = dict()
    t_dict = dict()

    for i in range(len(s)):
        s_dict[s[i]] = 1 + s_dict.get(s[i], 0)
        t_dict[t[i]] = 1 + t_dict.get(t[i], 0)

    return s_dict == t_dict

if __name__ == "__main__":
    s = input()
    t = input()
    result = is_anagram(s, t)
    print(result)