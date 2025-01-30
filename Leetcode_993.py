# Time Complexity: O(n)
# Space Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
    
        queue = deque([(root, None)])  # (node, parent)
        
        while queue:
            size = len(queue)
            x_parent = y_parent = None

            for i in range(size):
                node, parent = queue.popleft()
                if node.val == x:
                    x_parent = parent
                if node.val == y:
                    y_parent = parent
                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))

            if x_parent and y_parent:
                return x_parent != y_parent  # Different parents, same depth
            if x_parent or y_parent:
                return False  # One found, the other not in the same level

        return False
