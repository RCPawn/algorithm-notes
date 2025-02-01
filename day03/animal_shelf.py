"""
面试题 03.06. 动物收容所
    动物收容所。有家动物收容所只收容狗与猫，且严格遵守“先进先出”的原则。
    在收养该收容所的动物时，收养人只能收养所有动物中“最老”（由其进入收容所的时间长短而定）的动物，或者可以挑选猫或狗（同时必须收养此类动物中“最老”的）。
    换言之，收养人不能自由挑选想收养的对象。请创建适用于这个系统的数据结构，实现各种操作方法，比如enqueue、dequeueAny、dequeueDog和dequeueCat。
    允许使用Java内置的LinkedList数据结构。
    enqueue方法有一个animal参数，animal[0]代表动物编号，animal[1]代表动物种类，其中 0 代表猫，1 代表狗。
    dequeue*方法返回一个列表[动物编号, 动物种类]，若没有可以收养的动物，则返回[-1,-1]。
    示例 1：
             输入：
                ["AnimalShelf", "enqueue", "enqueue", "dequeueCat", "dequeueDog", "dequeueAny"]
                [[], [[0, 0]], [[1, 0]], [], [], []]
             输出：[null,null,null,[0,0],[-1,-1],[1,0]]
    示例 2：
             输入：
                ["AnimalShelf", "enqueue", "enqueue", "enqueue", "dequeueDog", "dequeueCat", "dequeueAny"]
                [[], [[0, 0]], [[1, 0]], [[2, 1]], [], [], []]
             输出：[null,null,null,null,[2,1],[0,0],[1,0]]
"""

from collections import deque
from typing import List


class AnimalShelf:
    def __init__(self):
        self.cats = deque()
        self.dogs = deque()

    def enqueue(self, animal: List[int]) -> None:
        # 动物ID和类型（0代表猫，1代表狗）
        animal_id, animal_type = animal
        if animal_type == 0:
            self.cats.append(animal_id)  # 猫入队
        else:
            self.dogs.append(animal_id)  # 狗入队

    def dequeueAny(self) -> List[int]:
        if not self.cats:
            return self.dequeueDog()
        if not self.dogs:
            return self.dequeueCat()

        if self.cats[0] < self.dogs[0]:
            return self.dequeueCat()
        else:
            return self.dequeueDog()

    def dequeueDog(self) -> List[int]:
        # 如果狗队列为空，返回[-1, -1]
        if not self.dogs:
            return [-1, -1]
        # 从狗队列中弹出最老的狗并返回
        return [self.dogs.popleft(), 1]

    def dequeueCat(self) -> List[int]:
        if not self.cats:
            return [-1, -1]
        return [self.cats.popleft(), 0]

# Your AnimalShelf object will be instantiated and called as such:
# obj = AnimalShelf()
# obj.enqueue(animal)
# param_2 = obj.dequeueAny()
# param_3 = obj.dequeueDog()
# param_4 = obj.dequeueCat()
