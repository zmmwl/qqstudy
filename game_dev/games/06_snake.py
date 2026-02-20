"""
贪吃蛇 - 经典游戏
================

游戏说明：
- 控制蛇移动，吃掉食物
- 每吃一个食物，蛇身体变长
- 撞到墙壁或自己身体游戏结束

知识点：
1. 网格移动
2. 蛇身体的数据结构（列表）
3. 碰撞检测
4. 游戏状态管理

控制：
- 方向键或WASD控制方向
- 空格键暂停/继续
- R键重新开始
- ESC退出

作者：游戏开发速成教程
"""

import pygame
import sys
import random
from collections import deque

# ==================== 颜色常量 ====================
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 180, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)
LIGHT_GRAY = (200, 200, 200)


# ==================== 方向常量 ====================
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


# ==================== 蛇类 ====================
class Snake:
    """
    蛇类 - 玩家控制的主角

    属性：
        body (deque): 蛇身体的坐标列表（使用双端队列）
        direction (tuple): 当前移动方向
        next_direction (tuple): 下一帧的方向（防止快速按键导致反向）
        grid_size (int): 每个格子的大小
        color (tuple): 蛇身体颜色
        head_color (tuple): 蛇头颜色

    方法：
        change_direction(new_dir): 改变方向
        update(): 更新蛇的位置
        grow(): 增长蛇身
        check_self_collision(): 检测自身碰撞
        check_wall_collision(width, height): 检测墙壁碰撞
        draw(surface): 绘制蛇
    """

    def __init__(self, start_x, start_y, grid_size=20, length=3):
        """
        初始化蛇

        参数：
            start_x (int): 起始x坐标（格子数）
            start_y (int): 起始y坐标（格子数）
            grid_size (int): 格子大小，默认20
            length (int): 初始长度，默认3

        示例：
            snake = Snake(10, 10)  # 在(10, 10)位置创建蛇
        """
        self.grid_size = grid_size
        self.color = GREEN
        self.head_color = DARK_GREEN

        # 使用deque（双端队列）存储蛇身体
        # 初始蛇身：连续的几个格子
        self.body = deque()
        for i in range(length):
            self.body.append((start_x - i, start_y))

        # 初始方向向右
        self.direction = RIGHT
        self.next_direction = RIGHT

        # 是否需要增长
        self.should_grow = False

    def change_direction(self, new_direction):
        """
        改变移动方向

        参数：
            new_direction (tuple): 新方向 (dx, dy)

        注意：不能直接反向移动（例如向右移动时不能直接向左）
        """
        # 计算新方向与当前方向是否相反
        dx, dy = new_direction
        current_dx, current_dy = self.direction

        # 如果不是反方向，则允许改变
        if (dx, dy) != (-current_dx, -current_dy):
            self.next_direction = new_direction

    def update(self):
        """
        更新蛇的位置

        原理：
        1. 在头部方向添加新格子
        2. 如果没有吃到食物，移除尾部格子
        3. 如果吃到食物，不移除尾部（蛇变长）
        """
        # 应用新方向
        self.direction = self.next_direction

        # 计算新头部位置
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)

        # 在头部添加新格子
        self.body.appendleft(new_head)

        # 如果不需要增长，移除尾部
        if not self.should_grow:
            self.body.pop()
        else:
            self.should_grow = False

    def grow(self):
        """
        蛇身增长

        设置标志，下一帧更新时不会移除尾部
        """
        self.should_grow = True

    def get_head(self):
        """获取蛇头位置"""
        return self.body[0]

    def check_self_collision(self):
        """
        检测是否撞到自己

        返回：
            bool: 是否发生自身碰撞
        """
        head = self.body[0]
        # 如果蛇头在身体其他部分出现，说明撞到了自己
        return head in list(self.body)[1:]

    def check_wall_collision(self, grid_width, grid_height):
        """
        检测是否撞墙

        参数：
            grid_width (int): 格子宽度数量
            grid_height (int): 格子高度数量

        返回：
            bool: 是否发生墙壁碰撞
        """
        head_x, head_y = self.body[0]
        return (head_x < 0 or head_x >= grid_width or
                head_y < 0 or head_y >= grid_height)

    def draw(self, surface):
        """
        绘制蛇

        参数：
            surface (pygame.Surface): 绘制目标
        """
        for i, (x, y) in enumerate(self.body):
            # 计算像素位置
            rect = pygame.Rect(
                x * self.grid_size,
                y * self.grid_size,
                self.grid_size - 1,  # 留1像素间隙
                self.grid_size - 1
            )

            # 蛇头用不同颜色
            if i == 0:
                pygame.draw.rect(surface, self.head_color, rect)
                # 画眼睛
                eye_size = 4
                eye_offset = self.grid_size // 4
                # 根据方向画眼睛
                if self.direction == RIGHT:
                    pygame.draw.circle(surface, WHITE,
                                      (rect.right - eye_offset, rect.centery - 3), eye_size)
                    pygame.draw.circle(surface, WHITE,
                                      (rect.right - eye_offset, rect.centery + 3), eye_size)
                elif self.direction == LEFT:
                    pygame.draw.circle(surface, WHITE,
                                      (rect.left + eye_offset, rect.centery - 3), eye_size)
                    pygame.draw.circle(surface, WHITE,
                                      (rect.left + eye_offset, rect.centery + 3), eye_size)
                elif self.direction == UP:
                    pygame.draw.circle(surface, WHITE,
                                      (rect.centerx - 3, rect.top + eye_offset), eye_size)
                    pygame.draw.circle(surface, WHITE,
                                      (rect.centerx + 3, rect.top + eye_offset), eye_size)
                else:  # DOWN
                    pygame.draw.circle(surface, WHITE,
                                      (rect.centerx - 3, rect.bottom - eye_offset), eye_size)
                    pygame.draw.circle(surface, WHITE,
                                      (rect.centerx + 3, rect.bottom - eye_offset), eye_size)
            else:
                pygame.draw.rect(surface, self.color, rect)


