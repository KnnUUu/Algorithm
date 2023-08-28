import random
import math

class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self):
        tangle = random.random()*math.radians(360)
        length = math.sqrt(random.random())*self.radius # 加sqrt的原因是为了使点分布均匀，不加的话大部分会分布在外面
        y = self.y_center+math.sin(tangle)*length
        x = self.x_center+math.cos(tangle)*length
        return [x,y]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
