"""
Description:
Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use O(1)O(1) additional space.

"""

def twoSum(numbers, target):
    l = 0
    r = len(numbers)-1

    while l < r:
        if numbers[l]+numbers[r] == target:
            return [l+1, r+1]
        # Case 1 : right number greater than target
        if numbers[r] >= target or numbers[r] + numbers[l] > target:
            r-=1
        if numbers[l] + numbers[r] < target:
            l += 1
    


if __name__ == "__main__":
    numbers = input()
    numbers = numbers.split()
    numbers = list(map(int, numbers))
    target = int(input())
    result = twoSum(numbers, target)
    print(result)