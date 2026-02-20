"""
移动的小球 - 学习让物体动起来
==============================

这个示例展示如何在pygame中让物体移动。

知识点：
1. 游戏物体的位置和速度
2. 更新位置的原理
3. 边界检测和反弹
4. 帧率与移动速度的关系

移动原理：
- 位置 = 位置 + 速度
- 每帧更新位置，物体就会移动

作者：游戏开发速成教程
"""

import pygame
import sys

# ==================== 颜色常量 ====================
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


# ==================== 小球类 ====================
class Ball:
    """
    小球类 - 封装小球的属性和行为

    属性：
        x (float): 小球中心的x坐标
        y (float): 小球中心的y坐标
        radius (int): 小球半径
        color (tuple): 小球颜色
        speed_x (float): x方向速度（像素/帧）
        speed_y (float): y方向速度（像素/帧）

    方法：
        update(): 更新小球位置
        draw(surface): 绘制小球
        check_boundary(width, height): 边界检测和反弹
    """

    def __init__(self, x, y, radius, color, speed_x, speed_y):
        """
        初始化小球

        参数：
            x (float): 初始x坐标
            y (float): 初始y坐标
            radius (int): 半径
            color (tuple): 颜色
            speed_x (float): x方向速度
            speed_y (float): y方向速度

        示例：
            ball = Ball(400, 300, 20, RED, 5, 3)
        """
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self):
        """
        更新小球位置

        原理：新位置 = 旧位置 + 速度
        这是游戏中最基本的移动公式！
        """
        self.x += self.speed_x
        self.y += self.speed_y

    def draw(self, surface):
        """
        绘制小球

        参数：
            surface (pygame.Surface): 要绘制到的表面
        """
        pygame.draw.circle(surface, self.color,
                          (int(self.x), int(self.y)), self.radius)

    def check_boundary(self, width, height):
        """
        边界检测和反弹

        参数：
            width (int): 窗口宽度
            height (int): 窗口高度

        反弹原理：
        当小球碰到边界时，将对应方向的速度取反
        速度为正表示向右/下移动，为负表示向左/上移动
        """
        # 左右边界
        if self.x - self.radius <= 0:  # 碰到左边界
            self.x = self.radius  # 防止卡在边界
            self.speed_x = -self.speed_x  # 速度取反（反弹）
        elif self.x + self.radius >= width:  # 碰到右边界
            self.x = width - self.radius
            self.speed_x = -self.speed_x

        # 上下边界
        if self.y - self.radius <= 0:  # 碰到上边界
            self.y = self.radius
            self.speed_y = -self.speed_y
        elif self.y + self.radius >= height:  # 碰到下边界
            self.y = height - self.radius
            self.speed_y = -self.speed_y


# ==================== 主函数 ====================
def main():
    """
    主函数 - 展示小球移动和反弹
    """
    # 窗口设置
    WIDTH = 800
    HEIGHT = 600

    # 初始化pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("移动的小球 - 按ESC退出")
    clock = pygame.time.Clock()

    # 创建小球
    # 参数：x, y, 半径, 颜色, x速度, y速度
    ball1 = Ball(400, 300, 30, RED, 5, 3)
    ball2 = Ball(100, 100, 20, BLUE, -4, 6)
    ball3 = Ball(600, 400, 25, GREEN, 3, -5)

    # 把所有小球放入列表，方便统一处理
    balls = [ball1, ball2, ball3]

    # 游戏主循环
    running = True
    while running:
        # ========== 1. 处理事件 ==========
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # 按ESC键退出
                if event.key == pygame.K_ESCAPE:
                    running = False

        # ========== 2. 更新游戏状态 ==========
        for ball in balls:
            ball.update()  # 更新位置
            ball.check_boundary(WIDTH, HEIGHT)  # 检测边界

        # ========== 3. 绘制画面 ==========
        # 清屏
        screen.fill(WHITE)

        # 绘制所有小球
        for ball in balls:
            ball.draw(screen)

        # 显示提示文字
        font = pygame.font.Font(None, 36)
        text = font.render("Press ESC to exit", True, BLACK)
        screen.blit(text, (10, 10))

        # 更新显示
        pygame.display.flip()

        # 控制帧率为60FPS
        clock.tick(60)

    pygame.quit()
    sys.exit()


# ==================== 扩展：带轨迹的小球 ====================
def main_with_trail():
    """
    扩展版本：小球带有运动轨迹
    展示如何实现拖尾效果
    """
    WIDTH = 800
    HEIGHT = 600

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("带轨迹的小球 - 按ESC退出")
    clock = pygame.time.Clock()

    # 小球属性
    x, y = 400, 300
    speed_x, speed_y = 5, 3
    radius = 20

    # 轨迹列表（存储之前的位置）
    trail = []
    max_trail_length = 50  # 最大轨迹长度

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # 更新位置
        x += speed_x
        y += speed_y

        # 边界检测
        if x - radius <= 0 or x + radius >= WIDTH:
            speed_x = -speed_x
        if y - radius <= 0 or y + radius >= HEIGHT:
            speed_y = -speed_y

        # 保存当前位置到轨迹
        trail.append((x, y))
        if len(trail) > max_trail_length:
            trail.pop(0)  # 移除最旧的位置

        # 绘制
        screen.fill(WHITE)

        # 绘制轨迹（渐变效果）
        for i, pos in enumerate(trail):
            # 计算透明度和大小（越早的位置越淡、越小）
            alpha = int(255 * (i + 1) / len(trail))
            size = int(radius * (i + 1) / len(trail))
            # 创建带透明度的表面
            trail_surface = pygame.Surface((size * 2, size * 2), pygame.SRCALPHA)
            pygame.draw.circle(trail_surface, (*RED, alpha), (size, size), size)
            screen.blit(trail_surface, (int(pos[0]) - size, int(pos[1]) - size))

        # 绘制主小球
        pygame.draw.circle(screen, RED, (int(x), int(y)), radius)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


# 程序入口
if __name__ == "__main__":
    # 运行基础版本
    main()

    # 如果想看轨迹效果，把上面改成：
    # main_with_trail()
