"""
LCR 150. 彩灯装饰记录 II
    一棵圣诞树记作根节点为 root 的二叉树，节点值为该位置装饰彩灯的颜色编号。
    请按照从左到右的顺序返回每一层彩灯编号，每一层的结果记录于一行。
    示例 1：
            输入：root = [8,17,21,18,null,null,6]
            输出：[[8],[17,21],[18,6]]
"""
from collections import deque
from typing import Optional, List

from utils.tree_node import TreeNode


def decorateRecord(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    res, queue = [], deque([root])
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(current_level)
    return res


#     8
#    / \
#   17 21
#  /     \
# 18      6

root = TreeNode.array_to_tree_node([8, 17, 21, 18, None, None, 6])
print(decorateRecord(root))
