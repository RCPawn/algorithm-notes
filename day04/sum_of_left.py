"""
404. 左叶子之和
    给定二叉树的根节点 root ，返回所有左叶子之和。
    示例 1：
            输入: root = [3,9,20,null,null,15,7]
            输出: 24
            解释: 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
    示例 2:
            输入: root = [1]
            输出: 0
"""
from typing import Optional

from utils.tree_node import TreeNode


# 方法一：
def sumOfLeftLeaves(root: Optional[TreeNode]) -> int:
    def dfs(node):
        if not node:
            return 0
        left_sum = 0
        if node.left and not node.left.left and not node.left.right:
            left_sum += node.left.val

        left_sum += dfs(node.left)
        left_sum += dfs(node.right)
        return left_sum

    if not root:
        return 0
    return dfs(root)


root = TreeNode.array_to_tree_node([3, 9, 20, None, None, 15, 7])
print(sumOfLeftLeaves(root))
