"""
游戏开发速成教程 - 主教程
========================

这是一个为初中生设计的游戏开发速成教程，使用pygame库。
教程分为8节，每节都有理论讲解和实际代码示例。

学习目标：
1. 理解游戏开发的基本概念
2. 掌握pygame的基本使用方法
3. 能够独立开发简单的小游戏

作者：游戏开发速成教程
"""

# ============================================================================
# 第1节：游戏开发入门
# ============================================================================
"""
【什么是游戏？】

从程序员的角度看，游戏就是一个不断循环的程序：
1. 获取玩家输入（键盘、鼠标等）
2. 更新游戏状态（位置、分数等）
3. 绘制画面（把游戏状态显示出来）

这个循环叫做"游戏循环"（Game Loop），是所有游戏的核心！


【什么是pygame？】

pygame是Python的一个游戏开发库，它提供了：
- 创建窗口和显示画面
- 绘制各种图形
- 处理键盘和鼠标输入
- 播放声音和音乐
- 检测碰撞


【安装pygame】

在命令行输入：
    pip install pygame

检查安装是否成功：
    python -c "import pygame; print(pygame.version.ver)"
"""

# ============================================================================
# 第2节：创建游戏窗口
# ============================================================================
"""
【游戏窗口的基本要素】

1. 窗口大小：宽度和高度（单位：像素）
2. 窗口标题：显示在窗口顶部的文字
3. 背景颜色：窗口的底色


【代码示例】
"""

import pygame
import sys


def lesson2_create_window():
    """
    第2节示例：创建一个基本的游戏窗口

    这是所有pygame程序的基本结构！
    """
    # 步骤1：初始化pygame
    pygame.init()

    # 步骤2：创建窗口
    # set_mode() 返回一个Surface对象，这是我们的"画布"
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # 步骤3：设置窗口标题
    pygame.display.set_caption("我的第一个游戏窗口")

    # 步骤4：创建时钟对象（用于控制帧率）
    clock = pygame.time.Clock()

    # 步骤5：游戏主循环
    running = True
    while running:
        # 5.1 处理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 5.2 更新游戏状态（这里暂时没有）

        # 5.3 绘制画面
        screen.fill((255, 255, 255))  # 白色背景
        pygame.display.flip()  # 更新显示

        # 5.4 控制帧率
        clock.tick(60)  # 60帧每秒

    # 步骤6：退出
    pygame.quit()
    sys.exit()


"""
【颜色的表示】

颜色用RGB值表示：(红, 绿, 蓝)
每个分量的范围是0-255

常用颜色：
- 黑色：(0, 0, 0)
- 白色：(255, 255, 255)
- 红色：(255, 0, 0)
- 绿色：(0, 255, 0)
- 蓝色：(0, 0, 255)
- 黄色：(255, 255, 0)  # 红+绿
- 青色：(0, 255, 255)  # 绿+蓝
- 紫色：(255, 0, 255)  # 红+蓝
"""

# ============================================================================
# 第3节：绘制图形
# ============================================================================
"""
【pygame的绑制函数】

pygame提供了多种绑制函数，都在pygame.draw模块中：
- rect(): 绘制矩形
- circle(): 绘制圆形
- line(): 绘制直线
- polygon(): 绘制多边形
- ellipse(): 绘制椭圆
- arc(): 绘制弧线


【代码示例】
"""


