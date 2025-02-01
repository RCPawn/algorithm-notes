"""
    Tree Node Class
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # 将数组转换为二叉树。数组表示二叉树的层次遍历，None 表示空节点。
    @staticmethod
    def array_to_tree_node(arr: List[Optional[int]]) -> Optional['TreeNode']:
        if not arr:
            return None

        root = TreeNode(arr[0])
        queue = [root]
        idx = 1

        while queue and idx < len(arr):
            node = queue.pop(0)

            if arr[idx] is not None:
                node.left = TreeNode(arr[idx])
                queue.append(node.left)
            idx += 1

            if idx < len(arr) and arr[idx] is not None:
                node.right = TreeNode(arr[idx])
                queue.append(node.right)
            idx += 1

        return root

    # 打印二叉树。使用层次遍历的方式打印。
    def print_tree_node(self):
        if not self:
            print("Empty tree")
            return

        queue = [self]
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.pop(0)
                if node:
                    print(node.val, end=" ")
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    print("None", end=" ")
            print()

    # 计算二叉树的高度。
    def tree_height(self) -> int:
        if not self:
            return 0
        left_height = self.left.tree_height() if self.left else 0
        right_height = self.right.tree_height() if self.right else 0
        return max(left_height, right_height) + 1

    # 判断二叉树是否对称。
    def is_symmetric(self) -> bool:
        def is_mirror(left: Optional['TreeNode'], right: Optional['TreeNode']) -> bool:
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (left.val == right.val and
                    is_mirror(left.left, right.right) and
                    is_mirror(left.right, right.left))

        if not self:
            return True
        return is_mirror(self.left, self.right)

    # 判断二叉树中是否包含目标值。
    def contains_value(self, target: int) -> bool:
        if not self:
            return False
        if self.val == target:
            return True
        left_contains = self.left.contains_value(target) if self.left else False
        right_contains = self.right.contains_value(target) if self.right else False
        return left_contains or right_contains

    # 统计二叉树中节点的总数。
    def count_nodes(self) -> int:
        if not self:
            return 0
        left_count = self.left.count_nodes() if self.left else 0
        right_count = self.right.count_nodes() if self.right else 0
        return 1 + left_count + right_count

    # 判断二叉树是否是平衡二叉树。
    def is_balanced(self) -> bool:
        def check_height(node: Optional['TreeNode']) -> int:
            if not node:
                return 0
            left_height = check_height(node.left)
            right_height = check_height(node.right)
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            return max(left_height, right_height) + 1

        return check_height(self) != -1

    # 返回所有从根节点到叶子节点的路径。
    def find_paths(self) -> List[str]:
        def dfs(node: Optional['TreeNode'], path: str, paths: List[str]):
            if not node:
                return
            path += str(node.val)
            if not node.left and not node.right:
                paths.append(path)
            else:
                path += "->"
                dfs(node.left, path, paths)
                dfs(node.right, path, paths)

        paths = []
        dfs(self, "", paths)
        return paths

    # 将二叉树序列化为字符串。
    def serialize(self) -> str:
        if not self:
            return "None"
        return (str(self.val) + "," +
                (self.left.serialize() if self.left else "None") + "," +
                (self.right.serialize() if self.right else "None"))

    # 将字符串反序列化为二叉树。
    @staticmethod
    def deserialize(data: str) -> Optional['TreeNode']:
        def build_tree(nodes: List[str]) -> Optional['TreeNode']:
            val = nodes.pop(0)
            if val == "None":
                return None
            node = TreeNode(int(val))
            node.left = build_tree(nodes)
            node.right = build_tree(nodes)
            return node

        nodes = data.split(",")
        return build_tree(nodes)

    # 查找二叉树中两个节点的最近公共祖先。
    def lowest_common_ancestor(self, p: 'TreeNode', q: 'TreeNode') -> Optional['TreeNode']:
        if not self or self == p or self == q:
            return self
        left = self.left.lowest_common_ancestor(p, q) if self.left else None
        right = self.right.lowest_common_ancestor(p, q) if self.right else None
        if left and right:
            return self
        return left if left else right
