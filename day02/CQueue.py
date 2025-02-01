"""
LCR 125. 图书整理 II
    读者来到图书馆排队借还书，图书管理员使用两个书车来完成整理借还书的任务。
    书车中的书从下往上叠加存放，图书管理员每次只能拿取书车顶部的书。
    排队的读者会有两种操作：
    1. push(bookID)：把借阅的书籍还到图书馆。
    2. pop()：从图书馆中借出书籍。
    为了保持图书的顺序，图书管理员每次取出供读者借阅的书籍是 最早 归还到图书馆的书籍。
    你需要返回 每次读者借出书的值 。
    如果没有归还的书可以取出，返回 -1 。
    示例 1：
            输入：
                ["BookQueue", "push", "push", "pop"]
                [[], [1], [2], []]
                输出：[null,null,null,1]
            解释：
                MyQueue myQueue = new MyQueue();
                myQueue.push(1); // queue is: [1]
                myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
                myQueue.pop(); // return 1, queue is [2]
"""


class CQueue:

    def __init__(self):
        # 存储新加入的书籍
        self.stack_in = []
        # 存储待移除的书籍
        self.stack_out = []

    def appendTail(self, value: int) -> None:
        self.stack_in.append(value)

    def deleteHead(self) -> int:
        # 检查 stack_out 是否为空
        if not self.stack_out:
            # 将 stack_in 中的所有元素转移到 stack_out
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        # 再次检查 stack_out 是否为空
        if not self.stack_out:
            return -1  # 队列为空，返回 -1
        return self.stack_out.pop()

    def deleteHead1(self):
        if self.stack_out:
            return self.stack_out.pop()
        if not self.stack_in:
            return -1
        while self.stack_in:
            self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
