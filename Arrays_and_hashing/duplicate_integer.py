"""
Description:
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false

"""

# Complexity : O(1)

def duplicate(nums):
    nums_set = set(nums)
    if(len(nums_set) == len(nums)):
        return False
    return True

if __name__ == "__main__":
    nums = input()
    nums = nums.split()
    nums = list(map(int, nums))
    result = duplicate(nums)
    print(result)