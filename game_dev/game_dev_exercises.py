"""
游戏开发练习题 - 带答案
======================

这个文件包含了游戏开发教程的练习题，帮助巩固所学知识。
每道题都有难度标记和参考答案。

练习题编号规则：
- 第1位：对应教程章节（2-8）
- 第2-3位：题目序号

例如：201 表示第2节的第1题

作者：游戏开发速成教程
"""

import pygame
import sys
import math
import random

# ==================== 颜色常量 ====================
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


# ============================================================================
# 第2节练习：创建游戏窗口
# ============================================================================

def exercise_201():
    """
    练习201（难度：简单）

    任务：创建一个800x600的窗口，背景色为浅蓝色（173, 216, 230）
    窗口标题为"我的练习窗口"
    程序运行5秒后自动关闭

    提示：
    1. 使用 pygame.time.get_ticks() 获取当前时间（毫秒）
    2. 计算5秒 = 5000毫秒
    """

    # ========== 参考答案 ==========
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("我的练习窗口")
    clock = pygame.time.Clock()

    start_time = pygame.time.get_ticks()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 检查是否超过5秒
        if pygame.time.get_ticks() - start_time >= 5000:
            running = False

        screen.fill((173, 216, 230))  # 浅蓝色
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


def exercise_202():
    """
    练习202（难度：中等）

    任务：创建一个可以改变背景色的窗口
    - 按R键：背景变红
    - 按G键：背景变绿
    - 按B键：背景变蓝
    - 按W键：背景变白
    """

    # ========== 参考答案 ==========
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("改变背景色 - R/G/B/W")
    clock = pygame.time.Clock()

    current_color = WHITE

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r:
                    current_color = RED
                elif event.key == pygame.K_g:
                    current_color = GREEN
                elif event.key == pygame.K_b:
                    current_color = BLUE
                elif event.key == pygame.K_w:
                    current_color = WHITE

        screen.fill(current_color)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


# ============================================================================
# 第3节练习：绘制图形
# ============================================================================

def exercise_301():
    """
    练习301（难度：简单）

    任务：绘制一个简单的房子
    - 房子主体：橙色矩形
    - 屋顶：红色三角形
    - 门：棕色矩形
    - 窗户：两个青色小正方形
    """

    # ========== 参考答案 ==========
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("绘制房子")
    clock = pygame.time.Clock()

    # 颜色定义
    ORANGE = (255, 165, 0)
    BROWN = (139, 69, 19)
    CYAN = (0, 255, 255)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill(WHITE)

        # 房子主体
        pygame.draw.rect(screen, ORANGE, (300, 300, 200, 150))

        # 屋顶
        roof_points = [(280, 300), (400, 200), (520, 300)]
        pygame.draw.polygon(screen, RED, roof_points)

        # 门
        pygame.draw.rect(screen, BROWN, (370, 350, 40, 100))

        # 窗户
        pygame.draw.rect(screen, CYAN, (320, 330, 35, 35))
        pygame.draw.rect(screen, CYAN, (445, 330, 35, 35))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


def exercise_302():
    """
    练习302（难度：中等）

    任务：绘制一个正在闪烁的彩色圆形
    - 圆在屏幕中央
    - 颜色在红、绿、蓝之间循环变化（每0.5秒换一次）

    提示：
    1. 使用颜色列表
    2. 用帧计数器或时间来控制切换
    """

    # ========== 参考答案 ==========
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("闪烁的圆形")
    clock = pygame.time.Clock()

    colors = [RED, GREEN, BLUE, YELLOW, (255, 165, 0)]  # 颜色列表
    current_color_index = 0
    timer = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # 每30帧（0.5秒）换一个颜色
        timer += 1
        if timer >= 30:
            timer = 0
            current_color_index = (current_color_index + 1) % len(colors)

        screen.fill(WHITE)
        pygame.draw.circle(screen, colors[current_color_index], (400, 300), 80)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


