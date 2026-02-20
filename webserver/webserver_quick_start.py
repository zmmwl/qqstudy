# ========================================
# Web 服务快速入门教程 (2-3小时学习计划)
# ========================================
# 适合人群：初中生、编程初学者
# 前置要求：已完成 Python 快速入门教程
#
# 建议学习时间分配：
# - 第1-2节：15分钟（概念理解）
# - 第3-4节：25分钟（基础服务器）
# - 第5-6节：30分钟（Flask 路由和参数）
# - 第7-8节：30分钟（模板和表单）
# - 第9-10节：30分钟（数据库集成）
# - 综合练习：30分钟

"""
使用方法：
1. 先安装 Flask：pip install flask
2. 逐节阅读代码
3. 运行代码，打开浏览器访问
4. 完成"练习"部分的题目
5. 阅读注释理解概念

运行方式：
python webserver_quick_start.py
然后打开浏览器访问 http://localhost:5000
"""


# ========================================
# 第1节：什么是 Web 服务？(5分钟)
# ========================================

"""
【用生活中的例子理解 Web 服务】

想象你去餐厅吃饭：
- 你（浏览器/客户端）→ 看菜单、点菜
- 服务员（网络）→ 传递你的请求
- 厨房（服务器）→ 做菜、端出来
- 菜（网页/数据）→ 你看到的结果

【BS 架构 vs CS 架构】

BS（Browser/Server）浏览器/服务器架构：
- 客户端：浏览器（Chrome、Edge、Safari）
- 服务器：运行在远程电脑上的程序
- 优点：不用安装软件，打开浏览器就能用
- 例子：百度、淘宝、bilibili

CS（Client/Server）客户端/服务器架构：
- 客户端：需要安装的软件（QQ、微信、游戏）
- 服务器：远程服务器
- 优点：体验更好、功能更强
- 例子：英雄联盟、Steam、QQ

本教程学习 BS 架构！

【Web 服务的三要素】

1. URL（地址）→ 告诉浏览器去哪里
   例如：https://www.baidu.com/s?wd=你好

   结构：
   https://     www.baidu.com    /s         ?wd=你好
   协议          域名/服务器       路径(页面)   参数(?后面)

   通俗理解：
   - 协议：用哪种语言交流（https是加密的，更安全）
   - 域名：服务器的名字（就像商店招牌）
   - 路径：要访问的页面（商店里的哪个柜台）
   - 参数：传递的具体信息（你要买什么）

2. HTTP（语言）→ 浏览器和服务器怎么对话
   - 请求（Request）：浏览器发给服务器
   - 响应（Response）：服务器返回给浏览器

3. HTML（内容）→ 网页长什么样
   - 浏览器把 HTML 渲染成漂亮的页面
"""

# 练习1：列举你常用的3个网站，分析它们的 URL 结构
# _______________________________________


# ========================================
# 第2节：HTTP 协议基础 (5分钟)
# ========================================

"""
【HTTP 请求方法】

最常用的两个方法：
- GET：获取数据（比如打开网页、搜索）
- POST：提交数据（比如登录、注册、发帖）

【HTTP 状态码】

用数字告诉浏览器发生了什么：
- 200：成功！（一切正常）
- 301/302：重定向（去别的地方）
- 404：找不到！（页面不存在）
- 500：服务器出错！（程序有 bug）

【HTTP 请求和响应的结构】

请求（Request）：
┌─────────────────────────────────┐
│ GET /hello HTTP/1.1             │ ← 请求行
│ Host: localhost:5000            │ ← 请求头
│ User-Agent: Chrome/...          │
│                                 │
│ （请求体，GET 一般没有）           │
└─────────────────────────────────┘

响应（Response）：
┌─────────────────────────────────┐
│ HTTP/1.1 200 OK                 │ ← 状态行
│ Content-Type: text/html         │ ← 响应头
│                                 │
│ <html>Hello World!</html>       │ ← 响应体（网页内容）
└─────────────────────────────────┘
"""


# ========================================
# 第3节：最简单的 Web 服务器 (10分钟)
# ========================================

"""
【Python 内置的简易服务器】

Python 自带一个超简单的 Web 服务器，
只需要一行命令就能启动！

打开终端，进入任意文件夹，运行：
  python -m http.server 8000

然后打开浏览器访问 http://localhost:8000
就能看到当前文件夹的文件列表了！

- localhost = 本机地址（就是你自己电脑）
- 8000 = 端口号（就像门牌号）

【什么是端口？】

一台电脑可以运行很多服务，用端口号区分：
- 就像一栋大楼有很多房间，用门牌号区分

常见端口：
- 80：HTTP 网页（默认，访问时不用写）
- 443：HTTPS 加密网页（默认，访问时不用写）
- 3306：MySQL 数据库
- 5000：Flask 开发服务器（我们要用的）
- 8000：Python 简易服务器

举例：
- http://localhost:5000 = 访问本机的5000端口
- localhost = 127.0.0.1（本机的IP地址）
"""

# 下面用代码创建一个最简单的服务器
# 运行后访问 http://localhost:5001

from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading
import time