def lesson3_draw_shapes():
    """
    第3节示例：绘制各种图形
    """
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("绘制图形")
    clock = pygame.time.Clock()

    # 颜色定义
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 清屏
        screen.fill(WHITE)

        # ========== 绘制各种图形 ==========

        # 1. 矩形
        # pygame.draw.rect(表面, 颜色, (x, y, 宽, 高), 边框宽度)
        # 边框宽度=0表示填充，>0表示只画边框
        pygame.draw.rect(screen, RED, (50, 50, 100, 60))      # 实心红色矩形
        pygame.draw.rect(screen, BLUE, (200, 50, 100, 60), 3)  # 蓝色边框矩形

        # 2. 圆形
        # pygame.draw.circle(表面, 颜色, (圆心x, 圆心y), 半径, 边框宽度)
        pygame.draw.circle(screen, GREEN, (100, 200), 40)      # 实心绿色圆
        pygame.draw.circle(screen, YELLOW, (250, 200), 40, 5)  # 黄色圆环

        # 3. 直线
        # pygame.draw.line(表面, 颜色, (起点x, 起点y), (终点x, 终点y), 线宽)
        pygame.draw.line(screen, (0, 0, 0), (400, 50), (400, 250), 2)

        # 4. 多边形（三角形）
        # pygame.draw.polygon(表面, 颜色, [(点1x, 点1y), (点2x, 点2y), ...])
        triangle_points = [(600, 50), (550, 150), (650, 150)]
        pygame.draw.polygon(screen, (0, 255, 255), triangle_points)

        # 5. 椭圆
        # pygame.draw.ellipse(表面, 颜色, (x, y, 宽, 高), 边框宽度)
        pygame.draw.ellipse(screen, (255, 0, 255), (500, 200, 120, 60))

        # 6. 文字
        # 创建字体
        font = pygame.font.Font(None, 36)  # None表示默认字体，36是字号
        # 渲染文字
        text_surface = font.render("Hello Pygame!", True, (0, 0, 0))
        # 绘制到屏幕
        screen.blit(text_surface, (50, 300))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


# ============================================================================
# 第4节：处理事件
# ============================================================================
"""
【什么是事件？】

事件是用户与程序交互的方式，例如：
- 点击关闭按钮
- 按下键盘
- 移动鼠标
- 点击鼠标


【处理事件的两种方式】

1. 事件循环：检测特定事件发生
2. 状态查询：获取按键/鼠标的当前状态


【代码示例】
"""


def lesson4_handle_events():
    """
    第4节示例：处理键盘和鼠标事件
    """
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("处理事件 - 按ESC退出，点击鼠标试试")
    clock = pygame.time.Clock()

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # 鼠标位置
    mouse_x, mouse_y = 400, 300

    # 方块位置
    rect_x, rect_y = 400, 300

    font = pygame.font.Font(None, 36)

    running = True
    while running:
        # ========== 方式1：事件循环 ==========
        for event in pygame.event.get():
            # 退出事件
            if event.type == pygame.QUIT:
                running = False

            # 键盘按下事件
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    print("空格键被按下！")

            # 鼠标按下事件
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # event.button: 1=左键, 2=中键, 3=右键
                if event.button == 1:
                    print(f"鼠标左键点击位置: {event.pos}")

            # 鼠标移动事件
            elif event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = event.pos

        # ========== 方式2：状态查询 ==========
        # 获取所有按键的状态
        keys = pygame.key.get_pressed()

        # 根据按键状态移动方块
        speed = 5
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            rect_x -= speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            rect_x += speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            rect_y -= speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            rect_y += speed

        # 边界检测
        rect_x = max(0, min(rect_x, 800 - 50))
        rect_y = max(0, min(rect_y, 600 - 50))

        # ========== 绘制 ==========
        screen.fill(WHITE)

        # 绘制可移动的方块
        pygame.draw.rect(screen, (0, 100, 255), (rect_x, rect_y, 50, 50))

        # 绘制鼠标位置指示器
        pygame.draw.circle(screen, (255, 0, 0), (mouse_x, mouse_y), 10)

        # 显示提示
        hint1 = font.render("Arrow Keys / WASD: Move Blue Box", True, BLACK)
        hint2 = font.render("Mouse: Move Red Circle", True, BLACK)
        hint3 = font.render("ESC: Exit", True, BLACK)
        screen.blit(hint1, (10, 10))
        screen.blit(hint2, (10, 40))
        screen.blit(hint3, (10, 70))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


# ============================================================================
# 第5节：让物体动起来
# ============================================================================
"""
【移动的原理】

物体的位置会随着时间变化：
    新位置 = 旧位置 + 速度

每帧都执行这个计算，物体就会不断移动！


【速度的概念】

速度是一个向量，包含方向和大小：
- 速度 > 0：向右/下移动
- 速度 < 0：向左/上移动
- 速度 = 0：不动


【边界反弹】

当物体碰到边界时，将对应方向的速度取反即可实现反弹！


【代码示例】
"""