def exercise_303():
    """
    练习303（难度：中等）

    任务：绘制一个带分数显示的计分板
    - 显示"Score: 0"格式的文字
    - 按空格键分数+10
    - 按R键重置为0

    提示：
    1. 使用pygame.font.Font()创建字体
    2. 每次分数改变后重新渲染文字
    """

    # ========== 参考答案 ==========
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("计分板 - 空格加分，R重置")
    clock = pygame.time.Clock()

    font = pygame.font.Font(None, 72)
    score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    score += 10
                elif event.key == pygame.K_r:
                    score = 0

        screen.fill(WHITE)

        # 渲染分数文字
        score_text = font.render(f"Score: {score}", True, BLACK)
        text_rect = score_text.get_rect(center=(400, 300))
        screen.blit(score_text, text_rect)

        # 提示文字
        hint_font = pygame.font.Font(None, 36)
        hint = hint_font.render("SPACE: +10  R: Reset  ESC: Exit", True, (128, 128, 128))
        screen.blit(hint, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


# ============================================================================
# 第4节练习：处理事件
# ============================================================================

def exercise_401():
    """
    练习401（难度：简单）

    任务：创建一个可以用鼠标拖动的方块
    - 当鼠标左键按住方块时，方块跟随鼠标移动

    提示：
    1. 使用 event.pos 获取鼠标位置
    2. 检测鼠标是否在方块内部
    """

    # ========== 参考答案 ==========
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("鼠标拖动方块")
    clock = pygame.time.Clock()

    rect_x, rect_y = 375, 275
    rect_width, rect_height = 50, 50
    dragging = False
    offset_x, offset_y = 0, 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # 左键
                    # 检测是否点击到方块
                    if (rect_x <= event.pos[0] <= rect_x + rect_width and
                        rect_y <= event.pos[1] <= rect_y + rect_height):
                        dragging = True
                        offset_x = rect_x - event.pos[0]
                        offset_y = rect_y - event.pos[1]
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    dragging = False
            elif event.type == pygame.MOUSEMOTION:
                if dragging:
                    rect_x = event.pos[0] + offset_x
                    rect_y = event.pos[1] + offset_y

        screen.fill(WHITE)
        pygame.draw.rect(screen, BLUE, (rect_x, rect_y, rect_width, rect_height))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


def exercise_402():
    """
    练习402（难度：中等）

    任务：创建一个可以用键盘控制大小的圆形
    - 方向键上/下：调整半径（+/- 5像素）
    - 方向键左/右：改变颜色（在红、绿、蓝之间切换）
    - 显示当前半径和颜色名称
    """

    # ========== 参考答案 ==========
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("调整圆形 - 方向键控制")
    clock = pygame.time.Clock()

    colors = {"Red": RED, "Green": GREEN, "Blue": BLUE}
    color_names = list(colors.keys())
    current_color = 0
    radius = 50

    font = pygame.font.Font(None, 36)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_UP:
                    radius = min(radius + 5, 200)  # 最大200
                elif event.key == pygame.K_DOWN:
                    radius = max(radius - 5, 10)  # 最小10
                elif event.key == pygame.K_LEFT:
                    current_color = (current_color - 1) % len(color_names)
                elif event.key == pygame.K_RIGHT:
                    current_color = (current_color + 1) % len(color_names)

        screen.fill(WHITE)

        # 绘制圆形
        pygame.draw.circle(screen, colors[color_names[current_color]],
                          (400, 300), radius)

        # 显示信息
        info1 = font.render(f"Radius: {radius}", True, BLACK)
        info2 = font.render(f"Color: {color_names[current_color]}", True, BLACK)
        hint = font.render("UP/DOWN: Size  LEFT/RIGHT: Color  ESC: Exit", True, (128, 128, 128))

        screen.blit(info1, (10, 10))
        screen.blit(info2, (10, 50))
        screen.blit(hint, (10, 560))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


# ============================================================================
# 第5节练习：让物体动起来
# ============================================================================

def exercise_501():
    """
    练习501（难度：简单）

    任务：让一个方块从屏幕左边移动到右边
    - 到达右边界后，从左边重新出现
    - 类似走马灯效果
    """

    # ========== 参考答案 ==========
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("移动的方块")
    clock = pygame.time.Clock()

    rect_x = 0
    rect_width = 50
    speed = 5

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # 更新位置
        rect_x += speed

        # 到达右边界后从左边重新出现
        if rect_x > 800:
            rect_x = -rect_width

        screen.fill(WHITE)
        pygame.draw.rect(screen, BLUE, (rect_x, 275, rect_width, 50))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


def exercise_502():
    """
    练习502（难度：中等）

    任务：让一个小球做圆周运动
    - 小球沿着圆形轨道移动
    - 可以用方向键上/下调整圆周运动速度

    提示：
    1. 圆周运动的公式：
       x = 圆心x + 半径 * cos(角度)
       y = 圆心y + 半径 * sin(角度)
    2. 角度需要不断增加
    """

    # ========== 参考答案 ==========
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("圆周运动")
    clock = pygame.time.Clock()

    center_x, center_y = 400, 300
    orbit_radius = 150
    ball_radius = 20
    angle = 0
    angle_speed = 0.05  # 角度变化速度

    font = pygame.font.Font(None, 36)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # 获取按键状态调整速度
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            angle_speed += 0.005
        if keys[pygame.K_DOWN]:
            angle_speed = max(0.005, angle_speed - 0.005)

        # 更新角度
        angle += angle_speed

        # 计算小球位置（圆周运动）
        ball_x = center_x + orbit_radius * math.cos(angle)
        ball_y = center_y + orbit_radius * math.sin(angle)

        screen.fill(WHITE)

        # 绘制轨道
        pygame.draw.circle(screen, (200, 200, 200), (center_x, center_y), orbit_radius, 1)

        # 绘制中心点
        pygame.draw.circle(screen, BLACK, (center_x, center_y), 5)

        # 绘制小球
        pygame.draw.circle(screen, RED, (int(ball_x), int(ball_y)), ball_radius)

        # 显示速度
        speed_text = font.render(f"Speed: {angle_speed:.3f}", True, BLACK)
        screen.blit(speed_text, (10, 10))

        hint = font.render("UP/DOWN: Adjust Speed  ESC: Exit", True, (128, 128, 128))
        screen.blit(hint, (10, 560))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


# ============================================================================
# 第6节练习：碰撞检测
# ============================================================================

def exercise_601():
    """
    练习601（难度：中等）

    任务：创建一个简单的收集游戏
    - 玩家控制一个方块移动
    - 屏幕上有多个随机位置的"金币"（黄色圆形）
    - 玩家碰到金币后金币消失，分数+10
    - 收集完所有金币后显示"你赢了！"

    提示：
    1. 使用列表存储金币
    2. 碰撞后从列表移除金币
    """

    # ========== 参考答案 ==========
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("收集金币")
    clock = pygame.time.Clock()

    # 玩家
    player_x, player_y = 100, 100
    player_size = 40
    player_speed = 5

    # 金币列表 [(x, y), ...]
    coins = []
    for _ in range(10):
        x = random.randint(50, 750)
        y = random.randint(50, 550)
        coins.append([x, y])

    score = 0
    font = pygame.font.Font(None, 36)

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
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player_x += player_speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player_y -= player_speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player_y += player_speed

        # 边界限制
        player_x = max(0, min(player_x, 800 - player_size))
        player_y = max(0, min(player_y, 600 - player_size))

        # 碰撞检测
        player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
        for coin in coins[:]:  # 使用切片复制列表，避免修改时出问题
            # 简化：把圆形当作正方形检测
            coin_rect = pygame.Rect(coin[0] - 15, coin[1] - 15, 30, 30)
            if player_rect.colliderect(coin_rect):
                coins.remove(coin)
                score += 10

        # 绘制
        screen.fill(WHITE)

        # 绘制金币
        for coin in coins:
            pygame.draw.circle(screen, YELLOW, coin, 15)
            pygame.draw.circle(screen, (200, 200, 0), coin, 15, 2)

        # 绘制玩家
        pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))

        # 显示分数
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        # 剩余金币
        remaining = font.render(f"Coins: {len(coins)}", True, BLACK)
        screen.blit(remaining, (10, 50))

        # 胜利检测
        if len(coins) == 0:
            win_text = font.render("YOU WIN! Press ESC to exit", True, GREEN)
            screen.blit(win_text, (250, 280))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