def run_simple_server():
    """最简单的 Python Web 服务器"""

    class MyHandler(SimpleHTTPRequestHandler):
        """自定义处理器"""
        def do_GET(self):
            # 根据访问的路径返回不同内容
            if self.path == '/':
                self.send_response(200)  # 状态码 200
                self.send_header('Content-type', 'text/html; charset=utf-8')
                self.end_headers()
                html = """
                <html>
                <head><title>我的第一个网页</title></head>
                <body>
                    <h1>你好，这是我的第一个 Web 服务器！</h1>
                    <p>访问 <a href="/hello">/hello</a> 看看</p>
                    <p>访问 <a href="/time">/time</a> 看当前时间</p>
                </body>
                </html>
                """
                self.wfile.write(html.encode('utf-8'))

            elif self.path == '/hello':
                self.send_response(200)
                self.send_header('Content-type', 'text/html; charset=utf-8')
                self.end_headers()
                self.wfile.write(b'<h1>Hello World!</h1>')

            elif self.path == '/time':
                self.send_response(200)
                self.send_header('Content-type', 'text/html; charset=utf-8')
                self.end_headers()
                current_time = time.strftime('%Y-%m-%d %H:%M:%S')
                html = f'<h1>当前时间：{current_time}</h1>'
                self.wfile.write(html.encode('utf-8'))

            else:
                self.send_response(404)  # 404 找不到
                self.send_header('Content-type', 'text/html; charset=utf-8')
                self.end_headers()
                self.wfile.write(b'<h1>404 - 页面找不到！</h1>')

    # 启动服务器
    server = HTTPServer(('localhost', 5001), MyHandler)
    print("简易服务器启动！访问 http://localhost:5001")
    print("按 Ctrl+C 停止服务器")
    # server.serve_forever()  # 取消注释来运行


# 练习3：运行上面的服务器，访问不同的路径
# _______________________________________


# ========================================
# 第4节：用 Flask 创建 Web 应用 (15分钟)
# ========================================

"""
【什么是 Flask？】

Flask 是一个 Python Web 框架，它帮我们处理了很多复杂的事情：
- 解析 HTTP 请求
- 路由（根据 URL 调用不同的函数）
- 返回响应

【安装 Flask】
pip install flask

【Flask 的核心概念】

1. 路由（Route）：URL 和函数的对应关系
   /hello → hello() 函数
   /time → show_time() 函数

2. 视图函数（View Function）：处理请求的函数

3. 模板（Template）：HTML 文件，可以动态生成内容

4. 静态文件（Static）：CSS、JS、图片等
"""

from flask import Flask, request, redirect, url_for

# 创建 Flask 应用
app = Flask(__name__)


# 【示例4.1】最简单的 Flask 应用
@app.route('/')
def index():
    """首页"""
    return '<h1>欢迎来到我的网站！</h1><p><a href="/hello">问好</a></p>'


# 【示例4.2】不同的路由
@app.route('/hello')
def hello():
    """问候页面"""
    return '<h1>Hello, World!</h1><p><a href="/">返回首页</a></p>'


@app.route('/bye')
def bye():
    """告别页面"""
    return '<h1>再见！</h1><p><a href="/">返回首页</a></p>'


# 【示例4.3】返回不同类型的内容
@app.route('/json')
def json_data():
    """返回 JSON 数据"""
    from flask import jsonify
    data = {
        'name': '小明',
        'age': 14,
        'hobby': ['编程', '游戏', '音乐']
    }
    return jsonify(data)