# ==================== 食物类 ====================
class Food:
    """
    食物类 - 蛇需要吃的东西
    """

    def __init__(self, grid_size=20):
        """
        初始化食物

        参数：
            grid_size (int): 格子大小
        """
        self.grid_size = grid_size
        self.x = 0
        self.y = 0
        self.color = RED

    def spawn(self, snake_body, grid_width, grid_height):
        """
        在随机位置生成食物（避开蛇身）

        参数：
            snake_body (deque): 蛇身体坐标
            grid_width (int): 格子宽度
            grid_height (int): 格子高度
        """
        while True:
            self.x = random.randint(0, grid_width - 1)
            self.y = random.randint(0, grid_height - 1)

            # 确保食物不在蛇身上
            if (self.x, self.y) not in snake_body:
                break

    def get_position(self):
        """获取食物位置"""
        return (self.x, self.y)

    def draw(self, surface):
        """
        绘制食物

        参数：
            surface (pygame.Surface): 绘制目标
        """
        # 绘制苹果形状
        center_x = self.x * self.grid_size + self.grid_size // 2
        center_y = self.y * self.grid_size + self.grid_size // 2
        radius = self.grid_size // 2 - 2

        # 主体
        pygame.draw.circle(surface, self.color, (center_x, center_y), radius)

        # 叶子
        pygame.draw.ellipse(surface, DARK_GREEN,
                           (center_x, center_y - radius - 5, 6, 8))

        # 高光
        pygame.draw.circle(surface, WHITE,
                          (center_x - 3, center_y - 3), 3)


