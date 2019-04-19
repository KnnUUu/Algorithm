class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        self.checked = dict() # val->node
        def clone(node):
            if node.val in self.checked:
                return self.checked[node.val]
            else:
                copy = Node(node.val, [])
                self.checked[node.val] = copy
                for nei in node.neighbors:
                    copy.neighbors.append(clone(nei))
                return copy
        return clone(node)




