"""
3074. 重新分装苹果
    给你一个长度为 n 的数组 apple 和另一个长度为 m 的数组 capacity 。
    一共有 n 个包裹，其中第 i 个包裹中装着 apple[i] 个苹果。
    同时，还有 m 个箱子，第 i 个箱子的容量为 capacity[i] 个苹果。
    请你选择一些箱子来将这 n 个包裹中的苹果重新分装到箱子中，返回你需要选择的箱子的 最小 数量。
    注意，同一个包裹中的苹果可以分装到不同的箱子中。
    示例 1：
            输入：apple = [1,3,2], capacity = [4,3,1,5,2]
            输出：2
            解释：使用容量为 4 和 5 的箱子。
            总容量大于或等于苹果的总数，所以可以完成重新分装。
    示例 2：
            输入：apple = [5,5,5], capacity = [2,4,2,7]
            输出：4
            解释：需要使用所有箱子。
"""
from typing import List


# 方法一
def minimum_boxes(apple, capacity: List[int]):
    need_size = sum(apple)
    capacity.sort(reverse=True)
    current_size, min_boxes = 0, 0
    for box_size in capacity:
        if current_size < need_size:
            current_size += box_size
        else:
            break
        min_boxes += 1
    return min_boxes


# 方法二：
def minimum_boxes1(apple, capacity):
    need_size = sum(apple)
    capacity.sort(reverse=True)
    for count, box_size in enumerate(capacity, 1):
        need_size -= box_size
        if need_size <= 0:
            return count


apple = [5, 5, 5]
capacity = [2, 4, 2, 7]
print(minimum_boxes1(apple, capacity))
