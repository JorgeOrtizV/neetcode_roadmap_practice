"""
Description:

Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first. 
"""

from collections import Counter

# Time complexity : O(n)

def two_integer_sum(nums, target):
    setNums = dict() # We store all seen numbers in {number : index} format
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in setNums.keys():
            return [setNums[diff], i]
        setNums[nums[i]] = i
    

if __name__ == "__main__":
    nums = input()
    nums = nums.split()
    nums = list(map(int, nums))
    target = int(input())
    result = two_integer_sum(nums, target)
    print(result)