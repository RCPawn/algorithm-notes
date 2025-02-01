"""
938. 二叉搜索树的范围和
    给定二叉搜索树的根结点 root，
    返回值位于范围 [low, high] 之间的所有结点的值的和。
    示例 1：
            输入：root = [10,5,15,3,7,null,18], low = 7, high = 15
            输出：32
    示例 2：
            输入：root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
            输出：23
"""
from collections import deque
from typing import Optional

from utils.tree_node import TreeNode


# 方法一：
def rangeSumBST(root: Optional[TreeNode], low, high) -> int:
    result_list = []
    queue = deque([root])
    while queue:
        node = queue.popleft()

        if low <= node.val <= high:
            result_list.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return sum(result_list)


# 方法二：
def rangeSumBST1(root, low, high):
    if not root:
        return 0
    if root.val > high:
        return rangeSumBST1(root.left, low, high)
    if root.val < low:
        return rangeSumBST1(root.right, low, high)
    return (root.val + rangeSumBST1(root.left, low, high)
            + rangeSumBST1(root.right, low, high))


level_order = [10, 5, 15, 3, 7, 13, 18, 1, None, 6]
tree = TreeNode.array_to_tree_node(level_order)
print(rangeSumBST(tree, 6, 10))