def lesson5_moving_objects():
    """
    第5节示例：让物体移动和反弹
    """
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("移动物体 - 观察小球的运动")
    clock = pygame.time.Clock()

    WIDTH, HEIGHT = 800, 600

    # 小球属性
    ball_x = 400.0  # x坐标
    ball_y = 300.0  # y坐标
    ball_radius = 20  # 半径
    ball_speed_x = 5.0  # x方向速度
    ball_speed_y = 3.0  # y方向速度

    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # ========== 更新位置 ==========
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # ========== 边界检测和反弹 ==========
        # 左右边界
        if ball_x - ball_radius <= 0:
            ball_x = ball_radius
            ball_speed_x = -ball_speed_x  # 速度取反
        elif ball_x + ball_radius >= WIDTH:
            ball_x = WIDTH - ball_radius
            ball_speed_x = -ball_speed_x

        # 上下边界
        if ball_y - ball_radius <= 0:
            ball_y = ball_radius
            ball_speed_y = -ball_speed_y
        elif ball_y + ball_radius >= HEIGHT:
            ball_y = HEIGHT - ball_radius
            ball_speed_y = -ball_speed_y

        # ========== 绘制 ==========
        screen.fill(WHITE)
        pygame.draw.circle(screen, RED, (int(ball_x), int(ball_y)), ball_radius)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


# ============================================================================
# 第6节：碰撞检测
# ============================================================================
"""
【什么是碰撞检测？】

判断两个游戏物体是否接触或重叠。

【两种常用的碰撞检测方法】

1. 矩形碰撞（AABB）
   - 适用于方形物体
   - 简单高效
   - pygame.Rect.colliderect()

2. 圆形碰撞
   - 适用于圆形物体
   - 两圆心距离 < 两半径之和 = 碰撞


【代码示例】
"""


