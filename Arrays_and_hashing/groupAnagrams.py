"""
Description:

Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
"""

from collections import defaultdict

def groupAnagrams(words):
    hashMap = defaultdict(list)
    for s in words:
        key = [0]*26
        for c in s:
            key[ord(c) - ord('a')] += 1
        hashMap[tuple(key)].append(s)
    return list(hashMap.values())

if __name__ == "__main__":
    words = input()
    words = words.split(",")
    result = groupAnagrams(words)
    print(result)