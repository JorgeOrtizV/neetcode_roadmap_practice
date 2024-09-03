"""
Description:

Given an array of integers nums, return the length of the longest consecutive sequence of elements.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.

You must write an algorithm that runs in O(n) time.

Example:

Input: nums = [2,20,4,10,3,4,5]

Output: 4


Input: nums = [0,3,2,5,4,6,1,1]

Output: 7
"""


def longestConsecutive(nums):
    numsSet = set(nums)
    # empty array
    if len(nums) == 0:
        return 0

    maxSeq = 1
    for i in nums:
        seq = 1
        # Find the starting num of the sequence (smallest)
        while i+1 in numsSet and i-1 not in numsSet:
            seq += 1
            if seq > maxSeq:
                maxSeq = seq
            # Remove i and update pivot to next element
            numsSet.discard(i)
            i += 1
    return maxSeq


if __name__ == "__main__":
    nums = input()
    nums = nums.split()
    nums = list(map(int, nums))
    result = longestConsecutive(nums)
    print(result)