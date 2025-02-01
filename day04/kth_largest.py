"""
703. 数据流中的第 K 大元素
    设计一个找到数据流中第 k 大元素的类（class）。
    注意是排序后的第 k 大元素，不是第 k 个不同的元素。
    请实现 KthLargest 类：
        KthLargest(int k, int[] nums) 使用整数 k 和整数流 nums 初始化对象。
        int add(int val) 将 val 插入数据流 nums 后，返回当前数据流中第 k 大的元素。
    示例 1：
            输入：
                ["KthLargest", "add", "add", "add", "add", "add"]
                [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
            输出：[null, 4, 5, 5, 8, 8]
            解释：
                KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
                kthLargest.add(3); // 返回 4
                kthLargest.add(5); // 返回 5
                kthLargest.add(10); // 返回 5
                kthLargest.add(9); // 返回 8
                kthLargest.add(4); // 返回 8
    示例 2：
            输入：
                ["KthLargest", "add", "add", "add", "add"]
                [[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]]

            输出：[null, 7, 7, 7, 8]
            解释：
                KthLargest kthLargest = new KthLargest(4, [7, 7, 7, 7, 8, 3]);
                kthLargest.add(2); // 返回 7
                kthLargest.add(10); // 返回 7
                kthLargest.add(9); // 返回 7
                kthLargest.add(9); // 返回 8
"""
import heapq

from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # 将新值 val 插入最小堆中
        heapq.heappush(self.min_heap, val)

        # 如果堆的大小超过 k，则移除堆顶的最小元素
        # 因为堆顶的元素就是当前堆中的最小元素，去掉它可以确保堆只保留 k 个最大元素
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        return self.min_heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