def lesson6_collision_detection():
    """
    第6节示例：碰撞检测
    """
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("碰撞检测 - 用方向键控制蓝色方块")
    clock = pygame.time.Clock()

    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)

    # 玩家方块
    player_x = 100
    player_y = 100
    player_size = 40
    player_speed = 5

    # 目标方块（用于矩形碰撞演示）
    target_rect = pygame.Rect(300, 200, 60, 60)

    # 目标圆形（用于圆形碰撞演示）
    circle_x = 500
    circle_y = 350
    circle_radius = 40

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

        # 创建玩家矩形
        player_rect = pygame.Rect(player_x, player_y, player_size, player_size)

        # ========== 矩形碰撞检测 ==========
        rect_collision = player_rect.colliderect(target_rect)

        # ========== 圆形碰撞检测 ==========
        # 计算玩家中心和圆心的距离
        player_center_x = player_x + player_size // 2
        player_center_y = player_y + player_size // 2

        import math
        distance = math.sqrt(
            (player_center_x - circle_x) ** 2 +
            (player_center_y - circle_y) ** 2
        )
        # 碰撞条件：距离 < 玩家半径 + 圆半径
        circle_collision = distance < (player_size // 2 + circle_radius)

        # ========== 绘制 ==========
        screen.fill(WHITE)

        # 绘制目标方块（碰撞时变色）
        target_color = GREEN if rect_collision else RED
        pygame.draw.rect(screen, target_color, target_rect)
        rect_text = font.render("Rect", True, (0, 0, 0))
        screen.blit(rect_text, (target_rect.x + 10, target_rect.y + 20))

        # 绘制目标圆（碰撞时变色）
        circle_color = GREEN if circle_collision else RED
        pygame.draw.circle(screen, circle_color, (circle_x, circle_y), circle_radius)
        circle_text = font.render("Circle", True, (0, 0, 0))
        screen.blit(circle_text, (circle_x - 30, circle_y - 10))

        # 绘制玩家
        pygame.draw.rect(screen, BLUE, player_rect)

        # 显示状态
        status = font.render(f"Rect: {'HIT!' if rect_collision else 'No'}  "
                            f"Circle: {'HIT!' if circle_collision else 'No'}",
                            True, (0, 0, 0))
        screen.blit(status, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


# ============================================================================
# 第7节：游戏1 - 接球游戏
# ============================================================================
"""
【完整游戏示例：接球游戏】

这是一个完整的游戏，综合运用了前面学的所有知识！

游戏规则：
- 用键盘控制挡板左右移动
- 接住下落的小球得分
- 漏掉3个球游戏结束

完整代码请看：games/05_catch_ball.py
"""


def lesson7_catch_ball_game():
    """
    第7节：运行接球游戏

    这个游戏展示了如何把学到的知识组合成一个完整的游戏。
    """
    print("接球游戏 - 请运行 games/05_catch_ball.py")
    print("控制方式：")
    print("  左右方向键或A/D键 - 移动挡板")
    print("  空格键 - 重新开始")
    print("  ESC - 退出游戏")


# ============================================================================
# 第8节：游戏2 - 贪吃蛇
# ============================================================================
"""
【完整游戏示例：贪吃蛇】

这是一个经典的贪吃蛇游戏！

游戏规则：
- 控制蛇移动，吃掉食物
- 每吃一个食物，蛇身体变长
- 撞到墙壁或自己身体游戏结束

关键技术：
- 使用网格移动
- 用列表存储蛇身体
- 碰撞检测

完整代码请看：games/06_snake.py
"""


def lesson8_snake_game():
    """
    第8节：运行贪吃蛇游戏

    这个游戏展示了更复杂的游戏逻辑。
    """
    print("贪吃蛇游戏 - 请运行 games/06_snake.py")
    print("控制方式：")
    print("  方向键或WASD - 控制蛇的移动方向")
    print("  空格键 - 暂停/继续游戏")
    print("  R键 - 重新开始")
    print("  ESC - 退出游戏")


# ============================================================================
# 教程导航
# ============================================================================
def show_menu():
    """
    显示教程菜单
    """
    print("\n" + "=" * 60)
    print("       游戏开发速成教程 - pygame")
    print("=" * 60)
    print("\n请选择要学习的章节：\n")
    print("  1. 游戏开发入门（pygame介绍、游戏循环概念）")
    print("  2. 创建游戏窗口（初始化、窗口、颜色）")
    print("  3. 绘制图形（矩形、圆形、线条、文字）")
    print("  4. 处理事件（键盘、鼠标、退出）")
    print("  5. 让物体动起来（移动原理、速度、边界）")
    print("  6. 碰撞检测（矩形碰撞、圆形碰撞）")
    print("  7. 游戏1 - 接球游戏（完整游戏）")
    print("  8. 游戏2 - 贪吃蛇（完整游戏）")
    print("  9. 运行所有示例")
    print("  0. 退出")
    print("\n" + "=" * 60)


def run_lesson(choice):
    """
    运行指定章节的示例

    参数：
        choice (int): 章节编号
    """
    lessons = {
        2: lesson2_create_window,
        3: lesson3_draw_shapes,
        4: lesson4_handle_events,
        5: lesson5_moving_objects,
        6: lesson6_collision_detection,
        7: lesson7_catch_ball_game,
        8: lesson8_snake_game,
    }

    if choice in lessons:
        print(f"\n正在运行第{choice}节示例...\n")
        lessons[choice]()
    else:
        print("无效的选择！")


def main():
    """
    主函数 - 教程入口
    """
    print("""
    ╔════════════════════════════════════════════════════════════╗
    ║                    游戏开发速成教程                         ║
    ║                      使用 pygame                           ║
    ╠════════════════════════════════════════════════════════════╣
    ║  欢迎来到游戏开发的世界！                                   ║
    ║                                                            ║
    ║  这个教程将教你如何使用Python和pygame创建游戏。             ║
    ║  每一节都有详细的讲解和可运行的代码示例。                   ║
    ║                                                            ║
    ║  让我们开始吧！                                            ║
    ╚════════════════════════════════════════════════════════════╝
    """)

    while True:
        show_menu()
        try:
            choice = int(input("请输入选择 (0-9): "))
            if choice == 0:
                print("\n感谢学习！再见！\n")
                break
            elif choice == 9:
                # 运行所有示例
                for i in [2, 3, 4, 5, 6]:
                    print(f"\n{'='*40}")
                    print(f"第{i}节示例")
                    print('='*40)
                    run_lesson(i)
            elif choice == 1:
                print("\n第1节是理论讲解，请阅读代码中的注释！")
                print("主要概念：游戏循环、pygame是什么、如何安装pygame")
                input("\n按回车继续...")
            else:
                run_lesson(choice)
        except ValueError:
            print("请输入有效的数字！")
        except Exception as e:
            print(f"发生错误: {e}")


# 程序入口
if __name__ == "__main__":
    main()
