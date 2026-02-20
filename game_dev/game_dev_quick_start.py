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

你可以把游戏想象成一本"翻页动画书"：
- 每一页就是一帧画面
- 快速翻页（每秒60页）就产生了动画效果
- 游戏循环就是不断"翻页"的过程


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


【pygame的坐标系】

pygame使用的是"屏幕坐标系"，和数学课本上的坐标系不太一样：
- 原点(0, 0)在窗口的【左上角】
- x轴向右递增（和数学一样）
- y轴【向下】递增（和数学相反！）

例如在800x600的窗口中：
- 左上角是 (0, 0)
- 右下角是 (800, 600)
- 中心点大约是 (400, 300)

记住：y值越大，位置越靠下！


【代码示例】
"""

import pygame
import sys


def lesson2_create_window():
    """
    第2节示例：创建一个基本的游戏窗口

    这是所有pygame程序的基本结构！

    调用示例：
        lesson2_create_window()  # 打开一个800x600的白色窗口

    注意：运行后会打开游戏窗口，按关闭按钮退出。
    """
    # 步骤1：初始化pygame
    pygame.init()

    # 步骤2：创建窗口
    # set_mode() 返回一个Surface对象，我们可以把它想象成一块"画布"
    # 所有图形都画在这块画布上，然后显示到屏幕上
    WIDTH, HEIGHT = 800, 600  # 窗口宽800像素，高600像素
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # 步骤3：设置窗口标题
    pygame.display.set_caption("我的第一个游戏窗口")

    # 步骤4：创建时钟对象（用于控制游戏速度）
    # 想象成游戏的"节拍器"，控制每秒画多少帧
    clock = pygame.time.Clock()

    # 步骤5：游戏主循环
    # 这是游戏的"心脏"，只要running为True，游戏就会一直运行
    running = True
    while running:
        # 5.1 处理事件（事件就是玩家的操作）
        # event.get() 获取所有未处理的事件，就像查看"收件箱"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 点击关闭按钮
                running = False  # 把running改成False，循环就会结束

        # 5.2 更新游戏状态（这里暂时没有游戏逻辑）

        # 5.3 绘制画面
        screen.fill((255, 255, 255))  # 用白色填充整个屏幕（相当于清空画布）
        pygame.display.flip()  # 把画好的内容显示出来（相当于"翻页"）

        # 5.4 控制帧率
        # tick(60) 表示每秒最多循环60次，也就是60帧
        # 这样游戏速度就不会太快，在不同的电脑上运行速度一致
        clock.tick(60)

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

    调用示例：
        lesson3_draw_shapes()  # 显示各种图形的绘制演示

    展示内容：
        - 矩形（实心和空心）
        - 圆形（实心和空心）
        - 直线
        - 多边形（三角形）
        - 椭圆
        - 文字
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
        # pygame.draw.rect(表面, 颜色, (左上角x, 左上角y, 宽度, 高度), 边框宽度)
        # 边框宽度=0表示填充（实心），>0表示只画边框（空心）
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
        # pygame.draw.polygon(表面, 颜色, [点1的坐标, 点2的坐标, ...])
        # 给出所有顶点的坐标，pygame会自动把它们连起来
        triangle_points = [(600, 50), (550, 150), (650, 150)]
        pygame.draw.polygon(screen, (0, 255, 255), triangle_points)

        # 5. 椭圆
        # pygame.draw.ellipse(表面, 颜色, (左上角x, 左上角y, 宽度, 高度), 边框宽度)
        # 椭圆是画在一个"不可见的矩形"里面的
        pygame.draw.ellipse(screen, (255, 0, 255), (500, 200, 120, 60))

        # 6. 文字（显示文字需要三个步骤）
        # 步骤1：创建字体对象
        font = pygame.font.Font(None, 36)  # None表示使用默认字体，36是字号大小
        # 步骤2：渲染文字（把文字变成图像）
        # render(文字内容, 是否抗锯齿, 颜色)
        # 抗锯齿=True会让文字边缘更平滑
        text_surface = font.render("Hello Pygame!", True, (0, 0, 0))
        # 步骤3：把文字图像画到屏幕上
        # blit的意思是"把一个图像复制到另一个图像上"
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

事件就是"发生了什么事情"，比如：
- 点击关闭按钮 → 产生QUIT事件
- 按下键盘 → 产生KEYDOWN事件
- 移动鼠标 → 产生MOUSEMOTION事件
- 点击鼠标 → 产生MOUSEBUTTONDOWN事件

pygame会把所有事件放进一个"队列"（就像排队一样），
我们需要用循环来逐个处理它们。


【处理事件的两种方式】

1. 事件循环：检测"刚才发生了什么"（比如按了一下空格）
   - 适合处理单次触发的操作（如跳跃、开枪）

2. 状态查询：检测"现在是什么状态"（比如按键是否按着）
   - 适合处理持续性的操作（如移动、加速）

打个比方：
- 事件循环像是"门铃响了"——告诉你有人按了门铃
- 状态查询像是"门是否开着"——告诉你门的当前状态


【代码示例】
"""


