"""
671. 二叉树中第二小的节点
    给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或 0。
    如果一个节点有两个子节点的话，那么该节点的值等于两个子节点中较小的一个。
    更正式地说，即 root.val = min(root.left.val, root.right.val) 总成立。
    给出这样的一个二叉树，你需要输出所有节点中的 第二小的值 。
    如果第二小的值不存在的话，输出 -1 。
    示例 1：
            输入：root = [2,2,5,null,null,5,7]
            输出：5
            解释：最小的值是 2 ，第二小的值是 5 。
    示例 2：
            输入：root = [2,2,2]
            输出：-1
            解释：最小的值是 2, 但是不存在第二小的值。
"""
from collections import deque
from typing import Optional
from utils.tree_node import TreeNode


# def findSecondMinimumValue(root: Optional[TreeNode]) -> int:
#     queue = deque([root])
#     tree_set = set()
#     while queue:
#         level_size = len(queue)
#         for _ in range(level_size):
#             node = queue.popleft()
#             tree_set.add(node.val)
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
#     if len(tree_set) == 1:
#         return -1
#     sorted_list = sorted(tree_set)
#     return sorted_list[1]

def findSecondMinimumValue(root: Optional[TreeNode]) -> int:
    if not root:
        return -1

    min_value = root.val
    second_min = float('inf')
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if min_value < node.val < second_min:
            second_min = node.val

        if node.val == min_value:
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return second_min if second_min != float('inf') else -1


#   2
#  / \
# 2   5
#    / \
#   5   7
root = TreeNode.array_to_tree_node([2, 2, 5, None, None, 5, 5])
print(findSecondMinimumValue(root))
