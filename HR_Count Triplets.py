# 保存各个数字的index
# 然后再遍历一次计算每个结果是否成立，太慢
def countTriplets_my_solution(arr, r):
    # time average O(N), worse O((1/3N)^3) -> O(1/9N^3) -> O(n^3)
    # worse case: 3 array with same size [1,1,1], [3,3,3],[9,9,9]
    # space O(N)
    val2index = dict() # int -> list

    for i in range(len(arr)):
        if arr[i] not in val2index:
            val2index[arr[i]] = [i]
        else:
            val2index[arr[i]].append(i)

    ret = 0
    for i in range(len(arr)):
        val = arr[i]
        if val*r in val2index and val*r*r in val2index:
            firstIndex = i
            for secondIndex in val2index[val*r]:
                for thirdIndex in val2index[val*r*r]:
                    if firstIndex < secondIndex < thirdIndex:
                        ret +=1

    return ret

# 核心思想是遇到了某个数字就先预测如果下次遇到这个数字时能增加几个count
# 先预测好遇到时因为都是发生在之前的计算所以可以保证index1<index2<index3
from collections import defaultdict
def countTriplets(arr, r):
    # 预测二、三次幂的hash
    predictDouble = defaultdict(int)
    predictTrible = defaultdict(int)

    ret = 0
    for n in arr:
        # 之前预测的三次幂结果，因为遇到了所以可以加上了
        ret += predictTrible[n]
        # 添加三次幂预测，再次之前已经有predictDouble[n]个组合了
        predictTrible[n*r] += predictDouble[n]
        # 添加二次幂预测,1指当前n个数
        predictDouble[n*r] += 1
    return ret 