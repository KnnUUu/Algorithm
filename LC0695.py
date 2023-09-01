from typing import List

class Solution:
    # 注意不要搞错xy的顺序
    # time O(N) 因为最坏情况所有都是陆地也是4N次
    # space O(1)
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ret = max(ret,self.exploreIsland(grid,j,i))
                print()
        return ret 
    
    def exploreIsland(self, grid: List[List[int]],x:int,y:int)->int:
        if y<0 or y >= len(grid) or x<0 or x >= len(grid[0]) or grid[y][x]==0:
            return 0
        
        grid[y][x]=0
        area = 1
        area+=self.exploreIsland(grid,x-1,y)
        area+=self.exploreIsland(grid,x+1,y)
        area+=self.exploreIsland(grid,x,y-1)
        area+=self.exploreIsland(grid,x,y+1)
        return area

import unittest
class Test0695(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.maxAreaOfIsland( [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]),6)

unittest.main()
