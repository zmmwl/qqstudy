"""
键盘控制 - 学习用键盘控制游戏角色
==================================

这个示例展示如何处理键盘输入来控制游戏角色。

知识点：
1. 键盘事件处理
2. 按键状态检测
3. 连续移动（按住键不放）
4. 对角线移动

控制方式：
- 方向键或WASD控制移动
- 空格键跳跃/加速

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
CYAN = (0, 255, 255)


# ==================== 玩家类 ====================
class Player:
    """
    玩家类 - 可以用键盘控制的角色

    属性：
        x, y (float): 位置坐标
        width, height (int): 大小
        color (tuple): 颜色
        speed (float): 移动速度
        velocity_x, velocity_y (float): 速度向量

    方法：
        handle_input(keys): 根据按键状态更新速度
        update(width, height): 更新位置
        draw(surface): 绘制玩家
    """

    def __init__(self, x, y, width=50, height=50, color=BLUE, speed=5):
        """
        初始化玩家

        参数：
            x (float): 初始x坐标
            y (float): 初始y坐标
            width (int): 宽度，默认50
            height (int): 高度，默认50
            color (tuple): 颜色，默认蓝色
            speed (float): 移动速度，默认5

        示例：
            player = Player(400, 300)  # 使用默认参数
            player = Player(100, 100, 40, 60, RED, 8)  # 自定义参数
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
        self.velocity_x = 0
        self.velocity_y = 0

    def handle_input(self, keys):
        """
        处理键盘输入

        参数：
            keys (tuple): pygame.key.get_pressed()返回的按键状态

        支持的按键：
            方向键：UP, DOWN, LEFT, RIGHT
            WASD：W(上), S(下), A(左), D(右)

        速度设置：
            按下键：速度 = speed
            松开键：速度 = 0
        """
        # 重置速度
        self.velocity_x = 0
        self.velocity_y = 0

        # 检测按键状态
        # 上移
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.velocity_y = -self.speed
        # 下移
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.velocity_y = self.speed
        # 左移
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.velocity_x = -self.speed
        # 右移
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.velocity_x = self.speed

        # 对角线移动时，速度要除以根号2，保持速度一致
        if self.velocity_x != 0 and self.velocity_y != 0:
            self.velocity_x *= 0.707  # 1/√2 ≈ 0.707
            self.velocity_y *= 0.707

    def update(self, width, height):
        """
        更新玩家位置

        参数：
            width (int): 窗口宽度（用于边界检测）
            height (int): 窗口高度（用于边界检测）
        """
        # 更新位置
        self.x += self.velocity_x
        self.y += self.velocity_y

        # 边界检测（防止移出屏幕）
        if self.x < 0:
            self.x = 0
        elif self.x + self.width > width:
            self.x = width - self.width

        if self.y < 0:
            self.y = 0
        elif self.y + self.height > height:
            self.y = height - self.height

    def draw(self, surface):
        """
        绘制玩家

        参数：
            surface (pygame.Surface): 要绘制到的表面
        """
        pygame.draw.rect(surface, self.color,
                        (int(self.x), int(self.y), self.width, self.height))

        # 画一个简单的"眼睛"表示方向
        eye_x = int(self.x + self.width // 2 + self.velocity_x * 2)
        eye_y = int(self.y + self.height // 2 + self.velocity_y * 2)
        pygame.draw.circle(surface, WHITE, (eye_x, eye_y), 8)
        pygame.draw.circle(surface, BLACK, (eye_x, eye_y), 4)

    def get_rect(self):
        """
        获取玩家的矩形区域（用于碰撞检测）

        返回：
            pygame.Rect: 矩形对象
        """
        return pygame.Rect(int(self.x), int(self.y), self.width, self.height)


# ==================== 食物类 ====================
class Food:
    """
    食物类 - 玩家可以收集的物品
    """

    def __init__(self, x, y, size=15, color=GREEN):
        """
        初始化食物

        参数：
            x (float): x坐标
            y (float): y坐标
            size (int): 大小，默认15
            color (tuple): 颜色，默认绿色
        """
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.collected = False

    def draw(self, surface):
        """绘制食物"""
        if not self.collected:
            pygame.draw.circle(surface, self.color,
                             (int(self.x), int(self.y)), self.size)

    def check_collision(self, player_rect):
        """
        检测与玩家的碰撞

        参数：
            player_rect (pygame.Rect): 玩家的矩形区域

        返回：
            bool: 是否发生碰撞
        """
        if self.collected:
            return False

        # 创建食物的圆形碰撞区域（简化为矩形）
        food_rect = pygame.Rect(
            int(self.x - self.size),
            int(self.y - self.size),
            self.size * 2,
            self.size * 2
        )
        return player_rect.colliderect(food_rect)


# ==================== 主函数 ====================
def main():
    """
    主函数 - 键盘控制示例
    """
    # 窗口设置
    WIDTH = 800
    HEIGHT = 600

    # 初始化
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("键盘控制 - 方向键或WASD移动，ESC退出")
    clock = pygame.time.Clock()

    # 创建玩家
    player = Player(WIDTH // 2, HEIGHT // 2, 50, 50, BLUE, 6)

    # 创建一些食物
    import random
    foods = []
    for _ in range(10):
        x = random.randint(30, WIDTH - 30)
        y = random.randint(30, HEIGHT - 30)
        foods.append(Food(x, y))

    # 游戏状态
    score = 0

    # 游戏主循环
    running = True
    while running:
        # ========== 1. 处理事件 ==========
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                # 按R键重置游戏
                elif event.key == pygame.K_r:
                    player.x = WIDTH // 2
                    player.y = HEIGHT // 2
                    score = 0
                    for food in foods:
                        food.collected = False

        # ========== 2. 获取按键状态并更新 ==========
        # 获取当前所有按键的状态
        keys = pygame.key.get_pressed()

        # 根据按键状态更新玩家速度
        player.handle_input(keys)

        # 更新玩家位置
        player.update(WIDTH, HEIGHT)

        # 检测与食物的碰撞
        player_rect = player.get_rect()
        for food in foods:
            if food.check_collision(player_rect):
                food.collected = True
                score += 10

        # ========== 3. 绘制画面 ==========
        screen.fill(WHITE)

        # 绘制食物
        for food in foods:
            food.draw(screen)

        # 绘制玩家
        player.draw(screen)

        # 显示分数和提示
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        # 显示控制提示
        hint_font = pygame.font.Font(None, 24)
        hint_text = hint_font.render(
            "Arrow Keys / WASD: Move | R: Reset | ESC: Exit",
            True, (100, 100, 100)
        )
        screen.blit(hint_text, (10, HEIGHT - 30))

        pygame.display.flip()

        # 控制帧率
        clock.tick(60)

    pygame.quit()
    sys.exit()


# ==================== 扩展：支持加速和跳跃 ====================
def main_with_boost():
    """
    扩展版本：支持按住Shift加速
    """
    WIDTH = 800
    HEIGHT = 600

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("键盘控制（带加速）- Shift加速，ESC退出")
    clock = pygame.time.Clock()

    # 玩家属性
    x, y = WIDTH // 2, HEIGHT // 2
    width, height = 40, 40
    base_speed = 5
    speed = base_speed

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # 获取按键状态
        keys = pygame.key.get_pressed()

        # 按住Shift加速
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            speed = base_speed * 2
        else:
            speed = base_speed

        # 计算移动方向
        velocity_x = 0
        velocity_y = 0

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            velocity_x = -speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            velocity_x = speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            velocity_y = -speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            velocity_y = speed

        # 对角线移动修正
        if velocity_x != 0 and velocity_y != 0:
            velocity_x *= 0.707
            velocity_y *= 0.707

        # 更新位置
        x += velocity_x
        y += velocity_y

        # 边界检测
        x = max(0, min(x, WIDTH - width))
        y = max(0, min(y, HEIGHT - height))

        # 绘制
        screen.fill(WHITE)

        # 根据速度改变颜色（加速时变红）
        if speed > base_speed:
            color = RED
        else:
            color = BLUE

        pygame.draw.rect(screen, color, (int(x), int(y), width, height))

        # 显示速度
        font = pygame.font.Font(None, 36)
        speed_text = font.render(f"Speed: {speed:.1f} (Hold SHIFT to boost)", True, BLACK)
        screen.blit(speed_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


# 程序入口
if __name__ == "__main__":
    main()

    # 如果想看加速效果，把上面改成：
    # main_with_boost()
