"""
257. 二叉树的所有路径
    给你一个二叉树的根节点 root ，按 任意顺序 ，
    返回所有从根节点到叶子节点的路径。
    叶子节点 是指没有子节点的节点。
    示例 1：
            输入：root = [1,2,3,null,5]
            输出：["1->2->5","1->3"]
"""

from typing import List, Optional

from utils.tree_node import TreeNode


def binaryTreePaths(root: Optional[TreeNode]) -> List[str]:
    def dfs(root, path):
        if root:
            path += str(root.val)
            if not root.left and not root.right:
                paths.append(path)
            else:
                path += '->'
                dfs(root.left, path)
                dfs(root.right, path)

    paths = []
    dfs(root, '')
    return paths


#   1
#  / \
# 2   3
#  \
#   5
root = TreeNode.array_to_tree_node([1, 2, 3, None, 5])
print(binaryTreePaths(root))
