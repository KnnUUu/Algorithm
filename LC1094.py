class Solution:
    # time O(N)
    # space O(1)
    # 因为总路程有限，使用一个list记录各个点乘客增减，最后看中间有没有超就可
    def carPooling1(self, trips, capacity: int) -> bool:
        numPassenger = [0 for i in range(1001)]
        for pas,fr,to in trips:
            numPassenger[fr]+=pas
            numPassenger[to]-=pas

        curPassenger=0
        for i in range(len(numPassenger)):
            curPassenger += numPassenger[i]
            if curPassenger>capacity:
                return False
        return True

    # 先找出所有上下时间点跟人数
    # 再sort后跟上面一样的判断方法
    # c++的map()因为底层是红黑树可以按照键大小排序，可以直接用，python的OrderedDict()因为只能记录插入顺序所以需要自己排
    def carPooling(self, trips, capacity: int) -> bool:
        tripInfo = [[0,0] for i in range(len(trips)*2)]
        for i in range(len(trips)):
            tripInfo[i*2][0]=trips[i][1]
            tripInfo[i*2][1]=trips[i][0]

            tripInfo[i*2+1][0]=trips[i][2]
            tripInfo[i*2+1][1]=-trips[i][0]

        tripInfo = sorted(tripInfo,key = lambda val:val[0])
        print(tripInfo)
        curPassenger=0
        for i in range(len(tripInfo)):
            curPassenger += tripInfo[i][1]
            # 防止同个低点多个上下时，由于先计算增加的导致结果出错
            if curPassenger>capacity and (i+1<len(tripInfo) and tripInfo[i][0]!=tripInfo[i+1][0]):
                return False
        return True
        
test = Solution()
assert(test.carPooling([[2,1,5],[3,3,7]],4)==False)
assert(test.carPooling([[2,1,5],[3,3,7]],5)==True)
assert(test.carPooling([[4,5,6],[6,4,7],[4,3,5],[2,3,5]],13)==True)