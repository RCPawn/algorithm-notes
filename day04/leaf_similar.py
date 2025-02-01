"""
872. 叶子相似的树
    请考虑一棵二叉树上所有的叶子，
    这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。
    举个例子，如上图所示，给定一棵叶值序列为 (6, 7, 4, 9, 8) 的树。
    如果有两棵二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。
    如果给定的两个根结点分别为 root1 和 root2 的树是叶相似的，
    则返回 true；否则返回 false 。
    示例 1：
            输入：root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
            输出：true
    示例 2：
            输入：root1 = [1,2,3], root2 = [1,3,2]
            输出：false
"""
from utils.tree_node import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def leafSimilar(root1, root2) -> bool:
    def dfs(node):
        if not node:
            return []
        if not node.left and not node.right:
            return [node.val]
        return dfs(node.left) + dfs(node.right)

    return dfs(root1) == dfs(root2)


arr1 = [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]
arr2 = [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]
root1 = TreeNode.array_to_tree_node(arr1)
root2 = TreeNode.array_to_tree_node(arr2)

print(leafSimilar(root1, root2))
