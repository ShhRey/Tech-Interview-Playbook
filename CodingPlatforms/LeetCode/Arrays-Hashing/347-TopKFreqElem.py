# Question: Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

from typing import Counter, List
import heapq

# HashMap-based Approach
# TC: O(Nlog(N))    SC: O(N)
def topKFrequentM(nums: List[int], k: int) -> List[int]:
    # Using Counter to create hmap
    """
    # Alternate Method
    freq = {}
    for n in nums:
        freq[n] = freq.get(n, 0) + 1
    """
    hmap = Counter(nums)
    # Desc sort using count, for highest occurrences
    smap = sorted(hmap.items(), key = lambda x:x[1], reverse = True)
    # Slice result for upto k-elements
    return [i[0] for i in smap[:k]]



# Bucket Sort based Approach
# TC: O(N)      SC: O(N)
def topKFrequentBS(nums: List[int], k: int) -> List[int]:
    freq = Counter(nums)
    # Creating empty buckets: Storing num, counts
    buck = [[] for _ in range(len(nums)+1)]
    for num, count in freq.items():
        buck[count].append(num)
    # Empty list for storing k-elements
    res = []
    # Iterating in rev-order for high freq
    for i in range(len(nums), 0, -1):
        for num in buck[i]:
            res.append(num)
            if len(res) == k:
                # Finish loop once k reached
                return res



# Heap-based Approach
# TC: O(Nlog(K))    SC: O(N)
def topKFrequentH(nums: List[int], k: int) -> List[int]:
    # Frequency map of nums
    hmap = Counter(nums)
    heap = []
    # Creating heap of count, num
    for num, count in hmap.items():
        # Push count, nums tuple in heap 
        heapq.heappush(heap, (count, num))
        # Pop Elements once k achieved
        if len(heap) > k:
            # Lowest occured will be removed
            heapq.heappop(heap)
    # Produce output as list-of-idx
    return [num for count, num in heap]





# Custom Test Cases
q = topKFrequentH([1,1,1,2,2,3], 2)
print(q)