@app.route('/html')
def html_page():
    """返回 HTML 页面"""
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>我的网页</title>
        <style>
            body { font-family: Arial; margin: 50px; }
            h1 { color: #333; }
            .box { background: #f0f0f0; padding: 20px; border-radius: 10px; }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>这是一个漂亮的网页</h1>
            <p>用 HTML + CSS 制作的</p>
            <a href="/">返回首页</a>
        </div>
    </body>
    </html>
    """
    return html


# 练习4：添加一个新的路由 /about，返回一段自我介绍
# _______________________________________


# ========================================
# 第5节：URL 参数 (10分钟)
# ========================================

"""
【什么是 URL 参数？】

在 URL 中传递数据给服务器，有两种方式：

1. 路径参数：直接写在路径里
   /user/小明        → 路径参数 name = "小明"
   /user/小明/14     → 路径参数 name = "小明", age = 14
   特点：参数是URL的一部分，更简洁

2. 查询参数：用 ? 和 & 连接
   /search?q=Python           → 查询参数 q = "Python"
   /search?q=Python&page=2    → 查询参数 q = "Python", page = "2"
   特点：参数在?后面，用&分隔，适合可选参数

【为什么要用参数？】

让同一个页面显示不同的内容：
- /greet/小明 → 显示"你好，小明！"
- /greet/小红 → 显示"你好，小红！"
"""


# 【示例5.1】路径参数
@app.route('/greet/<name>')
def greet(name):
    """
    路径参数：<name> 会匹配 URL 中的那部分

    访问方式：
    /greet/小明 → name = "小明"
    /greet/小红 → name = "小红"
    """
    return f'<h1>你好，{name}！</h1><p><a href="/">返回首页</a></p>'


@app.route('/user/<name>/<int:age>')
def user_info(name, age):
    """
    多个参数，并且指定类型

    <int:age> 表示 age 必须是整数

    访问方式：
    /user/小明/14 → name = "小明", age = 14
    """
    return f'''
    <h1>用户信息</h1>
    <p>姓名：{name}</p>
    <p>年龄：{age}</p>
    <p>明年：{age + 1}岁</p>
    <p><a href="/">返回首页</a></p>
    '''


# 【示例5.2】查询参数
@app.route('/search')
def search():
    """
    查询参数：URL 中 ? 后面的部分

    访问方式：
    /search?q=Python
    /search?q=Flask&page=2

    使用 request.args.get('参数名') 获取
    """
    keyword = request.args.get('q', '')  # 获取 q 参数，默认为空字符串
    page = request.args.get('page', '1')  # 获取 page 参数，默认为 '1'

    if keyword:
        return f'''
        <h1>搜索结果</h1>
        <p>关键词：{keyword}</p>
        <p>页码：{page}</p>
        <p>（这里显示搜索结果...）</p>
        <p><a href="/">返回首页</a></p>
        '''
    else:
        return '''
        <h1>搜索</h1>
        <p>请在 URL 中添加 ?q=关键词</p>
        <p>例如：<a href="/search?q=Python">/search?q=Python</a></p>
        <p><a href="/">返回首页</a></p>
        '''


@app.route('/calculator')
def calculator():
    """
    综合示例：简易计算器

    访问方式：
    /calculator?a=10&b=5&op=add
    """
    a = request.args.get('a', '0')
    b = request.args.get('b', '0')
    op = request.args.get('op', 'add')

    try:
        a = float(a)
        b = float(b)

        if op == 'add':
            result = a + b
            symbol = '+'
        elif op == 'sub':
            result = a - b
            symbol = '-'
        elif op == 'mul':
            result = a * b
            symbol = '×'
        elif op == 'div':
            result = a / b if b != 0 else '错误：不能除以0'
            symbol = '÷'
        else:
            result = '未知操作'
            symbol = '?'

        return f'''
        <h1>计算结果</h1>
        <p>{a} {symbol} {b} = {result}</p>
        <p>
            <a href="/calculator?a=10&b=5&op=add">10+5</a> |
            <a href="/calculator?a=10&b=5&op=sub">10-5</a> |
            <a href="/calculator?a=10&b=5&op=mul">10×5</a> |
            <a href="/calculator?a=10&b=5&op=div">10÷5</a>
        </p>
        <p><a href="/">返回首页</a></p>
        '''
    except ValueError:
        return '<h1>错误</h1><p>请输入有效的数字！</p>'


# 练习5：创建一个路由 /square/<int:n>，返回 n 的平方
# _______________________________________


# ========================================
# 第6节：HTTP 方法 - GET 和 POST (15分钟)
# ========================================

"""
【GET vs POST】

GET：
- 用于获取数据
- 参数在 URL 中（?name=value）
- 可以收藏、分享链接
- 例子：搜索、查看商品

POST：
- 用于提交数据
- 参数在请求体中（不在 URL 显示）
- 更安全（适合密码等敏感信息）
- 例子：登录、注册、发帖

【Flask 中处理不同的方法】
使用 methods 参数指定路由支持的方法
"""


# 【示例6.1】GET 请求
@app.route('/login', methods=['GET'])
def login_get():
    """显示登录表单（GET 请求）"""
    return '''
    <h1>登录</h1>
    <form method="POST" action="/login">
        <p>
            用户名：<input type="text" name="username" required>
        </p>
        <p>
            密码：<input type="password" name="password" required>
        </p>
        <p>
            <button type="submit">登录</button>
        </p>
    </form>
    <p><a href="/">返回首页</a></p>
    '''


# 【示例6.2】POST 请求
@app.route('/login', methods=['POST'])
def login_post():
    """处理登录表单（POST 请求）"""
    username = request.form.get('username')  # POST 数据用 request.form
    password = request.form.get('password')

    # 模拟验证（实际项目中要查数据库）
    if username == 'admin' and password == '123456':
        return f'''
        <h1>登录成功！</h1>
        <p>欢迎，{username}！</p>
        <p><a href="/">返回首页</a></p>
        '''
    else:
        return '''
        <h1>登录失败</h1>
        <p>用户名或密码错误！</p>
        <p>提示：用户名 admin，密码 123456</p>
        <p><a href="/login">重新登录</a></p>
        '''


# 【示例6.3】同一个路由处理 GET 和 POST
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    """
    一个函数处理两种请求

    GET：显示表单
    POST：处理表单提交
    """
    if request.method == 'GET':
        # 显示表单
        return '''
        <h1>意见反馈</h1>
        <form method="POST">
            <p>
                姓名：<input type="text" name="name" required>
            </p>
            <p>
                邮箱：<input type="email" name="email">
            </p>
            <p>
                反馈内容：<br>
                <textarea name="content" rows="5" cols="30" required></textarea>
            </p>
            <p>
                <button type="submit">提交</button>
            </p>
        </form>
        <p><a href="/">返回首页</a></p>
        '''

    else:  # POST
        # 处理表单
        name = request.form.get('name')
        email = request.form.get('email')
        content = request.form.get('content')

        return f'''
        <h1>感谢您的反馈！</h1>
        <div style="background:#f0f0f0;padding:20px;border-radius:10px;">
            <p><strong>姓名：</strong>{name}</p>
            <p><strong>邮箱：</strong>{email}</p>
            <p><strong>内容：</strong>{content}</p>
        </div>
        <p><a href="/feedback">继续反馈</a> | <a href="/">返回首页</a></p>
        '''


# 练习6：创建一个注册页面，包含用户名、密码、确认密码
# _______________________________________


# ========================================
# 第7节：模板 - Jinja2 (15分钟)
# ========================================

"""
【为什么需要模板？】

之前的代码把 HTML 写在 Python 字符串里，很乱！

模板可以把 HTML 和 Python 代码分开：
- HTML 文件放在 templates 文件夹
- Python 代码专注于逻辑
- 用 {{ 变量 }} 在 HTML 中显示数据

【Jinja2 模板语法】

显示变量：{{ name }}
条件判断：{% if condition %} ... {% endif %}
循环：{% for item in items %} ... {% endfor %}
"""

from flask import render_template_string, render_template

# 为了让教程可以在一个文件中运行，使用 render_template_string
# 实际项目中使用 render_template('xxx.html')

# 【示例7.1】基础模板
@app.route('/template/basic')
def template_basic():
    """基础模板示例"""
    name = '小明'
    age = 14

    # 实际项目中，这个 HTML 应该放在 templates 文件夹
    template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>模板示例</title>
        <style>
            body { font-family: Arial; margin: 50px; }
            .info { background: #e8f4fd; padding: 20px; border-radius: 10px; }
        </style>
    </head>
    <body>
        <h1>用户信息</h1>
        <div class="info">
            <p>姓名：{{ name }}</p>
            <p>年龄：{{ age }}</p>
            <p>明年：{{ age + 1 }} 岁</p>
        </div>
        <p><a href="/">返回首页</a></p>
    </body>
    </html>
    '''

    return render_template_string(template, name=name, age=age)


# 【示例7.2】条件判断
@app.route('/template/if/<int:score>')
def template_if(score):
    """模板中的条件判断"""
    template = '''
    <h1>成绩查询</h1>
    <p>你的分数：{{ score }} 分</p>

    {% if score >= 90 %}
        <p style="color: green;">优秀！继续保持！</p>
    {% elif score >= 80 %}
        <p style="color: blue;">良好！再接再厉！</p>
    {% elif score >= 60 %}
        <p style="color: orange;">及格！还需努力！</p>
    {% else %}
        <p style="color: red;">不及格！要加油了！</p>
    {% endif %}

    <p><a href="/">返回首页</a></p>
    '''
    return render_template_string(template, score=score)


# 【示例7.3】循环
@app.route('/template/loop')
def template_loop():
    """模板中的循环"""
    students = [
        {'name': '小明', 'score': 95},
        {'name': '小红', 'score': 88},
        {'name': '小刚', 'score': 72},
        {'name': '小芳', 'score': 91},
        {'name': '小强', 'score': 65},
    ]

    template = '''
    <h1>学生成绩表</h1>
    <table border="1" cellpadding="10" style="border-collapse: collapse;">
        <tr style="background: #f0f0f0;">
            <th>排名</th>
            <th>姓名</th>
            <th>成绩</th>
            <th>等级</th>
        </tr>
        {% for student in students %}
        <tr>
            <td>{{ loop.index }}</td>
            <td>{{ student.name }}</td>
            <td>{{ student.score }}</td>
            <td>
                {% if student.score >= 90 %}
                    优秀
                {% elif student.score >= 80 %}
                    良好
                {% elif student.score >= 60 %}
                    及格
                {% else %}
                    不及格
                {% endif %}
            </td>
        </tr>
        {% endfor %}
    </table>

    <h3>统计信息</h3>
    <p>总人数：{{ students|length }} 人</p>
    <!-- students|length 表示获取students列表的长度 -->
    <!-- | 叫做"过滤器"，length是统计数量的过滤器 -->

    <p><a href="/">返回首页</a></p>
    '''
    return render_template_string(template, students=students)


# 【示例7.4】模板继承（进阶）
@app.route('/template/extend')
def template_extend():
    """模板继承示例"""
    # 父模板
    base_template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>{% block title %}默认标题{% endblock %}</title>
        <style>
            body { font-family: Arial; margin: 0; }
            nav { background: #333; color: white; padding: 15px; }
            nav a { color: white; margin-right: 20px; text-decoration: none; }
            .content { padding: 20px; }
            footer { background: #f0f0f0; padding: 10px; text-align: center; }
        </style>
    </head>
    <body>
        <nav>
            <a href="/">首页</a>
            <a href="/template/extend">模板示例</a>
            <a href="/hello">Hello</a>
        </nav>
        <div class="content">
            {% block content %}
            <h1>默认内容</h1>
            {% endblock %}
        </div>
        <footer>
            <p>© 2024 我的网站</p>
        </footer>
    </body>
    </html>
    '''

    # 子模板（继承父模板）
    child_template = '''
    {% extends base %}

    {% block title %}模板继承示例{% endblock %}

    {% block content %}
    <h1>欢迎！</h1>
    <p>这是通过模板继承生成的页面。</p>
    <ul>
        <li>导航栏和页脚在父模板中定义</li>
        <li>只有中间的内容在子模板中定义</li>
        <li>这样可以保持网站风格统一</li>
    </ul>
    {% endblock %}
    '''

    return render_template_string(child_template, base=base_template)


# 练习7：创建一个商品列表页面，显示商品名称、价格、库存
# _______________________________________


# ========================================
# 第8节：表单和文件上传 (15分钟)
# ========================================

"""
【HTML 表单】

表单是用户输入数据的界面：
- 文本框：<input type="text">
- 密码框：<input type="password">
- 单选框：<input type="radio">
- 复选框：<input type="checkbox">
- 下拉框：<select>
- 文本域：<textarea>
- 文件上传：<input type="file">
"""

import os
from werkzeug.utils import secure_filename

# 配置文件上传
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# 确保上传文件夹存在
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    """检查文件类型是否允许"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# 【示例8.1】综合表单
@app.route('/form', methods=['GET', 'POST'])
def form_demo():
    """综合表单示例"""
    if request.method == 'GET':
        return '''
        <h1>综合表单示例</h1>
        <form method="POST" style="max-width: 500px;">
            <fieldset>
                <legend>基本信息</legend>
                <p>
                    姓名：<input type="text" name="name" required>
                </p>
                <p>
                    性别：
                    <input type="radio" name="gender" value="M" checked> 男
                    <input type="radio" name="gender" value="F"> 女
                </p>
                <p>
                    年龄：<input type="number" name="age" min="1" max="150">
                </p>
            </fieldset>

            <fieldset>
                <legend>联系方式</legend>
                <p>
                    邮箱：<input type="email" name="email">
                </p>
                <p>
                    电话：<input type="tel" name="phone">
                </p>
            </fieldset>

            <fieldset>
                <legend>其他</legend>
                <p>
                    爱好：
                    <input type="checkbox" name="hobby" value="reading"> 阅读
                    <input type="checkbox" name="hobby" value="gaming"> 游戏
                    <input type="checkbox" name="hobby" value="music"> 音乐
                    <input type="checkbox" name="hobby" value="sports"> 运动
                </p>
                <p>
                    年级：
                    <select name="grade">
                        <option value="7">七年级</option>
                        <option value="8">八年级</option>
                        <option value="9">九年级</option>
                    </select>
                </p>
                <p>
                    自我介绍：<br>
                    <textarea name="intro" rows="4" cols="40"></textarea>
                </p>
            </fieldset>

            <p>
                <button type="submit">提交</button>
                <button type="reset">重置</button>
            </p>
        </form>
        <p><a href="/">返回首页</a></p>
        '''

    else:  # POST
        name = request.form.get('name')
        gender = request.form.get('gender')
        age = request.form.get('age')
        email = request.form.get('email')
        phone = request.form.get('phone')
        hobbies = request.form.getlist('hobby')  # 复选框用 getlist
        grade = request.form.get('grade')
        intro = request.form.get('intro')

        gender_text = '男' if gender == 'M' else '女'
        grade_text = {'7': '七年级', '8': '八年级', '9': '九年级'}.get(grade, '未知')

        return f'''
        <h1>表单提交结果</h1>
        <table border="1" cellpadding="10" style="border-collapse: collapse;">
            <tr><th>项目</th><th>内容</th></tr>
            <tr><td>姓名</td><td>{name}</td></tr>
            <tr><td>性别</td><td>{gender_text}</td></tr>
            <tr><td>年龄</td><td>{age}</td></tr>
            <tr><td>邮箱</td><td>{email}</td></tr>
            <tr><td>电话</td><td>{phone}</td></tr>
            <tr><td>爱好</td><td>{', '.join(hobbies) if hobbies else '无'}</td></tr>
            <tr><td>年级</td><td>{grade_text}</td></tr>
            <tr><td>自我介绍</td><td>{intro or '无'}</td></tr>
        </table>
        <p><a href="/form">重新填写</a> | <a href="/">返回首页</a></p>
        '''


# 【示例8.2】文件上传
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    """文件上传示例"""
    if request.method == 'GET':
        return '''
        <h1>文件上传</h1>
        <form method="POST" enctype="multipart/form-data">
            <p>
                选择文件：
                <input type="file" name="file">
            </p>
            <p>
                <button type="submit">上传</button>
            </p>
        </form>
        <p>支持的文件类型：txt, pdf, png, jpg, jpeg, gif</p>
        <p><a href="/">返回首页</a></p>
        '''

    else:  # POST
        # 检查是否有文件
        if 'file' not in request.files:
            return '<h1>错误</h1><p>没有选择文件！</p>'

        file = request.files['file']

        # 检查文件名是否为空
        if file.filename == '':
            return '<h1>错误</h1><p>没有选择文件！</p>'

        # 检查文件类型并保存
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)  # 安全处理文件名
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            return f'''
            <h1>上传成功！</h1>
            <p>文件名：{filename}</p>
            <p>保存位置：{filepath}</p>
            <p><a href="/upload">继续上传</a> | <a href="/">返回首页</a></p>
            '''
        else:
            return '<h1>错误</h1><p>不支持的文件类型！</p>'


# 练习8：创建一个问卷调查表单，至少包含5个不同类型的输入
# _______________________________________


# ========================================
# 第9节：连接数据库 (15分钟)
# ========================================

"""
【Web 服务 + 数据库】

实际网站都需要存储数据：
- 用户信息
- 商品信息
- 订单记录
- 文章内容

Flask 可以轻松连接 MySQL 数据库！
"""

# 【示例9.1】模拟数据库（内存中的数据）
# 实际项目中使用真正的数据库

# 模拟的学生数据
students_db = [
    {'id': 1, 'name': '小明', 'gender': 'M', 'age': 14, 'class': '七年级1班', 'score': 95.5},
    {'id': 2, 'name': '小红', 'gender': 'F', 'age': 13, 'class': '七年级1班', 'score': 98.0},
    {'id': 3, 'name': '小刚', 'gender': 'M', 'age': 14, 'class': '七年级2班', 'score': 88.5},
    {'id': 4, 'name': '小芳', 'gender': 'F', 'age': 13, 'class': '七年级1班', 'score': 92.0},
    {'id': 5, 'name': '小强', 'gender': 'M', 'age': 15, 'class': '七年级2班', 'score': 75.5},
]

next_id = 6  # 下一个学生的 ID


@app.route('/students')
def student_list():
    """学生列表（从"数据库"读取）"""
    template = '''
    <h1>学生列表</h1>
    <p><a href="/students/add">添加学生</a></p>

    {% if students %}
    <table border="1" cellpadding="10" style="border-collapse: collapse;">
        <tr style="background: #f0f0f0;">
            <th>ID</th>
            <th>姓名</th>
            <th>性别</th>
            <th>年龄</th>
            <th>班级</th>
            <th>成绩</th>
            <th>操作</th>
        </tr>
        {% for student in students %}
        <tr>
            <td>{{ student.id }}</td>
            <td>{{ student.name }}</td>
            <td>{{ '男' if student.gender == 'M' else '女' }}</td>
            <td>{{ student.age }}</td>
            <td>{{ student.class }}</td>
            <td>{{ student.score }}</td>
            <td>
                <a href="/students/{{ student.id }}">查看</a>
                <a href="/students/{{ student.id }}/edit">编辑</a>
                <a href="/students/{{ student.id }}/delete" onclick="return confirm('确定删除？')">删除</a>
            </td>
        </tr>
        {% endfor %}
    </table>
    {% else %}
    <p>暂无学生数据</p>
    {% endif %}

    <p><a href="/">返回首页</a></p>
    '''
    return render_template_string(template, students=students_db)


@app.route('/students/<int:student_id>')
def student_detail(student_id):
    """学生详情"""
    # next() 是Python内置函数，从迭代器中获取第一个满足条件的元素
    # (s for s in students_db if s['id'] == student_id) 是生成器表达式
    # 整句意思：从students_db中找到第一个id等于student_id的学生
    # 如果找不到，返回 None（第二个参数）
    student = next((s for s in students_db if s['id'] == student_id), None)

    if not student:
        return '<h1>404</h1><p>学生不存在！</p>'

    template = '''
    <h1>学生详情</h1>
    <table border="1" cellpadding="10" style="border-collapse: collapse;">
        <tr><th>ID</th><td>{{ student.id }}</td></tr>
        <tr><th>姓名</th><td>{{ student.name }}</td></tr>
        <tr><th>性别</th><td>{{ '男' if student.gender == 'M' else '女' }}</td></tr>
        <tr><th>年龄</th><td>{{ student.age }}</td></tr>
        <tr><th>班级</th><td>{{ student.class }}</td></tr>
        <tr><th>成绩</th><td>{{ student.score }}</td></tr>
    </table>
    <p>
        <a href="/students/{{ student.id }}/edit">编辑</a>
        <a href="/students">返回列表</a>
    </p>
    '''
    return render_template_string(template, student=student)


@app.route('/students/add', methods=['GET', 'POST'])
def student_add():
    """添加学生"""
    global next_id

    if request.method == 'GET':
        return '''
        <h1>添加学生</h1>
        <form method="POST">
            <p>姓名：<input type="text" name="name" required></p>
            <p>性别：
                <input type="radio" name="gender" value="M" checked> 男
                <input type="radio" name="gender" value="F"> 女
            </p>
            <p>年龄：<input type="number" name="age" min="1" max="150"></p>
            <p>班级：<input type="text" name="class_name" value="七年级1班"></p>
            <p>成绩：<input type="number" name="score" step="0.1" min="0" max="100"></p>
            <p><button type="submit">添加</button></p>
        </form>
        <p><a href="/students">返回列表</a></p>
        '''

    else:  # POST
        new_student = {
            'id': next_id,
            'name': request.form.get('name'),
            'gender': request.form.get('gender'),
            'age': int(request.form.get('age', 0)),
            'class': request.form.get('class_name'),
            'score': float(request.form.get('score', 0)),
        }
        students_db.append(new_student)
        next_id += 1

        return f'''
        <h1>添加成功！</h1>
        <p>学生 {new_student['name']} 已添加</p>
        <p><a href="/students">返回列表</a></p>
        '''


@app.route('/students/<int:student_id>/edit', methods=['GET', 'POST'])
def student_edit(student_id):
    """编辑学生"""
    global students_db
    student = next((s for s in students_db if s['id'] == student_id), None)

    if not student:
        return '<h1>404</h1><p>学生不存在！</p>'

    if request.method == 'GET':
        return f'''
        <h1>编辑学生</h1>
        <form method="POST">
            <p>姓名：<input type="text" name="name" value="{student['name']}" required></p>
            <p>性别：
                <input type="radio" name="gender" value="M" {'checked' if student['gender']=='M' else ''}> 男
                <input type="radio" name="gender" value="F" {'checked' if student['gender']=='F' else ''}> 女
            </p>
            <p>年龄：<input type="number" name="age" value="{student['age']}" min="1" max="150"></p>
            <p>班级：<input type="text" name="class_name" value="{student['class']}"></p>
            <p>成绩：<input type="number" name="score" value="{student['score']}" step="0.1" min="0" max="100"></p>
            <p><button type="submit">保存</button></p>
        </form>
        <p><a href="/students">返回列表</a></p>
        '''

    else:  # POST
        student['name'] = request.form.get('name')
        student['gender'] = request.form.get('gender')
        student['age'] = int(request.form.get('age', 0))
        student['class'] = request.form.get('class_name')
        student['score'] = float(request.form.get('score', 0))

        return f'''
        <h1>修改成功！</h1>
        <p>学生 {student['name']} 的信息已更新</p>
        <p><a href="/students">返回列表</a></p>
        '''


@app.route('/students/<int:student_id>/delete')
def student_delete(student_id):
    """删除学生"""
    global students_db
    students_db = [s for s in students_db if s['id'] != student_id]

    return '''
    <h1>删除成功！</h1>
    <p><a href="/students">返回列表</a></p>
    '''


# 练习9：为学生管理系统添加"按班级筛选"功能
# _______________________________________


# ========================================
# 第10节：API 接口 (10分钟)
# ========================================

"""
【什么是 API？】

API（Application Programming Interface）= 应用程序接口

用生活中的例子理解：
- 餐厅点餐：你（前端）告诉服务员（API）要什么菜
- 服务员把菜单给厨房（后端），厨房做好后通过服务员给你
- API 就是"服务员"，负责传递信息

让不同的程序可以互相"对话"：
- 前端（网页/手机App）发送请求
- 后端（服务器）返回数据（通常是 JSON 格式）

【RESTful API 是什么？】

RESTful 是一种设计 API 的风格，让 API 更规范、更易懂：
- 用名词表示资源：/students（学生资源）
- 用动词（HTTP方法）表示操作：GET获取、POST创建、PUT更新、DELETE删除

对照表：
- GET    /api/students     → 获取学生列表（查）
- GET    /api/students/1   → 获取ID为1的学生（查）
- POST   /api/students     → 创建新学生（增）
- PUT    /api/students/1   → 更新ID为1的学生（改）
- DELETE /api/students/1   → 删除ID为1的学生（删）

其实就是数据库的"增删改查"！
"""

from flask import jsonify

# API 路由前缀
API_PREFIX = '/api'


@app.route(f'{API_PREFIX}/students')
def api_get_students():
    """获取学生列表（API）"""
    return jsonify({
        'success': True,
        'data': students_db,
        'total': len(students_db)
    })


@app.route(f'{API_PREFIX}/students/<int:student_id>')
def api_get_student(student_id):
    """获取单个学生（API）"""
    student = next((s for s in students_db if s['id'] == student_id), None)

    if student:
        return jsonify({
            'success': True,
            'data': student
        })
    else:
        return jsonify({
            'success': False,
            'message': '学生不存在'
        }), 404


@app.route(f'{API_PREFIX}/students', methods=['POST'])
def api_create_student():
    """创建学生（API）"""
    global next_id

    data = request.get_json()

    new_student = {
        'id': next_id,
        'name': data.get('name'),
        'gender': data.get('gender', 'M'),
        'age': data.get('age', 0),
        'class': data.get('class_name', ''),
        'score': data.get('score', 0),
    }
    students_db.append(new_student)
    next_id += 1

    return jsonify({
        'success': True,
        'message': '创建成功',
        'data': new_student
    }), 201


@app.route(f'{API_PREFIX}/students/<int:student_id>', methods=['PUT'])
def api_update_student(student_id):
    """更新学生（API）"""
    student = next((s for s in students_db if s['id'] == student_id), None)

    if not student:
        return jsonify({
            'success': False,
            'message': '学生不存在'
        }), 404

    data = request.get_json()

    student['name'] = data.get('name', student['name'])
    student['gender'] = data.get('gender', student['gender'])
    student['age'] = data.get('age', student['age'])
    student['class'] = data.get('class_name', student['class'])
    student['score'] = data.get('score', student['score'])

    return jsonify({
        'success': True,
        'message': '更新成功',
        'data': student
    })


@app.route(f'{API_PREFIX}/students/<int:student_id>', methods=['DELETE'])
def api_delete_student(student_id):
    """删除学生（API）"""
    global students_db
    student = next((s for s in students_db if s['id'] == student_id), None)

    if not student:
        return jsonify({
            'success': False,
            'message': '学生不存在'
        }), 404

    students_db = [s for s in students_db if s['id'] != student_id]

    return jsonify({
        'success': True,
        'message': '删除成功'
    })


# API 测试页面
@app.route('/api-test')
def api_test():
    """API 测试页面"""
    return '''
    <h1>API 测试页面</h1>

    <h3>1. 获取学生列表</h3>
    <button onclick="testGetStudents()">GET /api/students</button>

    <h3>2. 获取单个学生</h3>
    <button onclick="testGetStudent()">GET /api/students/1</button>

    <h3>3. 创建学生</h3>
    <button onclick="testCreateStudent()">POST /api/students</button>

    <h3>4. 更新学生</h3>
    <button onclick="testUpdateStudent()">PUT /api/students/1</button>

    <h3>5. 删除学生</h3>
    <button onclick="testDeleteStudent()">DELETE /api/students/1</button>

    <h3>返回结果：</h3>
    <pre id="result" style="background: #f0f0f0; padding: 15px; min-height: 100px;"></pre>

    <script>
    function showResult(data) {
        document.getElementById('result').textContent = JSON.stringify(data, null, 2);
    }

    async function testGetStudents() {
        const response = await fetch('/api/students');
        const data = await response.json();
        showResult(data);
    }

    async function testGetStudent() {
        const response = await fetch('/api/students/1');
        const data = await response.json();
        showResult(data);
    }

    async function testCreateStudent() {
        const response = await fetch('/api/students', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                name: '新学生',
                gender: 'M',
                age: 14,
                class_name: '七年级1班',
                score: 85.5
            })
        });
        const data = await response.json();
        showResult(data);
    }

    async function testUpdateStudent() {
        const response = await fetch('/api/students/1', {
            method: 'PUT',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                name: '小明（已修改）',
                score: 99
            })
        });
        const data = await response.json();
        showResult(data);
    }

    async function testDeleteStudent() {
        const response = await fetch('/api/students/1', {
            method: 'DELETE'
        });
        const data = await response.json();
        showResult(data);
    }
    </script>

    <p><a href="/">返回首页</a></p>
    '''


# 练习10：为 API 添加"按班级搜索"功能
# _______________________________________


# ========================================
# 首页导航
# ========================================

@app.route('/')
def home():
    """教程首页"""
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Web 服务快速入门教程</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 800px; margin: 50px auto; padding: 20px; }
            h1 { color: #333; border-bottom: 2px solid #333; padding-bottom: 10px; }
            .section { background: #f9f9f9; padding: 20px; margin: 20px 0; border-radius: 10px; }
            .section h2 { margin-top: 0; color: #2196F3; }
            ul { line-height: 2; }
            a { color: #2196F3; text-decoration: none; }
            a:hover { text-decoration: underline; }
            .tag { background: #e0e0e0; padding: 2px 8px; border-radius: 3px; font-size: 12px; }
        </style>
    </head>
    <body>
        <h1>Web 服务快速入门教程</h1>
        <p>适合初中生的 Web 开发教程，简单、快速、易懂、边学边练！</p>

        <div class="section">
            <h2>第3-4节：基础服务器</h2>
            <ul>
                <li><a href="/hello">/hello</a> <span class="tag">路由</span></li>
                <li><a href="/json">/json</a> <span class="tag">JSON</span></li>
                <li><a href="/html">/html</a> <span class="tag">HTML</span></li>
            </ul>
        </div>

        <div class="section">
            <h2>第5节：URL 参数</h2>
            <ul>
                <li><a href="/greet/小明">/greet/小明</a> <span class="tag">路径参数</span></li>
                <li><a href="/user/小红/14">/user/小红/14</a> <span class="tag">多参数</span></li>
                <li><a href="/search?q=Python">/search?q=Python</a> <span class="tag">查询参数</span></li>
                <li><a href="/calculator?a=10&b=5&op=add">/calculator?a=10&b=5&op=add</a> <span class="tag">综合</span></li>
            </ul>
        </div>

        <div class="section">
            <h2>第6节：GET 和 POST</h2>
            <ul>
                <li><a href="/login">/login</a> <span class="tag">登录表单</span></li>
                <li><a href="/feedback">/feedback</a> <span class="tag">反馈表单</span></li>
            </ul>
        </div>

        <div class="section">
            <h2>第7节：模板</h2>
            <ul>
                <li><a href="/template/basic">/template/basic</a> <span class="tag">基础模板</span></li>
                <li><a href="/template/if/85">/template/if/85</a> <span class="tag">条件判断</span></li>
                <li><a href="/template/loop">/template/loop</a> <span class="tag">循环</span></li>
                <li><a href="/template/extend">/template/extend</a> <span class="tag">模板继承</span></li>
            </ul>
        </div>

        <div class="section">
            <h2>第8节：表单</h2>
            <ul>
                <li><a href="/form">/form</a> <span class="tag">综合表单</span></li>
                <li><a href="/upload">/upload</a> <span class="tag">文件上传</span></li>
            </ul>
        </div>

        <div class="section">
            <h2>第9节：数据库</h2>
            <ul>
                <li><a href="/students">/students</a> <span class="tag">学生管理</span></li>
            </ul>
        </div>

        <div class="section">
            <h2>第10节：API</h2>
            <ul>
                <li><a href="/api/students">/api/students</a> <span class="tag">JSON API</span></li>
                <li><a href="/api-test">/api-test</a> <span class="tag">API 测试</span></li>
            </ul>
        </div>
    </body>
    </html>
    '''


# ========================================
# 运行服务器
# ========================================

if __name__ == '__main__':
    print("=" * 50)
    print("Web 服务快速入门教程")
    print("=" * 50)
    print()
    print("1. 安装 Flask：pip install flask")
    print("2. 打开浏览器访问：http://localhost:5000")
    print("3. 按 Ctrl+C 停止服务器")
    print()
    print("=" * 50)

    # 启动 Flask 开发服务器
    # debug=True 表示开启调试模式，修改代码后自动重启
    app.run(host='localhost', port=5000, debug=True)


# ========================================
# 学习建议
# ========================================
"""
【重要知识点总结】

1. Web 服务三要素：
   - URL（地址）
   - HTTP（协议）
   - HTML（内容）

2. HTTP 方法：
   - GET：获取数据
   - POST：提交数据

3. Flask 核心：
   - 路由（@app.route）
   - 请求（request）
   - 响应（return）
   - 模板（render_template）

4. 常见状态码：
   - 200：成功
   - 404：找不到
   - 500：服务器错误

【学习口诀】

路由决定去哪里，请求带来用户意
模板渲染成网页，响应返回给浏览器
GET获取POST提交，状态码告诉你结果

【进阶学习方向】

1. 前端基础
   - HTML（结构）
   - CSS（样式）
   - JavaScript（交互）

2. 数据库集成
   - Flask-SQLAlchemy
   - Flask-Migrate

3. 用户认证
   - Flask-Login
   - 密码加密

4. 部署上线
   - Gunicorn
   - Nginx
   - 云服务器

【推荐资源】

- Flask 官方文档：https://flask.palletsprojects.com/
- MDN Web 教程：https://developer.mozilla.org/zh-CN/
- 菜鸟教程：https://www.runoob.com/

【下一步建议】

1. 完成本教程的所有练习
2. 学习 HTML/CSS/JavaScript 基础
3. 做一个小项目（如：待办事项、博客）
4. 学习数据库集成
5. 尝试部署到云服务器
"""