# ==================== 游戏类 ====================
class SnakeGame:
    """
    贪吃蛇游戏类 - 管理整个游戏
    """

    def __init__(self, width=800, height=600, grid_size=20):
        """
        初始化游戏

        参数：
            width (int): 窗口宽度
            height (int): 窗口高度
            grid_size (int): 格子大小
        """
        self.width = width
        self.height = height
        self.grid_size = grid_size

        # 计算格子数量
        self.grid_width = width // grid_size
        self.grid_height = height // grid_size

        # 初始化pygame
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("贪吃蛇 - 方向键控制，空格暂停，ESC退出")
        self.clock = pygame.time.Clock()

        # 创建字体
        self.font = pygame.font.Font(None, 48)
        self.small_font = pygame.font.Font(None, 32)

        # 游戏状态
        self.reset_game()

    def reset_game(self):
        """重置游戏状态"""
        # 创建蛇（在中间位置）
        start_x = self.grid_width // 2
        start_y = self.grid_height // 2
        self.snake = Snake(start_x, start_y, self.grid_size, length=3)

        # 创建食物
        self.food = Food(self.grid_size)
        self.food.spawn(self.snake.body, self.grid_width, self.grid_height)

        # 游戏状态
        self.score = 0
        self.game_over = False
        self.paused = False

        # 移动计时器（控制蛇的移动速度）
        self.move_timer = 0
        self.move_delay = 8  # 每8帧移动一次（可调整难度）

        # 速度（分数越高越快）
        self.base_speed = 8
        self.current_speed = self.base_speed

    def update(self):
        """更新游戏状态"""
        if self.game_over or self.paused:
            return

        # 更新移动计时器
        self.move_timer += 1

        # 根据移动延迟更新蛇的位置
        if self.move_timer >= self.move_delay:
            self.move_timer = 0

            # 更新蛇的位置
            self.snake.update()

            # 检测是否吃到食物
            if self.snake.get_head() == self.food.get_position():
                self.snake.grow()
                self.score += 10
                self.food.spawn(self.snake.body, self.grid_width, self.grid_height)

                # 每50分加速一次
                if self.score % 50 == 0 and self.move_delay > 3:
                    self.move_delay -= 1

            # 检测碰撞
            if (self.snake.check_self_collision() or
                self.snake.check_wall_collision(self.grid_width, self.grid_height)):
                self.game_over = True

    def draw(self):
        """绘制游戏画面"""
        # 清屏（深色背景）
        self.screen.fill((30, 30, 30))

        # 绘制网格线（可选，帮助看清格子）
        self.draw_grid()

        # 绘制食物
        self.food.draw(self.screen)

        # 绘制蛇
        self.snake.draw(self.screen)

        # 绘制分数
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))

        # 绘制蛇长度
        length_text = self.small_font.render(f"Length: {len(self.snake.body)}", True, LIGHT_GRAY)
        self.screen.blit(length_text, (10, 50))

        # 暂停画面
        if self.paused:
            self.draw_paused()

        # 游戏结束画面
        if self.game_over:
            self.draw_game_over()

        pygame.display.flip()

    def draw_grid(self):
        """绘制背景网格"""
        for x in range(0, self.width, self.grid_size):
            pygame.draw.line(self.screen, (40, 40, 40), (x, 0), (x, self.height))
        for y in range(0, self.height, self.grid_size):
            pygame.draw.line(self.screen, (40, 40, 40), (0, y), (self.width, y))

    def draw_paused(self):
        """绘制暂停画面"""
        # 半透明遮罩
        overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 128))
        self.screen.blit(overlay, (0, 0))

        # 暂停文字
        pause_text = self.font.render("PAUSED", True, YELLOW)
        text_rect = pause_text.get_rect(center=(self.width // 2, self.height // 2))
        self.screen.blit(pause_text, text_rect)

        hint_text = self.small_font.render("Press SPACE to continue", True, WHITE)
        hint_rect = hint_text.get_rect(center=(self.width // 2, self.height // 2 + 50))
        self.screen.blit(hint_text, hint_rect)

    def draw_game_over(self):
        """绘制游戏结束画面"""
        # 半透明遮罩
        overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        self.screen.blit(overlay, (0, 0))

        # 游戏结束文字
        game_over_text = self.font.render("GAME OVER", True, RED)
        text_rect = game_over_text.get_rect(center=(self.width // 2, self.height // 2 - 50))
        self.screen.blit(game_over_text, text_rect)

        # 最终分数
        final_score = self.font.render(f"Final Score: {self.score}", True, WHITE)
        score_rect = final_score.get_rect(center=(self.width // 2, self.height // 2 + 10))
        self.screen.blit(final_score, score_rect)

        # 蛇长度
        length_text = self.small_font.render(f"Snake Length: {len(self.snake.body)}", True, LIGHT_GRAY)
        length_rect = length_text.get_rect(center=(self.width // 2, self.height // 2 + 50))
        self.screen.blit(length_text, length_rect)

        # 重新开始提示
        restart_text = self.small_font.render("Press R to restart", True, WHITE)
        restart_rect = restart_text.get_rect(center=(self.width // 2, self.height // 2 + 100))
        self.screen.blit(restart_text, restart_rect)

    def handle_input(self):
        """处理输入"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False

                elif event.key == pygame.K_SPACE:
                    if not self.game_over:
                        self.paused = not self.paused

                elif event.key == pygame.K_r:
                    if self.game_over:
                        self.reset_game()

                # 方向控制（只有游戏运行时才能改变方向）
                if not self.game_over and not self.paused:
                    if event.key in (pygame.K_UP, pygame.K_w):
                        self.snake.change_direction(UP)
                    elif event.key in (pygame.K_DOWN, pygame.K_s):
                        self.snake.change_direction(DOWN)
                    elif event.key in (pygame.K_LEFT, pygame.K_a):
                        self.snake.change_direction(LEFT)
                    elif event.key in (pygame.K_RIGHT, pygame.K_d):
                        self.snake.change_direction(RIGHT)

        return True

    def run(self):
        """运行游戏主循环"""
        running = True

        while running:
            # 处理输入
            running = self.handle_input()

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
    print("欢迎玩贪吃蛇！")
    print("=" * 50)
    print("控制方式：")
    print("  方向键或WASD - 控制蛇的移动方向")
    print("  空格键 - 暂停/继续游戏")
    print("  R键 - 重新开始")
    print("  ESC - 退出游戏")
    print("=" * 50)
    print("目标：吃掉食物，让蛇变长，不要撞墙或撞到自己！")
    print("=" * 50)

    # 创建并运行游戏
    game = SnakeGame(800, 600, 20)
    game.run()


# 程序入口
if __name__ == "__main__":
    main()
