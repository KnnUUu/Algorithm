def findKthLargest(nums, k):
    return sorted(nums,reverse=True)[k-1]
# Nlg(N)

import heapq
def findKthLargest(nums, k):
    heapq._heapify_max(nums) # n
    for i in range(k-1): heapq._heappop_max(nums) # k*lg(n)
    return heapq._heappop_max(nums)
# N + k*lg(N)

def findKthLargest(nums, k):
    heap = nums[:k]
    heapq.heapify(heap)
    for i in range(k,len(nums)): heapq.heappushpop(heap,nums[i])
    return heap[0]
# k + N*lg(k)

print(findKthLargest([3,2,1,5,6,4],k = 2))

print(findKthLargest([3,2,3,1,2,4,5,5,6],k = 4))