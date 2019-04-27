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


def quickSelect(nums,k):
    k-=1


print(quickSelect([3,2,1,5,6,4],0,5,k = 1-1))
print(quickSelect([3,2,1,5,6,4],0,5,k = 2-1))
print(quickSelect([3,2,1,5,6,4],0,5,k = 3-1))
print(quickSelect([3,2,1,5,6,4],0,5,k = 4-1))
print(quickSelect([3,2,1,5,6,4],0,5,k = 5-1))
print(quickSelect([3,2,1,5,6,4],0,5,k = 6-1))