# ============================================================================
# 综合练习
# ============================================================================

def exercise_final():
    """
    综合练习（难度：困难）

    任务：创建一个简单的躲避游戏
    - 玩家控制一个角色在屏幕底部左右移动
    - 从屏幕顶部随机掉落障碍物
    - 玩家被障碍物碰到就游戏结束
    - 显示存活时间和躲避的障碍物数量

    这个练习综合运用了：
    1. 游戏窗口创建
    2. 图形绘制
    3. 事件处理
    4. 物体移动
    5. 碰撞检测
    """

    # ========== 参考答案 ==========
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("躲避游戏 - 方向键移动，ESC退出")
    clock = pygame.time.Clock()

    # 玩家
    player_x = 375
    player_y = 530
    player_width, player_height = 50, 50
    player_speed = 7

    # 障碍物列表
    obstacles = []
    spawn_timer = 0
    spawn_delay = 40  # 生成间隔（帧）

    # 游戏状态
    game_over = False
    start_time = pygame.time.get_ticks()
    dodge_count = 0

    font = pygame.font.Font(None, 48)
    small_font = pygame.font.Font(None, 32)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r and game_over:
                    # 重新开始
                    player_x = 375
                    obstacles.clear()
                    game_over = False
                    start_time = pygame.time.get_ticks()
                    dodge_count = 0
                    spawn_delay = 40

        if not game_over:
            # 获取按键状态
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                player_x -= player_speed
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                player_x += player_speed

            # 边界限制
            player_x = max(0, min(player_x, 800 - player_width))

            # 生成障碍物
            spawn_timer += 1
            if spawn_timer >= spawn_delay:
                spawn_timer = 0
                obs_x = random.randint(0, 750)
                obs_speed = random.uniform(3, 7)
                obstacles.append({
                    'x': obs_x,
                    'y': -50,
                    'width': 50,
                    'height': 50,
                    'speed': obs_speed
                })

            # 更新障碍物
            for obs in obstacles[:]:
                obs['y'] += obs['speed']

                # 检测是否通过屏幕
                if obs['y'] > 600:
                    obstacles.remove(obs)
                    dodge_count += 1

            # 碰撞检测
            player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
            for obs in obstacles:
                obs_rect = pygame.Rect(obs['x'], obs['y'], obs['width'], obs['height'])
                if player_rect.colliderect(obs_rect):
                    game_over = True
                    break

            # 逐渐增加难度
            if dodge_count > 0 and dodge_count % 5 == 0 and spawn_delay > 15:
                spawn_delay -= 1

        # 绘制
        screen.fill(WHITE)

        # 绘制障碍物
        for obs in obstacles:
            pygame.draw.rect(screen, RED,
                           (obs['x'], obs['y'], obs['width'], obs['height']))

        # 绘制玩家
        pygame.draw.rect(screen, BLUE,
                        (player_x, player_y, player_width, player_height))

        # 计算存活时间
        if game_over:
            survive_time = (pygame.time.get_ticks() - start_time) // 1000
        else:
            survive_time = (pygame.time.get_ticks() - start_time) // 1000

        # 显示信息
        time_text = small_font.render(f"Time: {survive_time}s", True, BLACK)
        screen.blit(time_text, (10, 10))

        dodge_text = small_font.render(f"Dodged: {dodge_count}", True, BLACK)
        screen.blit(dodge_text, (10, 40))

        # 游戏结束画面
        if game_over:
            overlay = pygame.Surface((800, 600), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 128))
            screen.blit(overlay, (0, 0))

            game_over_text = font.render("GAME OVER", True, RED)
            text_rect = game_over_text.get_rect(center=(400, 250))
            screen.blit(game_over_text, text_rect)

            final_text = font.render(f"Time: {survive_time}s  Dodged: {dodge_count}", True, WHITE)
            final_rect = final_text.get_rect(center=(400, 320))
            screen.blit(final_text, final_rect)

            restart_text = small_font.render("Press R to restart", True, WHITE)
            restart_rect = restart_text.get_rect(center=(400, 380))
            screen.blit(restart_text, restart_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


# ============================================================================
# 练习菜单
# ============================================================================

def show_exercise_menu():
    """显示练习题菜单"""
    print("\n" + "=" * 60)
    print("           游戏开发练习题")
    print("=" * 60)
    print("\n第2节练习：创建游戏窗口")
    print("  201 - 创建浅蓝色窗口（简单）")
    print("  202 - 可改变背景色的窗口（中等）")
    print("\n第3节练习：绘制图形")
    print("  301 - 绘制房子（简单）")
    print("  302 - 闪烁的圆形（中等）")
    print("  303 - 计分板（中等）")
    print("\n第4节练习：处理事件")
    print("  401 - 鼠标拖动方块（简单）")
    print("  402 - 键盘控制圆形（中等）")
    print("\n第5节练习：让物体动起来")
    print("  501 - 走马灯方块（简单）")
    print("  502 - 圆周运动（中等）")
    print("\n第6节练习：碰撞检测")
    print("  601 - 收集金币游戏（中等）")
    print("\n综合练习")
    print("  99 - 躲避游戏（困难）")
    print("\n  0 - 退出")
    print("=" * 60)


def run_exercise(exercise_num):
    """运行指定的练习题"""
    exercises = {
        201: exercise_201,
        202: exercise_202,
        301: exercise_301,
        302: exercise_302,
        303: exercise_303,
        401: exercise_401,
        402: exercise_402,
        501: exercise_501,
        502: exercise_502,
        601: exercise_601,
        99: exercise_final,
    }

    if exercise_num in exercises:
        print(f"\n运行练习 {exercise_num}...")
        print("按ESC键退出练习")
        exercises[exercise_num]()
    else:
        print("无效的练习编号！")


def main():
    """主函数"""
    print("""
    ╔════════════════════════════════════════════════════════════╗
    ║                  游戏开发练习题                             ║
    ╠════════════════════════════════════════════════════════════╣
    ║  通过这些练习来巩固你所学的知识！                           ║
    ║  每道题都有参考答案，可以对照学习。                         ║
    ╚════════════════════════════════════════════════════════════╝
    """)

    while True:
        show_exercise_menu()
        try:
            choice = int(input("请选择练习题编号: "))
            if choice == 0:
                print("\n再见！\n")
                break
            run_exercise(choice)
        except ValueError:
            print("请输入有效的数字！")
        except Exception as e:
            print(f"发生错误: {e}")


if __name__ == "__main__":
    main()
