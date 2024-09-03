"""
Description:

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example:

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]

"""

def threeSum(nums):
    result = []
    # Since the array is not sorted we would sort it so we can achieve a more efficient solution
    nums.sort() # This makes automatically our solution at least O(n log n)
    for i in range(len(nums)):
        # Since we want the target to be 0 if our leftmost element is positive then there is no way we can sum 0
        if nums[i] > 0:
            break
        # Since the triplet cannot have duplicates we skip repeated elements in the first position
        if i>0 and nums[i]==nums[i-1]:
            continue

        l = i+1
        r = len(nums)-1
        # In overall the solution will be O(n2) since we are using one loop for the pivot element and
        # one loop to the other two elements of the sum.
        while l<r:
            sum3 = nums[i] + nums[l] + nums[r]
            if sum3 < 0:
                l+=1
            elif sum3 > 0:
                r-=1
            else:
                result.append([nums[i], nums[l], nums[r]])
                l += 1
                #r -= 1
                # Avoid duplicates in second position
                while nums[l] == nums[l-1] and l<r:
                    l +=1

    return result


if __name__ == "__main__":
    nums = input()
    nums = nums.split()
    nums = list(map(int, nums))
    result = threeSum(nums)
    print(result)