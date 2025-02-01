"""
637. 二叉树的层平均值
    给定一个非空二叉树的根节点 root , 以数组的形式返回每一层节点的平均值。
    与实际答案相差 10-5 以内的答案可以被接受。
    示例 1：
            输入：root = [3,9,20,null,null,15,7]
            输出：[3.00000,14.50000,11.00000]
            解释：第 0 层的平均值为 3,第 1 层的平均值为 14.5,第 2 层的平均值为 11 。
            因此返回 [3, 14.5, 11] 。
    示例 2:
            输入：root = [3,9,20,15,7]
            输出：[3.00000,14.50000,11.00000]
"""
from collections import deque
from typing import List, Optional
from utils.tree_node import TreeNode


def averageOfLevels(root: Optional[TreeNode]) -> List[float]:
    queue = deque([root])
    average_of_levels = []
    while queue:
        total = 0
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            total += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        average_of_levels.append(total / level_size)
    return average_of_levels


#   3
#  / \
# 9  20
#   /  \
#  15   7
root = TreeNode.array_to_tree_node([3, 9, 20, None, None, 15, 7])
print(averageOfLevels(root))
