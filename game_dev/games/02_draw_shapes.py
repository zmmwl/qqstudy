"""
绘制图形 - 学习pygame绑定的基本图形
====================================

这个示例展示如何在pygame中绘制各种图形。

知识点：
1. 颜色的表示（RGB）
2. 绘制矩形
3. 绘制圆形
4. 绘制线条
5. 绘制多边形
6. 绘制文字

作者：游戏开发速成教程
"""

import pygame
import sys

# ==================== 颜色常量 ====================
# RGB颜色值（红, 绿, 蓝），范围0-255
WHITE = (255, 255, 255)      # 白色
BLACK = (0, 0, 0)            # 黑色
RED = (255, 0, 0)            # 红色
GREEN = (0, 255, 0)          # 绿色
BLUE = (0, 0, 255)           # 蓝色
YELLOW = (255, 255, 0)       # 黄色
CYAN = (0, 255, 255)         # 青色
MAGENTA = (255, 0, 255)      # 品红色
ORANGE = (255, 165, 0)       # 橙色


# ==================== 绘制函数 ====================
def draw_rectangle(surface, color, x, y, width, height, border_width=0):
    """
    绘制矩形

    参数：
        surface (pygame.Surface): 要绘制到的表面（通常是屏幕）
        color (tuple): 颜色 (R, G, B)
        x (int): 矩形左上角的x坐标
        y (int): 矩形左上角的y坐标
        width (int): 矩形宽度
        height (int): 矩形高度
        border_width (int): 边框宽度
                         0 = 填充实心矩形
                         >0 = 空心矩形边框宽度

    示例：
        draw_rectangle(screen, RED, 100, 100, 50, 30)  # 实心红色矩形
        draw_rectangle(screen, BLUE, 200, 100, 50, 30, 3)  # 蓝色边框矩形
    """
    pygame.draw.rect(surface, color, (x, y, width, height), border_width)


def draw_circle(surface, color, x, y, radius, border_width=0):
    """
    绘制圆形

    参数：
        surface (pygame.Surface): 要绘制到的表面
        color (tuple): 颜色 (R, G, B)
        x (int): 圆心x坐标
        y (int): 圆心y坐标
        radius (int): 半径
        border_width (int): 边框宽度
                         0 = 填充实心圆
                         >0 = 空心圆边框宽度

    示例：
        draw_circle(screen, GREEN, 400, 300, 50)  # 实心绿色圆
        draw_circle(screen, YELLOW, 400, 300, 60, 3)  # 黄色圆环
    """
    pygame.draw.circle(surface, color, (x, y), radius, border_width)


def draw_line(surface, color, start_x, start_y, end_x, end_y, width=1):
    """
    绘制直线

    参数：
        surface (pygame.Surface): 要绘制到的表面
        color (tuple): 颜色 (R, G, B)
        start_x (int): 起点x坐标
        start_y (int): 起点y坐标
        end_x (int): 终点x坐标
        end_y (int): 终点y坐标
        width (int): 线条宽度，默认1

    示例：
        draw_line(screen, BLACK, 0, 0, 800, 600, 2)  # 黑色斜线
    """
    pygame.draw.line(surface, color, (start_x, start_y), (end_x, end_y), width)


def draw_polygon(surface, color, points, border_width=0):
    """
    绘制多边形

    参数：
        surface (pygame.Surface): 要绘制到的表面
        color (tuple): 颜色 (R, G, B)
        points (list): 顶点坐标列表，格式：[(x1, y1), (x2, y2), ...]
        border_width (int): 边框宽度，0为填充

    示例：
        # 绘制三角形
        draw_polygon(screen, CYAN, [(400, 100), (300, 200), (500, 200)])
    """
    pygame.draw.polygon(surface, color, points, border_width)


def draw_text(surface, text, x, y, font_size=32, color=BLACK, font_name=None):
    """
    绘制文字

    参数：
        surface (pygame.Surface): 要绘制到的表面
        text (str): 要显示的文字
        x (int): 文字左上角x坐标
        y (int): 文字左上角y坐标
        font_size (int): 字体大小，默认32
        color (tuple): 文字颜色，默认黑色
        font_name (str): 字体名称，None表示默认字体

    返回：
        pygame.Rect: 文字的矩形区域

    示例：
        draw_text(screen, "Hello Pygame!", 100, 100, 48, RED)
    """
    # 创建字体对象
    font = pygame.font.Font(font_name, font_size)

    # 渲染文字（抗锯齿=True，颜色，背景色=None表示透明）
    text_surface = font.render(text, True, color)

    # 将文字绘制到屏幕上
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)

    return text_rect


