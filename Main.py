# import pygame
# import random
# import math
# from pygame.locals import *
#
# # 初始化Pygame
# pygame.init()
#
# # 窗口设置
# WIDTH, HEIGHT = 800, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("新年烟花秀")
# clock = pygame.time.Clock()
#
# # 颜色定义
# COLORS = {
#     'gold': (255, 215, 0),
#     'red': (255, 0, 0),
#     'blue': (0, 255, 255),
#     'pink': (255, 192, 203),
#     'orange': (255, 165, 0),
#     'white': (255, 255, 255)
# }
#
#
# class Firework:
#     def __init__(self):
#         self.x = random.randint(100, WIDTH - 100)
#         self.y = HEIGHT
#         self.color = random.choice(list(COLORS.values()))
#         self.radius = 3
#         self.speed = random.uniform(8, 12)
#         self.angle = math.radians(90 + random.uniform(-10, 10))
#         self.exploded = False
#         self.particles = []
#
#     def update(self):
#         if not self.exploded:
#             # 上升运动
#             self.x += math.cos(self.angle) * 0.5
#             self.y -= self.speed
#             self.speed *= 0.98  # 空气阻力
#
#             # 爆炸条件
#             if self.speed < 2:
#                 self.explode()
#
#         # 更新粒子
#         for p in self.particles[:]:
#             p.update()
#             if p.dead:
#                 self.particles.remove(p)
#
#     def explode(self):
#         self.exploded = True
#         # 生成爆炸粒子
#         for _ in range(100):
#             self.particles.append(Particle(
#                 self.x, self.y,
#                 color=random.choice(list(COLORS.values())),
#                 is_trail=False
#             ))
#
#     def draw(self, surface):
#         if not self.exploded:
#             pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)
#
#         for p in self.particles:
#             p.draw(surface)
#
#
# class Particle:
#     def __init__(self, x, y, color, is_trail=False):
#         self.x = x
#         self.y = y
#         self.color = color
#         self.age = 0
#         self.lifetime = random.randint(20, 40)
#         self.dead = False
#
#         # 物理参数
#         angle = math.radians(random.randint(0, 360))
#         speed = random.uniform(2, 8) if is_trail else random.uniform(4, 12)
#         self.vx = math.cos(angle) * speed
#         self.vy = math.sin(angle) * speed
#         self.gravity = 0.3
#         self.resistance = 0.97
#
#     def update(self):
#         self.vx *= self.resistance
#         self.vy *= self.resistance
#         self.vy += self.gravity
#
#         self.x += self.vx
#         self.y += self.vy
#         self.age += 1
#
#         if self.age > self.lifetime:
#             self.dead = True
#
#     def draw(self, surface):
#         alpha = 255 * (1 - self.age / self.lifetime)
#         size = max(1, int(3 * (1 - self.age / self.lifetime)))
#         color = (*self.color[:3], int(alpha)) if len(self.color) == 4 else (*self.color, int(alpha))
#         pygame.draw.circle(surface, color, (int(self.x), int(self.y)), size)
#
#
# # 烟花列表
# fireworks = []
# running = True
#
# # 主循环
# while running:
#     screen.fill((0, 0, 30))  # 深蓝色背景
#
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             running = False
#         elif event.type == MOUSEBUTTONDOWN:  # 鼠标点击发射
#             fireworks.append(Firework())
#
#     # 随机自动发射
#     if random.random() < 0.03:
#         fireworks.append(Firework())
#
#     # 更新和绘制烟花
#     for fw in fireworks[:]:
#         fw.update()
#         fw.draw(screen)
#         if fw.exploded and len(fw.particles) == 0:
#             fireworks.remove(fw)
#
#     pygame.display.flip()
#     clock.tick(60)  # 60 FPS
#
# pygame.quit()
import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []

        for num in nums:
            self.min_heap.append(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)

        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        return self.min_heap[0]