def lesson4_handle_events():
    """
    第4节示例：处理键盘和鼠标事件

    调用示例：
        lesson4_handle_events()  # 打开事件处理演示

    操作说明：
        - 方向键或WASD：移动蓝色方块
        - 鼠标移动：红色圆圈跟随
        - 空格键：控制台输出提示
        - ESC或关闭窗口：退出
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
        # 遍历所有未处理的事件
        for event in pygame.event.get():
            # 退出事件：当用户点击窗口的关闭按钮时触发
            if event.type == pygame.QUIT:
                running = False

            # 键盘按下事件：当用户按下任意键时触发
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # ESC键的编号
                    running = False
                elif event.key == pygame.K_SPACE:  # 空格键的编号
                    print("空格键被按下！")

            # 鼠标按下事件：当用户点击鼠标时触发
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # event.button 告诉我们是哪个键：1=左键, 2=中键, 3=右键
                if event.button == 1:
                    print(f"鼠标左键点击位置: {event.pos}")  # event.pos 是 (x, y) 坐标

            # 鼠标移动事件：当用户移动鼠标时触发
            elif event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = event.pos  # 获取鼠标当前位置

        # ========== 方式2：状态查询 ==========
        # get_pressed() 返回一个列表，记录所有按键的当前状态
        # 如果按键被按下，对应的值就是 True，否则是 False
        keys = pygame.key.get_pressed()

        # 根据按键状态移动方块
        # 注意：这里用 if 而不是 elif，这样可以同时按两个键斜着移动！
        speed = 5  # 每帧移动5像素
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:  # 左箭头或A键
            rect_x -= speed  # 向左移动，x坐标减小
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:  # 右箭头或D键
            rect_x += speed  # 向右移动，x坐标增大
        if keys[pygame.K_UP] or keys[pygame.K_w]:  # 上箭头或W键
            rect_y -= speed  # 向上移动，y坐标减小（记住y轴向下！）
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:  # 下箭头或S键
            rect_y += speed  # 向下移动，y坐标增大

        # 边界检测（防止方块跑出屏幕）
        # max(0, ...) 确保坐标不会小于0（不会跑到左边或上边外面）
        # min(..., 750) 确保坐标不会超过边界（800-50=750，不会跑到右边或下边外面）
        rect_x = max(0, min(rect_x, 800 - 50))  # 800是窗口宽度，50是方块宽度
        rect_y = max(0, min(rect_y, 600 - 50))  # 600是窗口高度，50是方块高度

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

举个例子：
- 假设小球的x坐标是100，x方向速度是5
- 第1帧后：x = 100 + 5 = 105
- 第2帧后：x = 105 + 5 = 110
- ...小球就向右移动了！


【速度的概念】

速度决定了物体移动的快慢和方向：
- 速度 > 0：向右/下移动（x增加或y增加）
- 速度 < 0：向左/上移动（x减少或y减少）
- 速度 = 0：不动

速度的绝对值越大，移动越快！


【边界反弹】

当物体碰到边界时，把速度变成负数就能反弹！
- 原来向右移动（速度=5）
- 碰到右边界后，速度变成-5
- 现在就向左移动了！

这就像打乒乓球，球碰到球拍后方向会反过来。


【代码示例】
"""


def lesson5_moving_objects():
    """
    第5节示例：让物体移动和反弹

    调用示例：
        lesson5_moving_objects()  # 观看红色小球在窗口内弹跳

    演示内容：
        - 小球自动移动
        - 碰到边界自动反弹
        - ESC或关闭窗口退出
    """
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("移动物体 - 观察小球的运动")
    clock = pygame.time.Clock()

    WIDTH, HEIGHT = 800, 600

    # 小球属性
    ball_x = 400.0  # x坐标（用小数，因为速度可能是小数）
    ball_y = 300.0  # y坐标
    ball_radius = 20  # 半径（像素）
    ball_speed_x = 5.0  # x方向速度：正值表示向右移动
    ball_speed_y = 3.0  # y方向速度：正值表示向下移动

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
        # 这两行代码让小球"动"起来
        ball_x += ball_speed_x  # x坐标增加，小球向右移动
        ball_y += ball_speed_y  # y坐标增加，小球向下移动

        # ========== 边界检测和反弹 ==========
        # 判断小球是否碰到左边界（小球左边缘到达x=0的位置）
        if ball_x - ball_radius <= 0:
            ball_x = ball_radius  # 防止小球"卡"在边界里
            ball_speed_x = -ball_speed_x  # 速度取反，小球开始向右移动

        # 判断小球是否碰到右边界
        elif ball_x + ball_radius >= WIDTH:
            ball_x = WIDTH - ball_radius
            ball_speed_x = -ball_speed_x  # 速度取反，小球开始向左移动

        # 判断小球是否碰到上边界
        if ball_y - ball_radius <= 0:
            ball_y = ball_radius
            ball_speed_y = -ball_speed_y  # 速度取反，小球开始向下移动

        # 判断小球是否碰到下边界
        elif ball_y + ball_radius >= HEIGHT:
            ball_y = HEIGHT - ball_radius
            ball_speed_y = -ball_speed_y  # 速度取反，小球开始向上移动

        # ========== 绘制 ==========
        screen.fill(WHITE)
        # 注意：ball_x 和 ball_y 是小数，但画图需要整数坐标
        # int() 函数把小数转换成整数
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
比如：子弹打中敌人、角色吃到金币、球拍接到球...