def draw_ellipse(surface, color, x, y, width, height, border_width=0):
    """
    绘制椭圆

    参数：
        surface (pygame.Surface): 要绘制到的表面
        color (tuple): 颜色 (R, G, B)
        x (int): 椭圆外接矩形左上角x坐标
        y (int): 椭圆外接矩形左上角y坐标
        width (int): 椭圆宽度
        height (int): 椭圆高度
        border_width (int): 边框宽度，0为填充

    示例：
        draw_ellipse(screen, MAGENTA, 100, 400, 100, 50)  # 紫色椭圆
    """
    pygame.draw.ellipse(surface, color, (x, y, width, height), border_width)


# ==================== 游戏主循环 ====================
def main():
    """
    主函数 - 展示各种绑定的绘制方法
    """
    # 初始化
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("绘制图形示例")
    clock = pygame.time.Clock()

    # 游戏循环
    running = True
    while running:
        # 处理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # ========== 绘制各种图形 ==========

        # 清屏（白色背景）
        screen.fill(WHITE)

        # 1. 绘制矩形
        draw_rectangle(screen, RED, 50, 50, 100, 60)      # 实心红色矩形
        draw_rectangle(screen, BLUE, 200, 50, 100, 60, 3)  # 蓝色边框矩形

        # 2. 绘制圆形
        draw_circle(screen, GREEN, 100, 200, 40)           # 实心绿色圆
        draw_circle(screen, YELLOW, 250, 200, 40, 5)       # 黄色圆环

        # 3. 绘制线条
        draw_line(screen, BLACK, 400, 50, 400, 250, 2)     # 竖线
        draw_line(screen, ORANGE, 350, 150, 450, 150, 3)   # 横线

        # 4. 绘制三角形（多边形）
        triangle_points = [(600, 50), (550, 150), (650, 150)]
        draw_polygon(screen, CYAN, triangle_points)

        # 5. 绘制椭圆
        draw_ellipse(screen, MAGENTA, 500, 200, 120, 60)

        # 6. 绘制文字
        draw_text(screen, "Hello Pygame!", 50, 300, 48, RED)
        draw_text(screen, "绘制图形示例", 50, 380, 36, BLUE)

        # 7. 绘制更多形状组合 - 小房子
        # 房子主体
        draw_rectangle(screen, ORANGE, 150, 420, 100, 80)
        # 屋顶（三角形）
        roof_points = [(140, 420), (200, 380), (260, 420)]
        draw_polygon(screen, RED, roof_points)
        # 门
        draw_rectangle(screen, BROWN if 'BROWN' in dir() else (139, 69, 19),
                       180, 460, 30, 40)
        # 窗户
        draw_rectangle(screen, CYAN, 160, 440, 20, 20)
        draw_rectangle(screen, CYAN, 220, 440, 20, 20)

        # 8. 画一个笑脸
        center_x, center_y = 600, 450
        # 脸
        draw_circle(screen, YELLOW, center_x, center_y, 60)
        # 眼睛
        draw_circle(screen, BLACK, center_x - 20, center_y - 15, 8)
        draw_circle(screen, BLACK, center_x + 20, center_y - 15, 8)
        # 嘴巴（用弧线画）
        draw_arc(screen, BLACK, center_x - 25, center_y - 10, 50, 40, 3.14, 0, 3)

        # 更新显示
        pygame.display.flip()

        # 控制帧率
        clock.tick(60)

    pygame.quit()
    sys.exit()


def draw_arc(surface, color, x, y, width, height, start_angle, stop_angle, width_line=1):
    """
    绘制弧线

    参数：
        surface (pygame.Surface): 要绘制到的表面
        color (tuple): 颜色 (R, G, B)
        x (int): 弧线外接矩形左上角x坐标
        y (int): 弧线外接矩形左上角y坐标
        width (int): 弧线宽度
        height (int): 弧线高度
        start_angle (float): 起始角度（弧度）
        stop_angle (float): 结束角度（弧度）
        width_line (int): 线条宽度

    注意：角度用弧度表示
        0 = 3点钟方向
        pi/2 = 6点钟方向
        pi = 9点钟方向
        3pi/2 = 12点钟方向

    示例：
        # 画一个半圆弧
        draw_arc(screen, BLACK, 100, 100, 50, 50, 0, 3.14, 3)
    """
    import math
    pygame.draw.arc(surface, color, (x, y, width, height),
                    start_angle, stop_angle, width_line)


# 程序入口
if __name__ == "__main__":
    main()
