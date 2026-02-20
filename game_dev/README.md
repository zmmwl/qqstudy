# 游戏开发速成教程

适合初中生学习的 Pygame 游戏开发教程。

## 目录结构

```
game_dev/
├── game_dev_quick_start.py        # 主教程（约3小时）
├── game_dev_exercises.py          # 练习题（带答案）
├── games/                         # 游戏代码
│   ├── 01_hello_pygame.py        # 第一个窗口
│   ├── 02_draw_shapes.py         # 绘制图形
│   ├── 03_moving_ball.py         # 移动的小球
│   ├── 04_keyboard_control.py    # 键盘控制
│   ├── 05_catch_ball.py          # 接球游戏
│   ├── 06_snake.py               # 贪吃蛇
│   └── 07_space_shooter.py       # 太空射击
└── README.md                      # 本文件
```

## 安装依赖

在开始学习之前，请确保已经安装了 Python 和 pygame：

```bash
# 安装 pygame
pip install pygame
```

验证安装是否成功：

```bash
python -c "import pygame; print(pygame.version.ver)"
```

## 教程内容

### 主教程章节（game_dev_quick_start.py）

| 章节 | 主题 | 学习内容 |
|------|------|----------|
| 第1节 | 游戏开发入门 | pygame介绍、游戏循环概念 |
| 第2节 | 创建游戏窗口 | 初始化、窗口、颜色 |
| 第3节 | 绘制图形 | 矩形、圆形、线条、文字 |
| 第4节 | 处理事件 | 键盘、鼠标、退出 |
| 第5节 | 让物体动起来 | 移动原理、速度、边界 |
| 第6节 | 碰撞检测 | 矩形碰撞、圆形碰撞 |
| 第7节 | 接球游戏 | 完整游戏示例 |
| 第8节 | 贪吃蛇 | 完整游戏示例 |

### 游戏示例

| 文件 | 说明 | 难度 |
|------|------|------|
| 01_hello_pygame.py | 创建一个基本的游戏窗口 | 入门 |
| 02_draw_shapes.py | 绘制各种图形和文字 | 入门 |
| 03_moving_ball.py | 让小球移动和反弹 | 简单 |
| 04_keyboard_control.py | 键盘控制角色移动 | 简单 |
| 05_catch_ball.py | 接球小游戏 | 中等 |
| 06_snake.py | 经典贪吃蛇游戏 | 中等 |
| 07_space_shooter.py | 太空射击游戏 | 中等 |

### 练习题

| 编号 | 练习内容 | 难度 |
|------|----------|------|
| 201 | 创建浅蓝色窗口 | 简单 |
| 202 | 可改变背景色的窗口 | 中等 |
| 301 | 绘制房子 | 简单 |
| 302 | 闪烁的圆形 | 中等 |
| 303 | 计分板 | 中等 |
| 401 | 鼠标拖动方块 | 简单 |
| 402 | 键盘控制圆形 | 中等 |
| 501 | 走马灯方块 | 简单 |
| 502 | 圆周运动 | 中等 |
| 601 | 收集金币游戏 | 中等 |
| 99 | 躲避游戏（综合） | 困难 |

## 快速开始

### 运行主教程

```bash
cd /mnt/c/dev/python/qqstudy/game_dev
python game_dev_quick_start.py
```

### 运行练习题

```bash
python game_dev_exercises.py
```

### 运行游戏示例

```bash
# 运行贪吃蛇
python games/06_snake.py

# 运行太空射击
python games/07_space_shooter.py
```

## 游戏控制说明

### 通用控制
- **ESC** - 退出游戏
- **R** - 重新开始（游戏结束时）

### 接球游戏（05_catch_ball.py）
- **左右方向键 / A D** - 移动挡板
- **空格** - 重新开始

### 贪吃蛇（06_snake.py）
- **方向键 / W A S D** - 控制蛇的移动方向
- **空格** - 暂停/继续

### 太空射击（07_space_shooter.py）
- **左右方向键 / A D** - 移动飞船
- **空格** - 发射子弹

## 学习建议

1. **按顺序学习**：建议按照教程章节顺序学习，每节都建立在前一节的基础上。

2. **动手实践**：不要只看代码，要亲自运行和修改！

3. **完成练习**：每节学完后，完成对应的练习题巩固知识。

4. **尝试修改**：尝试修改游戏参数（速度、颜色、大小等），看看会发生什么。

5. **自己创作**：学完教程后，尝试自己创作一个小游戏！

## 常见问题

### Q: 运行时提示 "ModuleNotFoundError: No module named 'pygame'"
A: 需要先安装 pygame：`pip install pygame`

### Q: 游戏窗口太小/太大
A: 可以在代码中修改 `WIDTH` 和 `HEIGHT` 变量来调整窗口大小。

### Q: 游戏运行太快/太慢
A: 可以修改 `clock.tick(60)` 中的数值，或者调整物体的 `speed` 属性。

## 进阶学习

完成本教程后，你可以继续学习：

1. **添加声音**：使用 `pygame.mixer` 添加音效和背景音乐
2. **添加图片**：使用 `pygame.image.load()` 加载和显示图片
3. **动画效果**：学习精灵（Sprite）和动画系统
4. **关卡设计**：创建多个关卡和更复杂的游戏内容
5. **其他游戏类型**：尝试制作平台跳跃、RPG、塔防等类型游戏

## 资源链接

- [Pygame 官方文档](https://www.pygame.org/docs/)
- [Python 官方教程](https://docs.python.org/zh-cn/3/tutorial/)

---

祝你学习愉快，游戏开发有趣！
