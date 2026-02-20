"""
接球游戏 - 第一个完整的小游戏
==============================

游戏说明：
- 用键盘左右移动挡板
- 接住下落的小球
- 每接住一个球得10分
- 漏掉3个球游戏结束

知识点：
1. 完整的游戏结构
2. 碰撞检测
3. 游戏状态管理
4. 计分系统

控制：
- 左右方向键或A/D键移动
- 空格键重新开始
- ESC退出

作者：游戏开发速成教程
"""

import pygame
import sys
import random

# ==================== 颜色常量 ====================
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)


# ==================== 挡板类 ====================
class Paddle:
    """
    挡板类 - 玩家控制的角色

    属性：
        x, y (float): 位置坐标
        width, height (int): 大小
        color (tuple): 颜色
        speed (float): 移动速度

    方法：
        handle_input(keys): 处理键盘输入
        update(width): 更新位置
        draw(surface): 绘制挡板
        get_rect(): 获取矩形区域
    """

    def __init__(self, x, y, width=100, height=15, color=BLUE, speed=8):
        """
        初始化挡板

        参数：
            x (float): 初始x坐标
            y (float): 初始y坐标
            width (int): 宽度，默认100
            height (int): 高度，默认15
            color (tuple): 颜色，默认蓝色
            speed (float): 移动速度，默认8
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

    def handle_input(self, keys):
        """
        处理键盘输入

        参数：
            keys (tuple): 按键状态

        返回：
            float: x方向速度
        """
        velocity_x = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            velocity_x = -self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            velocity_x = self.speed
        return velocity_x

    def update(self, velocity_x, width):
        """
        更新挡板位置

        参数：
            velocity_x (float): x方向速度
            width (int): 窗口宽度
        """
        self.x += velocity_x

        # 边界检测
        if self.x < 0:
            self.x = 0
        elif self.x + self.width > width:
            self.x = width - self.width

    def draw(self, surface):
        """
        绘制挡板

        参数：
            surface (pygame.Surface): 绘制目标
        """
        # 绘制主体
        pygame.draw.rect(surface, self.color,
                        (int(self.x), int(self.y), self.width, self.height))

        # 绘制高光效果
        pygame.draw.rect(surface, WHITE,
                        (int(self.x) + 5, int(self.y) + 2,
                         self.width - 10, 4))

    def get_rect(self):
        """获取矩形区域"""
        return pygame.Rect(int(self.x), int(self.y), self.width, self.height)


# ==================== 球类 ====================
class Ball:
    """
    球类 - 需要被接住的对象

    属性：
        x, y (float): 位置坐标
        radius (int): 半径
        color (tuple): 颜色
        speed_y (float): 下落速度

    方法：
        update(): 更新位置
        draw(surface): 绘制球
        check_collision(paddle_rect): 检测与挡板的碰撞
        is_off_screen(height): 检测是否落出屏幕
    """

    def __init__(self, x, y, radius=12, color=RED, speed_y=4):
        """
        初始化球

        参数：
            x (float): 初始x坐标
            y (float): 初始y坐标
            radius (int): 半径，默认12
            color (tuple): 颜色，默认红色
            speed_y (float): 下落速度，默认4
        """
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed_y = speed_y
        self.active = True

    def update(self):
        """更新球的位置（向下移动）"""
        if self.active:
            self.y += self.speed_y

    def draw(self, surface):
        """绘制球"""
        if self.active:
            # 绘制主体
            pygame.draw.circle(surface, self.color,
                             (int(self.x), int(self.y)), self.radius)
            # 绘制高光
            pygame.draw.circle(surface, WHITE,
                             (int(self.x) - 3, int(self.y) - 3), 4)

    def check_collision(self, paddle_rect):
        """
        检测与挡板的碰撞

        参数：
            paddle_rect (pygame.Rect): 挡板的矩形区域

        返回：
            bool: 是否发生碰撞
        """
        if not self.active:
            return False

        # 获取球的矩形区域
        ball_rect = pygame.Rect(
            int(self.x - self.radius),
            int(self.y - self.radius),
            self.radius * 2,
            self.radius * 2
        )

        # 检测碰撞
        if ball_rect.colliderect(paddle_rect):
            # 确保球是从上方来的
            if self.y < paddle_rect.centery:
                self.active = False
                return True
        return False

    def is_off_screen(self, height):
        """
        检测球是否落出屏幕

        参数：
            height (int): 窗口高度

        返回：
            bool: 是否落出屏幕
        """
        return self.y - self.radius > height


# ==================== 游戏类 ====================
class CatchBallGame:
    """
    接球游戏类 - 管理整个游戏
    """

    def __init__(self, width=800, height=600):
        """
        初始化游戏

        参数：
            width (int): 窗口宽度
            height (int): 窗口高度
        """
        # 窗口设置
        self.width = width
        self.height = height

        # 初始化pygame
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("接球游戏 - 方向键移动，ESC退出")
        self.clock = pygame.time.Clock()

        # 创建字体
        self.font = pygame.font.Font(None, 48)
        self.small_font = pygame.font.Font(None, 32)

        # 初始化游戏状态
        self.reset_game()

    def reset_game(self):
        """重置游戏状态"""
        # 创建挡板（在屏幕底部中央）
        self.paddle = Paddle(
            x=self.width // 2 - 50,
            y=self.height - 40,
            width=100,
            height=15,
            color=BLUE,
            speed=8
        )

        # 球列表
        self.balls = []

        # 游戏状态
        self.score = 0
        self.lives = 3
        self.game_over = False

        # 球的生成计时器
        self.ball_timer = 0
        self.ball_interval = 60  # 每60帧生成一个新球（约1秒）

        # 难度递增
        self.difficulty = 1

    def spawn_ball(self):
        """生成一个新球"""
        # 随机x位置
        x = random.randint(30, self.width - 30)

        # 根据难度调整速度
        base_speed = 3 + self.difficulty * 0.5
        speed = random.uniform(base_speed, base_speed + 2)

        # 随机颜色
        colors = [RED, ORANGE, YELLOW, GREEN, CYAN, PURPLE]
        color = random.choice(colors)

        ball = Ball(x, 0, radius=12, color=color, speed_y=speed)
        self.balls.append(ball)

    def update(self):
        """更新游戏状态"""
        if self.game_over:
            return

        # 获取按键状态
        keys = pygame.key.get_pressed()

        # 更新挡板
        velocity_x = self.paddle.handle_input(keys)
        self.paddle.update(velocity_x, self.width)

        # 更新球的生成
        self.ball_timer += 1
        if self.ball_timer >= self.ball_interval:
            self.spawn_ball()
            self.ball_timer = 0

            # 每5个球增加难度
            if len(self.balls) % 5 == 0:
                self.difficulty += 0.5
                if self.ball_interval > 30:
                    self.ball_interval -= 2

        # 更新所有球
        paddle_rect = self.paddle.get_rect()
        for ball in self.balls:
            ball.update()

            # 检测与挡板的碰撞
            if ball.check_collision(paddle_rect):
                self.score += 10

            # 检测是否落出屏幕
            if ball.active and ball.is_off_screen(self.height):
                ball.active = False
                self.lives -= 1
                if self.lives <= 0:
                    self.game_over = True

        # 移除不活跃的球
        self.balls = [ball for ball in self.balls if ball.active]

    def draw(self):
        """绘制游戏画面"""
        # 清屏
        self.screen.fill(WHITE)

        # 绘制所有球
        for ball in self.balls:
            ball.draw(self.screen)

        # 绘制挡板
        self.paddle.draw(self.screen)

        # 绘制分数
        score_text = self.font.render(f"Score: {self.score}", True, BLACK)
        self.screen.blit(score_text, (10, 10))

        # 绘制生命值
        lives_text = self.font.render(f"Lives: {self.lives}", True, RED)
        self.screen.blit(lives_text, (self.width - 150, 10))

        # 绘制难度
        diff_text = self.small_font.render(f"Level: {int(self.difficulty)}", True, (100, 100, 100))
        self.screen.blit(diff_text, (self.width // 2 - 40, 10))

        # 游戏结束画面
        if self.game_over:
            self.draw_game_over()

        pygame.display.flip()

    def draw_game_over(self):
        """绘制游戏结束画面"""
        # 半透明遮罩
        overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 128))
        self.screen.blit(overlay, (0, 0))

        # 游戏结束文字
        game_over_text = self.font.render("GAME OVER", True, RED)
        text_rect = game_over_text.get_rect(center=(self.width // 2, self.height // 2 - 50))
        self.screen.blit(game_over_text, text_rect)

        # 最终分数
        final_score = self.font.render(f"Final Score: {self.score}", True, WHITE)
        score_rect = final_score.get_rect(center=(self.width // 2, self.height // 2 + 10))
        self.screen.blit(final_score, score_rect)

        # 重新开始提示
        restart_text = self.small_font.render("Press SPACE to restart", True, WHITE)
        restart_rect = restart_text.get_rect(center=(self.width // 2, self.height // 2 + 60))
        self.screen.blit(restart_text, restart_rect)

    def run(self):
        """运行游戏主循环"""
        running = True

        while running:
            # 处理事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_SPACE:
                        if self.game_over:
                            self.reset_game()

            # 更新游戏
            self.update()

            # 绘制画面
            self.draw()

            # 控制帧率
            self.clock.tick(60)

        pygame.quit()
        sys.exit()


# ==================== 主函数 ====================
def main():
    """
    主函数 - 游戏入口
    """
    print("=" * 50)
    print("欢迎玩接球游戏！")
    print("=" * 50)
    print("控制方式：")
    print("  左右方向键或A/D键 - 移动挡板")
    print("  空格键 - 重新开始")
    print("  ESC - 退出游戏")
    print("=" * 50)
    print("目标：尽可能多地接住下落的球！")
    print("=" * 50)

    # 创建并运行游戏
    game = CatchBallGame(800, 600)
    game.run()


# 程序入口
if __name__ == "__main__":
    main()
