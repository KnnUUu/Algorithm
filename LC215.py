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

def findKthLargest(nums, k):

    def part(nums, l, r, k):
        val = nums[k]
        nums[k],nums[l] = nums[l],nums[k]
        mark = l+1
        for i in range(l+1,r+1): # lg(N)
            if nums[i]>val:
                nums[i],nums[mark]=nums[mark],nums[i]
                mark+=1
        nums[l],nums[mark-1]=nums[mark-1],nums[l]

        if mark-1 > k:
            return part(nums,l,mark-2,k)
        elif mark-1 < k:
            return part(nums,mark,r,k)
        else:
            return nums[k]

    return part(nums,0,len(nums)-1,k-1)

print(findKthLargest([3,2,1,5,6,4],k = 2))

print(findKthLargest([3,2,3,1,2,4,5,5,6],k = 4))