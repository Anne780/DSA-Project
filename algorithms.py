class Solution:
    def maxPathSum(self, root):
        def helper(node):
            if not node:
                return 0
            left = max(helper(node.left), 0)
            right = max(helper(node.right), 0)
            max_path[0] = max(max_path[0], left + node.val + right)
            return node.val + max(left, right)

        max_path = [float('-inf')]
        helper(root)
        return max_path[0]
