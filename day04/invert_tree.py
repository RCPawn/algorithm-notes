"""
226. 翻转二叉树
    给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。
    示例 1：
            输入：root = [4,2,7,1,3,6,9]
            输出：[4,7,2,9,6,3,1]
    示例 2：
            输入：root = [2,1,3]
            输出：[2,3,1]
    示例 3：
            输入：root = []
            输出：[]
"""
from typing import Optional
from utils.tree_node import TreeNode


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return root
    left = invertTree(root.left)
    right = invertTree(root.right)
    root.left, root.right = right, left
    return root


root = TreeNode.array_to_tree_node([4, 2, 7, 1, 3, 6, 9])
tree = invertTree(root)
