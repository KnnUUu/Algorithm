"""


def partition(nums,left,right,pivot):
    pivotValue = nums[pivot]
    nums[right],nums[pivot] = nums[pivot],nums[right]
    j = left
    for i in range(left,right-1):
        if nums[i]<pivotValue:
            nums[i],nums[j] = nums[j],nums[i]
            j+=1
    nums[right], nums[j] = nums[j], nums[right]
    return j

def quickSelect(nums,left,right,k):
    pivot = partition(nums,left,right,(left+right)//2)
    if k == pivot:
        return nums[k]
    elif k < pivot:
        return quickSelect(nums,left,pivot-1,k)
    else:
        return quickSelect(nums,pivot+1,right,k)
"""

def quickSelect(nums,k):
    """
    return (k+1)th smallest element in nums
    result is same as sorted(nums)[k]

    average O(N)
    worse case O(N^2): pivot get the largest/smallest value every time
    """
    def part(l, r, k):
        if l==r:
            if l==k: return nums[l]
            else: return -1

        val = nums[k]
        nums[k],nums[l] = nums[l],nums[k]
        mark = l+1
        for i in range(l+1,r+1):
            if nums[i]<val:
                nums[i],nums[mark]=nums[mark],nums[i]
                mark+=1
        nums[l],nums[mark-1]=nums[mark-1],nums[l]

        if mark-1 > k:
            return part(l,mark-2,k)
        elif mark-1 < k:
            return part(mark,r,k)
        else:
            return nums[k]

    if not nums: return -1
    elif k<0 or k>=len(nums): return -1
    else: return part(0,len(nums)-1,k)

testNums = [6,4,3,1,5,2]
for i in range(len(testNums)):
    print(quickSelect(testNums,i))
