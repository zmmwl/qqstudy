"""
游戏开发入门 - 第一个Pygame窗口
================================

这是你第一个pygame程序！
运行后会弹出一个窗口，持续3秒后自动关闭。

知识点：
1. pygame初始化
2. 创建游戏窗口
3. 游戏循环
4. 退出pygame

作者：游戏开发速成教程
"""

import pygame
import sys

# ==================== 初始化 ====================
def init_game(width, height, title):
    """
    初始化pygame并创建游戏窗口

    参数：
        width (int): 窗口宽度（像素）
        height (int): 窗口高度（像素）
        title (str): 窗口标题

    返回：
        pygame.Surface: 游戏窗口对象，用于后续绘制

    示例：
        screen = init_game(800, 600, "我的游戏")
    """
    # 1. 初始化pygame的所有模块
    pygame.init()

    # 2. 创建游戏窗口
    # pygame.display.set_mode() 创建一个窗口并返回Surface对象
    # Surface对象就是我们画画的"画布"
    screen = pygame.display.set_mode((width, height))

    # 3. 设置窗口标题
    pygame.display.set_caption(title)

    return screen


# ==================== 游戏循环 ====================
def game_loop(screen, duration_ms=3000):
    """
    游戏主循环 - 游戏的心跳

    参数：
        screen (pygame.Surface): 游戏窗口对象
        duration_ms (int): 游戏持续时间（毫秒），默认3秒

    游戏循环的三个步骤：
    1. 处理事件（键盘、鼠标、关闭窗口等）
    2. 更新游戏状态
    3. 绘制画面

    示例：
        game_loop(screen, 5000)  # 运行5秒
    """
    # 获取开始时间
    start_time = pygame.time.get_ticks()

    # 创建时钟对象，用于控制帧率
    clock = pygame.time.Clock()

    # 游戏主循环
    running = True
    while running:
        # ========== 步骤1：处理事件 ==========
        for event in pygame.event.get():
            # 用户点击关闭按钮
            if event.type == pygame.QUIT:
                running = False

        # ========== 步骤2：更新游戏状态 ==========
        # 检查是否到达指定时间
        current_time = pygame.time.get_ticks()
        if current_time - start_time >= duration_ms:
            running = False

        # ========== 步骤3：绘制画面 ==========
        # 填充背景色（白色）
        # RGB颜色：(红, 绿, 蓝)，范围0-255
        screen.fill((255, 255, 255))

        # 更新显示（把画好的内容显示到屏幕上）
        pygame.display.flip()

        # 控制帧率为60FPS（每秒60帧）
        clock.tick(60)

    # 退出pygame
    pygame.quit()
    sys.exit()


# ==================== 主程序 ====================
def main():
    """
    主函数 - 程序入口
    """
    print("=" * 50)
    print("欢迎来到Pygame游戏开发世界！")
    print("窗口将在3秒后自动关闭...")
    print("=" * 50)

    # 初始化游戏
    screen = init_game(
        width=800,      # 窗口宽度
        height=600,     # 窗口高度
        title="我的第一个Pygame窗口"  # 窗口标题
    )

    # 运行游戏循环
    game_loop(screen, duration_ms=3000)


# 程序入口
if __name__ == "__main__":
    main()
