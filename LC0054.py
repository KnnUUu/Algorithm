class Solution:
    def spiralOrder(self, matrix):
        # time O(N)
        # space O(n)
        if len(matrix)==0 or len(matrix[0])==0:
            return []
        hLen = len(matrix[0])
        vLen = len(matrix)

        posX = -1
        posY = 0
        odd = True
        ret = []
        while hLen > 0 and vLen > 0:
            for i in range(hLen):
                if odd:
                    posX += 1
                else:
                    posX -= 1
                #print("x:"+str(posX)+" y:"+str(posY))
                ret.append(matrix[posY][posX])
            vLen -= 1

            for j in range(vLen):
                if odd:
                    posY += 1
                else:
                    posY -= 1
                #print("x:"+str(posX)+" y:"+str(posY))
                ret.append(matrix[posY][posX])
            hLen -= 1

            odd = not odd

        return ret

test=Solution()
print(test.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
print(test.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))