# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        def bfs(root):  
            queue=deque()
            res=[]
            level=0
            if root:
                queue.append(root)
            while len(queue)>0:
                cur_level=[]
                for i in range(len(queue)):
                    cur=queue.popleft()
                    cur_level.append(cur.val)
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
                level+=1
                res.append(cur_level)
            return res
        return bfs(root)
            