"""
112. 路径总和
    给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。
    判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。
    如果存在，返回 true ；否则，返回 false 。
    叶子节点 是指没有子节点的节点。
    示例 1：
            输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
            输出：true
            解释：等于目标和的根节点到叶节点路径如上图所示。
"""

from typing import Optional
from utils.tree_node import TreeNode


def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False
    if not root.left and not root.right:
        return root.val == targetSum
    return (hasPathSum(root.left, targetSum - root.val)
            or hasPathSum(root.right, targetSum - root.val))


#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1
level_order = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
root = TreeNode.array_to_tree_node(level_order)
print(hasPathSum(root, 22))
