# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        def bfs(root):
            level=0
            res=[]
            queue=deque()
            if root:
                queue.append(root)
            while len(queue)>0:
                curlevel=[]
                for i in range(len(queue)):
                    cur=queue.popleft()
                    curlevel.append(cur.val)
                
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
                level+=1
                res.append(curlevel[-1])

            return res
        return bfs(root)
                