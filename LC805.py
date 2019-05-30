class Solution(object):
    def splitArraySameAverage(self,A):
        if len(A) <= 1: return False

        def judge(target,sumArr,remain,arr):
            if remain==0:
                return sumArr==target
            if remain>len(arr) or not arr: return False
            return (judge(target,sumArr+arr[0],remain-1,arr[1:])
                    or judge(target,sumArr,remain,arr[1:]))

        avg = sum(A) / len(A)
        for lenB in range(1, (len(A) + 1) // 2 + 1):
            if judge(lenB * avg, 0, lenB, A): return True
        return False

test = Solution()
assert test.splitArraySameAverage([0]) == False
assert test.splitArraySameAverage([1,2,3,4,5,6,7,8]) == True
assert test.splitArraySameAverage([4, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 4, 5]) == True




