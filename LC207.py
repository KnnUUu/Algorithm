def canFinish(self, numCourses: int, prerequisites) -> bool:
    reached = [False for i in range(numCourses)]
    connect = []
