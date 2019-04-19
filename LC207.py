def canFinish_1(numCourses, prerequisites) -> bool:
    # key idea is to check no ring
    visit = [0 for i in range(numCourses)]
    # 0 not visited, 1 visiting, 2 visited
    edges = [[] for i in range(numCourses)]
    for prere in prerequisites: edges[prere[1]].append(prere[0]) # E
    print(edges)

    def DFS(vertex):
        if visit[vertex]==2: return True
        elif visit[vertex]==1: return False

        visit[vertex]=1
        if not all([DFS(edge) for edge in edges[vertex]]): return False
        visit[vertex]=2
        return True

    return all([DFS(i) for i in range(numCourses)]) # V+E

import collections
def canFinish_2(numCourses, prerequisites) -> bool:
    need=[0 for i in range(numCourses)] # 1
    for pre in prerequisites: need[pre[0]]+=1 # E
    print(need)
    q = collections.deque()
    for i in range(numCourses): # V
        if need[i]==0: q.append(i)
    while q: # V
        v = q.pop()
        for pre in prerequisites: # E
            if pre[1]==v:
                need[pre[0]]-=1
                if need[pre[0]] == 0: q.append(pre[0])
    print(need)
    return all([x==0 for x in need])

def canFinish_3(numCourses, prerequisites) -> bool:
    need=[0 for i in range(numCourses)] # 1
    edges = [[] for i in range(numCourses)] #1
    for pre in prerequisites: # E
        need[pre[0]]+=1
        edges[pre[1]].append(pre[0])
    print(need)
    q = collections.deque()
    for i in range(numCourses): # V
        if need[i]==0: q.append(i)
    count = 0
    while q: # V+E
        v = q.pop()
        count+=1
        for x in edges[v]:
            need[x]-=1
            if need[x] == 0: q.append(x)
    print(need)
    return count==numCourses

print(canFinish_3(5, [[1,2],[2,0],[0,1],[3,0],[4,3]]))
print()
print(canFinish_3(5, [[1,2],[0,1],[3,0],[4,3]]))
print()
print(canFinish_3(0, []))