【两种常用的碰撞检测方法】

1. 矩形碰撞（AABB）
   - 适用于方形物体
   - 简单高效，是最常用的方法
   - pygame提供了一个现成的函数：colliderect()

2. 圆形碰撞
   - 适用于圆形物体（如球类游戏）
   - 原理：计算两个圆心的距离，如果距离小于两半径之和，就碰撞了
   - 需要用到勾股定理！


【代码示例】
"""


def lesson6_collision_detection():
    """
    第6节示例：碰撞检测

    调用示例：
        lesson6_collision_detection()  # 打开碰撞检测演示

    操作说明：
        - 方向键或WASD：移动蓝色方块
        - 碰到红色物体时，物体会变成绿色
        - 演示矩形碰撞和圆形碰撞两种方式
        - ESC或关闭窗口退出
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

        # 边界限制（防止玩家跑出屏幕）
        player_x = max(0, min(player_x, 800 - player_size))
        player_y = max(0, min(player_y, 600 - player_size))

        # 创建玩家矩形对象（用于碰撞检测）
        # pygame.Rect(左上角x, 左上角y, 宽度, 高度)
        player_rect = pygame.Rect(player_x, player_y, player_size, player_size)

        # ========== 矩形碰撞检测 ==========
        # colliderect() 是pygame提供的函数，自动检测两个矩形是否重叠
        # 返回 True 表示碰撞，False 表示没碰撞
        rect_collision = player_rect.colliderect(target_rect)

        # ========== 圆形碰撞检测 ==========
        # 步骤1：计算玩家方块的中心点（因为玩家是方块，我们需要找到它的中心）
        player_center_x = player_x + player_size // 2  # 方块中心的x坐标
        player_center_y = player_y + player_size // 2  # 方块中心的y坐标

        # 步骤2：用勾股定理计算两点之间的距离
        # 勾股定理：直角三角形中，斜边² = 直角边1² + 直角边2²
        # 所以：距离 = sqrt((x2-x1)² + (y2-y1)²)
        import math  # math.sqrt() 用来计算平方根
        distance = math.sqrt(
            (player_center_x - circle_x) ** 2 +  # x方向的差的平方
            (player_center_y - circle_y) ** 2    # y方向的差的平方
        )
        # 步骤3：判断是否碰撞
        # 如果两个圆心的距离 < 两个半径之和，说明两个圆重叠了
        circle_collision = distance < (player_size // 2 + circle_radius)

        # ========== 绘制 ==========
        screen.fill(WHITE)

        # 绘制目标方块（碰撞时变色）
        # 这是一个"三元表达式"：值1 if 条件 else 值2
        # 如果碰撞了就用绿色，否则用红色
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

    调用示例：
        lesson7_catch_ball_game()  # 显示接球游戏的说明

    游戏位置：
        完整游戏代码在 games/05_catch_ball.py

    控制方式：
        - 左右方向键或A/D键：移动挡板
        - 空格键：重新开始
        - ESC：退出游戏
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

    调用示例：
        lesson8_snake_game()  # 显示贪吃蛇游戏的说明

    游戏位置：
        完整游戏代码在 games/06_snake.py

    控制方式：
        - 方向键或WASD：控制蛇的移动方向
        - 空格键：暂停/继续游戏
        - R键：重新开始
        - ESC：退出游戏
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

    这个函数没有参数，直接调用即可显示菜单。

    调用示例：
        show_menu()  # 显示教程菜单
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
        choice (int): 章节编号，范围 2-8

    调用示例：
        run_lesson(2)  # 运行第2节：创建游戏窗口
        run_lesson(3)  # 运行第3节：绘制图形
        run_lesson(6)  # 运行第6节：碰撞检测
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

    这个函数是整个教程的入口，显示菜单并处理用户选择。

    调用示例：
        main()  # 启动教程，进入交互式菜单

    注意：通常在文件末尾这样调用：
        if __name__ == "__main__":
            main()
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
