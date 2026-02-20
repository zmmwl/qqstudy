"""
太空射击 - 综合练习游戏
======================

游戏说明：
- 控制飞船左右移动
- 按空格键发射子弹
- 击落敌机得分
- 被敌机撞到或敌机突破防线游戏结束

知识点：
1. 多种游戏对象的管理
2. 子弹发射系统
3. 敌机生成和AI
4. 爆炸效果
5. 游戏难度递增

控制：
- 左右方向键或A/D键移动
- 空格键发射子弹
- R键重新开始
- ESC退出

作者：游戏开发速成教程
"""

import pygame
import sys
import random
import math

# ==================== 颜色常量 ====================
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 100, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
CYAN = (0, 255, 255)
PURPLE = (128, 0, 128)


# ==================== 飞船类 ====================
class Player:
    """
    玩家飞船类

    属性：
        x, y (float): 位置坐标
        width, height (int): 大小
        speed (float): 移动速度

    方法：
        handle_input(keys): 处理输入
        update(width): 更新位置
        draw(surface): 绘制飞船
        get_rect(): 获取碰撞区域
    """

    def __init__(self, x, y, width=50, height=40, speed=7):
        """
        初始化玩家飞船

        参数：
            x (float): 初始x坐标
            y (float): 初始y坐标
            width (int): 宽度，默认50
            height (int): 高度，默认40
            speed (float): 移动速度，默认7
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
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
        更新位置

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
        绘制飞船

        参数：
            surface (pygame.Surface): 绘制目标
        """
        # 飞船主体（三角形）
        points = [
            (self.x + self.width // 2, self.y),  # 顶点
            (self.x, self.y + self.height),      # 左下
            (self.x + self.width, self.y + self.height)  # 右下
        ]
        pygame.draw.polygon(surface, CYAN, points)

        # 飞船窗户
        pygame.draw.circle(surface, BLUE,
                          (int(self.x + self.width // 2),
                           int(self.y + self.height // 2)), 8)

        # 引擎火焰
        flame_height = random.randint(5, 15)
        flame_points = [
            (self.x + self.width // 4, self.y + self.height),
            (self.x + self.width // 2, self.y + self.height + flame_height),
            (self.x + self.width * 3 // 4, self.y + self.height)
        ]
        pygame.draw.polygon(surface, ORANGE, flame_points)

    def get_rect(self):
        """获取碰撞矩形"""
        return pygame.Rect(int(self.x), int(self.y), self.width, self.height)

    def get_gun_position(self):
        """获取枪口位置（用于发射子弹）"""
        return (self.x + self.width // 2, self.y)


# ==================== 子弹类 ====================
class Bullet:
    """
    子弹类

    属性：
        x, y (float): 位置坐标
        speed (float): 移动速度
        active (bool): 是否活跃

    方法：
        update(): 更新位置
        draw(surface): 绘制子弹
        is_off_screen(): 是否离开屏幕
    """

    def __init__(self, x, y, speed=10, color=YELLOW):
        """
        初始化子弹

        参数：
            x (float): 初始x坐标
            y (float): 初始y坐标
            speed (float): 移动速度，默认10
            color (tuple): 颜色，默认黄色
        """
        self.x = x
        self.y = y
        self.speed = speed
        self.color = color
        self.active = True
        self.width = 4
        self.height = 15

    def update(self):
        """更新位置（向上移动）"""
        self.y -= self.speed

    def draw(self, surface):
        """绘制子弹"""
        pygame.draw.rect(surface, self.color,
                        (int(self.x - self.width // 2),
                         int(self.y),
                         self.width, self.height))

        # 子弹光晕
        pygame.draw.circle(surface, WHITE, (int(self.x), int(self.y)), 3)

    def is_off_screen(self):
        """检测是否离开屏幕"""
        return self.y < 0

    def get_rect(self):
        """获取碰撞矩形"""
        return pygame.Rect(
            int(self.x - self.width // 2),
            int(self.y),
            self.width,
            self.height
        )


# ==================== 敌机类 ====================
class Enemy:
    """
    敌机类

    属性：
        x, y (float): 位置坐标
        width, height (int): 大小
        speed (float): 下落速度
        active (bool): 是否活跃

    方法：
        update(): 更新位置
        draw(surface): 绘制敌机
        is_off_screen(height): 是否突破防线
    """

    def __init__(self, x, y, width=40, height=35, speed=3):
        """
        初始化敌机

        参数：
            x (float): 初始x坐标
            y (float): 初始y坐标
            width (int): 宽度，默认40
            height (int): 高度，默认35
            speed (float): 下落速度，默认3
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.active = True
        self.color = RED

        # 随机选择敌机类型（影响外观）
        self.enemy_type = random.choice([1, 2, 3])

    def update(self):
        """更新位置（向下移动）"""
        self.y += self.speed

        # 某些敌机会左右摇摆
        if self.enemy_type == 2:
            self.x += math.sin(self.y * 0.05) * 2

    def draw(self, surface):
        """绘制敌机"""
        if self.enemy_type == 1:
            # 类型1：倒三角
            points = [
                (self.x + self.width // 2, self.y + self.height),
                (self.x, self.y),
                (self.x + self.width, self.y)
            ]
            pygame.draw.polygon(surface, self.color, points)
        elif self.enemy_type == 2:
            # 类型2：菱形
            points = [
                (self.x + self.width // 2, self.y),
                (self.x, self.y + self.height // 2),
                (self.x + self.width // 2, self.y + self.height),
                (self.x + self.width, self.y + self.height // 2)
            ]
            pygame.draw.polygon(surface, ORANGE, points)
        else:
            # 类型3：矩形加翅膀
            pygame.draw.rect(surface, PURPLE,
                           (int(self.x + 5), int(self.y),
                            self.width - 10, self.height))
            pygame.draw.rect(surface, PURPLE,
                           (int(self.x), int(self.y + 10),
                            self.width, self.height - 20))

    def is_off_screen(self, height):
        """检测是否突破防线"""
        return self.y > height

    def get_rect(self):
        """获取碰撞矩形"""
        return pygame.Rect(int(self.x), int(self.y), self.width, self.height)


# ==================== 爆炸效果类 ====================
class Explosion:
    """
    爆炸效果类

    属性：
        x, y (float): 位置坐标
        radius (int): 当前半径
        max_radius (int): 最大半径
        grow_speed (int): 扩展速度
        active (bool): 是否活跃

    方法：
        update(): 更新效果
        draw(surface): 绘制爆炸
    """

    def __init__(self, x, y, max_radius=30):
        """
        初始化爆炸效果

        参数：
            x (float): x坐标
            y (float): y坐标
            max_radius (int): 最大半径，默认30
        """
        self.x = x
        self.y = y
        self.radius = 5
        self.max_radius = max_radius
        self.grow_speed = 3
        self.active = True

    def update(self):
        """更新爆炸效果"""
        self.radius += self.grow_speed
        if self.radius >= self.max_radius:
            self.active = False

    def draw(self, surface):
        """绘制爆炸效果"""
        # 多层圆形，模拟爆炸
        alpha = int(255 * (1 - self.radius / self.max_radius))

        # 外圈（红色）
        if alpha > 0:
            pygame.draw.circle(surface, RED,
                             (int(self.x), int(self.y)),
                             self.radius, 3)

        # 中圈（橙色）
        if self.radius > 5:
            pygame.draw.circle(surface, ORANGE,
                             (int(self.x), int(self.y)),
                             self.radius - 5, 2)

        # 内圈（黄色）
        if self.radius > 10:
            pygame.draw.circle(surface, YELLOW,
                             (int(self.x), int(self.y)),
                             self.radius - 10, 2)


# ==================== 星星背景类 ====================
class Star:
    """
    背景星星类

    属性：
        x, y (float): 位置坐标
        speed (float): 下落速度
        size (int): 大小
    """

    def __init__(self, x, y, speed, size):
        self.x = x
        self.y = y
        self.speed = speed
        self.size = size

    def update(self, height):
        """更新位置"""
        self.y += self.speed
        if self.y > height:
            self.y = 0
            self.x = random.randint(0, 800)

    def draw(self, surface):
        """绘制星星"""
        pygame.draw.circle(surface, WHITE, (int(self.x), int(self.y)), self.size)


# ==================== 游戏类 ====================
class SpaceShooterGame:
    """
    太空射击游戏类 - 管理整个游戏
    """

    def __init__(self, width=800, height=600):
        """
        初始化游戏

        参数：
            width (int): 窗口宽度
            height (int): 窗口高度
        """
        self.width = width
        self.height = height

        # 初始化pygame
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("太空射击 - 方向键移动，空格射击，ESC退出")
        self.clock = pygame.time.Clock()

        # 创建字体
        self.font = pygame.font.Font(None, 48)
        self.small_font = pygame.font.Font(None, 32)

        # 创建背景星星
        self.stars = []
        for _ in range(50):
            x = random.randint(0, width)
            y = random.randint(0, height)
            speed = random.uniform(1, 3)
            size = random.randint(1, 2)
            self.stars.append(Star(x, y, speed, size))

        # 初始化游戏状态
        self.reset_game()

    def reset_game(self):
        """重置游戏状态"""
        # 创建玩家
        self.player = Player(
            x=self.width // 2 - 25,
            y=self.height - 60,
            width=50,
            height=40,
            speed=7
        )

        # 子弹列表
        self.bullets = []

        # 敌机列表
        self.enemies = []

        # 爆炸效果列表
        self.explosions = []

        # 游戏状态
        self.score = 0
        self.game_over = False

        # 射击冷却
        self.shoot_cooldown = 0
        self.shoot_delay = 10  # 射击间隔（帧数）

        # 敌机生成计时器
        self.enemy_timer = 0
        self.enemy_interval = 60  # 敌机生成间隔（帧数）

        # 难度
        self.difficulty = 1

    def shoot(self):
        """发射子弹"""
        if self.shoot_cooldown <= 0:
            gun_x, gun_y = self.player.get_gun_position()
            bullet = Bullet(gun_x, gun_y, speed=12, color=YELLOW)
            self.bullets.append(bullet)
            self.shoot_cooldown = self.shoot_delay

    def spawn_enemy(self):
        """生成敌机"""
        x = random.randint(0, self.width - 40)
        speed = 2 + self.difficulty * 0.5 + random.random()
        enemy = Enemy(x, -40, speed=speed)
        self.enemies.append(enemy)

    def update(self):
        """更新游戏状态"""
        if self.game_over:
            return

        # 获取按键状态
        keys = pygame.key.get_pressed()

        # 更新玩家
        velocity_x = self.player.handle_input(keys)
        self.player.update(velocity_x, self.width)

        # 射击（按住空格连续射击）
        if keys[pygame.K_SPACE]:
            self.shoot()

        # 更新射击冷却
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

        # 更新子弹
        for bullet in self.bullets:
            bullet.update()

        # 移除离开屏幕的子弹
        self.bullets = [b for b in self.bullets if not b.is_off_screen()]

        # 更新敌机生成
        self.enemy_timer += 1
        if self.enemy_timer >= self.enemy_interval:
            self.spawn_enemy()
            self.enemy_timer = 0

            # 每10个敌机增加难度
            if len(self.enemies) % 10 == 0:
                self.difficulty += 0.2
                if self.enemy_interval > 20:
                    self.enemy_interval -= 2

        # 更新敌机
        for enemy in self.enemies:
            enemy.update()

        # 检测敌机是否突破防线
        for enemy in self.enemies:
            if enemy.is_off_screen(self.height):
                self.game_over = True
                enemy.active = False

        # 检测子弹与敌机碰撞
        for bullet in self.bullets:
            for enemy in self.enemies:
                if bullet.active and enemy.active:
                    if bullet.get_rect().colliderect(enemy.get_rect()):
                        # 创建爆炸效果
                        explosion = Explosion(
                            enemy.x + enemy.width // 2,
                            enemy.y + enemy.height // 2
                        )
                        self.explosions.append(explosion)

                        bullet.active = False
                        enemy.active = False
                        self.score += 10

        # 检测玩家与敌机碰撞
        player_rect = self.player.get_rect()
        for enemy in self.enemies:
            if enemy.active and player_rect.colliderect(enemy.get_rect()):
                self.game_over = True
                explosion = Explosion(
                    self.player.x + self.player.width // 2,
                    self.player.y + self.player.height // 2,
                    max_radius=50
                )
                self.explosions.append(explosion)

        # 移除不活跃的对象
        self.bullets = [b for b in self.bullets if b.active]
        self.enemies = [e for e in self.enemies if e.active]

        # 更新爆炸效果
        for explosion in self.explosions:
            explosion.update()
        self.explosions = [e for e in self.explosions if e.active]

        # 更新背景星星
        for star in self.stars:
            star.update(self.height)

    def draw(self):
        """绘制游戏画面"""
        # 清屏（黑色背景）
        self.screen.fill(BLACK)

        # 绘制背景星星
        for star in self.stars:
            star.draw(self.screen)

        # 绘制子弹
        for bullet in self.bullets:
            bullet.draw(self.screen)

        # 绘制敌机
        for enemy in self.enemies:
            enemy.draw(self.screen)

        # 绘制玩家（如果游戏没有结束）
        if not self.game_over:
            self.player.draw(self.screen)

        # 绘制爆炸效果
        for explosion in self.explosions:
            explosion.draw(self.screen)

        # 绘制分数
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))

        # 绘制难度
        diff_text = self.small_font.render(f"Level: {int(self.difficulty)}", True, (150, 150, 150))
        self.screen.blit(diff_text, (10, 50))

        # 游戏结束画面
        if self.game_over:
            self.draw_game_over()

        pygame.display.flip()

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

        # 重新开始提示
        restart_text = self.small_font.render("Press R to restart", True, WHITE)
        restart_rect = restart_text.get_rect(center=(self.width // 2, self.height // 2 + 70))
        self.screen.blit(restart_text, restart_rect)

    def handle_input(self):
        """处理输入"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False

                elif event.key == pygame.K_r:
                    if self.game_over:
                        self.reset_game()

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
    print("欢迎玩太空射击！")
    print("=" * 50)
    print("控制方式：")
    print("  左右方向键或A/D - 移动飞船")
    print("  空格键 - 发射子弹")
    print("  R键 - 重新开始")
    print("  ESC - 退出游戏")
    print("=" * 50)
    print("目标：击落敌机得分，不要被撞到或让敌机突破防线！")
    print("=" * 50)

    # 创建并运行游戏
    game = SpaceShooterGame(800, 600)
    game.run()


# 程序入口
if __name__ == "__main__":
    main()
