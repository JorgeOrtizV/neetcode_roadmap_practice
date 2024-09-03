"""
Description:

Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.
"""

from collections import Counter

# Complexity : O(n log n)

def topKFrequent(nums, k):
    freqMap = Counter(nums)
    # sortedFreq = sorted(freqMap.items(), key=lambda x : x[1], reverse=True)
    # result = []
    # for i in range(k):
    #     result.append(sortedFreq[i][0])

    # We can achieve O(n) complexity by using bucket sort
    freqs = [[] for i in range(len(nums)+1)]
    for num, freq in freqMap.items():
        freqs[freq].append(num)

    result = []
    for i in range(len(freqs)-1, 0, -1):
        if k==0:
            break
        if len(freqs[i]) > 0:
            result.extend(freqs[i])
            k -= len(freqs[i])

    return result


        

if __name__ == '__main__':
    nums = input()
    nums = nums.split()
    nums = list(map(int, nums))

    k = int(input())

    result = topKFrequent(nums, k)

    print(result)
