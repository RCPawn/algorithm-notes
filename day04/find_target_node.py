"""
LCR 174. 寻找二叉搜索树中的目标节点
    某公司组织架构以二叉搜索树形式记录，节点值为处于该职位的员工编号。
    请返回第 cnt 大的员工编号。
    示例 1：
            输入：root = [7, 3, 9, 1, 5], cnt = 2
    输出：7
    示例 2：
            输入: root = [10, 5, 15, 2, 7, null, 20, 1, null, 6, 8], cnt = 4
            输出: 8
"""
from collections import deque
from typing import Optional
from utils.tree_node import TreeNode


# 方法一：
def findTargetNode(root: Optional[TreeNode], cnt: int) -> int:
    queue = deque([root])
    node_set = set()
    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            node_set.add(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return sorted(node_set)[-cnt]


# 方法二：
def findTargetNode1(self, root: Optional[TreeNode], cnt: int) -> int:
    def dfs(root):
        if not root:
            return
        dfs(root.right)
        if self.cnt == 0:
            return
        self.cnt -= 1
        if self.cnt == 0:
            self.res = root.val
        dfs(root.left)

    self.cnt = cnt
    dfs(root)
    return self.res


level_order = [10, 5, 15, 2, 7, None, 20, 1, None, 6, 8]
root = TreeNode.array_to_tree_node(level_order)
print(findTargetNode(root, 4))
