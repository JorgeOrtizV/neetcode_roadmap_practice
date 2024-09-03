"""
Description:
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n)O(n) time without using the division operation?
"""

def productExceptSelf(nums):
    zero_count = 0
    total = 1
    no_zero_total = 1
    for num in nums:
        total *= num
        if num != 0:
            no_zero_total *= num
        else:
            zero_count += 1
    result = []
    for i in range(len(nums)):
        if nums[i] == 0 and zero_count == 1:
            result.append(no_zero_total)
        elif zero_count > 1:
            result.append(0)
        else:
            result.append(total//nums[i])
    return result

def productExceptSelf_noDiv(nums):
    result = [1]*len(nums)
    # Calculate prefix
    for i in range(len(nums)-1):
        result[i+1] = result[i]*nums[i]
    # Calculate postfix and result
    postfix = 1
    for i in range(len(nums)-1, -1, -1): # Down to -1 so idx 0 is included
        result[i] *= postfix
        postfix *= nums[i]  
    return result

if __name__ == "__main__":
    nums = input()
    nums = nums.split()
    nums = list(map(int, nums))

    result = productExceptSelf_noDiv(nums)
    print(result)