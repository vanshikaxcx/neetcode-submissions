"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nakshaa={None:None}
        cur=head
        while cur:
            copy=Node(cur.val)
            nakshaa[cur]=copy
            cur=cur.next

        cur=head
        while cur:
            copy=nakshaa[cur]
            copy.next=nakshaa[cur.next]
            copy.random=nakshaa[cur.random]
            cur=cur.next

        return nakshaa[head]