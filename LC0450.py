# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        print("Node val:" + root.val + " Key:" + key)

        # time O(N) space O(1)
        if root == None:
            return None
        elif root.val < key:
            root.right = self.deleteNode(root.right,key)
        elif root.val > key:
            root.left = self.deleteNode(root.left,key)
        else:
            # 找到val为key的node
            if root.left == None and root.right == None:
                return None
            elif root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            else:
                # 找到比当前次一大或者次一小的元素，交换后删除
                # 这里是找次一大的
                swapNode = root.right
                while swapNode.left:
                    swapNode = swapNode.left
                root.val = swapNode.val
                root.right = self.deleteNode(root.right,swapNode.val)
        return root
