# ========================================
# Web 服务练习题集
# ========================================
# 完成这些练习来巩固你的 Web 开发技能！
# 建议先自己思考，实在不会再看答案

from flask import Flask, request, render_template_string, jsonify

app = Flask(__name__)


# ========================================
# 第1关：基础路由（共8题）
# ========================================

"""
练习说明：
根据题目要求，在下面编写 Flask 路由代码
"""

# 题1.1：创建一个路由 /hi，返回 "你好，世界！"
# 你的答案：
# @app.route('/hi')
# def hi():
#     return '你好，世界！'


# 题1.2：创建一个路由 /date，返回当前日期（格式：2024-01-15）
# 提示：import datetime; datetime.date.today()
# 你的答案：




# 题1.3：创建一个路由 /random，返回一个1-100的随机数
# 提示：import random; random.randint(1, 100)
# 你的答案：




# 题1.4：创建一个路由 /pages/about，返回 "关于我们" 页面
# 你的答案：




# 题1.5：创建一个路由返回 JSON 格式的数据
# 包含：name, age, city 三个字段
# 你的答案：




# 题1.6：创建一个路由 /redirect-test，重定向到 /hi
# 提示：from flask import redirect, url_for
# 你的答案：




# 题1.7：创建一个路由返回带有 CSS 样式的 HTML 页面
# 要求：标题是蓝色，段落是灰色
# 你的答案：




# 题1.8：创建一个路由 /headers，显示请求头中的 User-Agent
# 提示：request.headers.get('User-Agent')
# 你的答案：




# ========================================
# 第2关：URL 参数（共6题）
# ========================================

# 题2.1：创建路由 /square/<int:n>，返回 n 的平方
# 例如：/square/5 → 25
# 你的答案：




# 题2.2：创建路由 /greet/<name>/<int:times>
# 返回对 name 说 times 次你好
# 例如：/greet/小明/3 → "小明你好！小明你好！小明你好！"
# 你的答案：




# 题2.3：创建路由 /calculate/<int:a>/<operation>/<int:b>
# 支持：add(+), sub(-), mul(*), div(/)
# 例如：/calculate/10/add/5 → 15
# 你的答案：




# 题2.4：创建路由 /items，使用查询参数 ?page=n
# 返回 "第 n 页"
# 例如：/items?page=3 → "第 3 页"
# 你的答案：




# 题2.5：创建路由 /profile，支持多个查询参数
# name, age, city（都有默认值）
# 例如：/profile?name=小明&age=14&city=北京
# 你的答案：




# 题2.6：创建路由 /fibonacci/<int:n>
# 返回斐波那契数列的前 n 项
# 斐波那契：1, 1, 2, 3, 5, 8, 13, 21...
# 你的答案：




# ========================================
# 第3关：表单处理（共5题）
# ========================================

# 题3.1：创建一个简单的加法计算器
# GET：显示两个输入框
# POST：显示计算结果
# 你的答案：




# 题3.2：创建一个温度转换器
# 摄氏度 ↔ 华氏度
# 公式：F = C * 9/5 + 32
# 你的答案：




# 题3.3：创建一个 BMI 计算器
# 输入：身高(cm)、体重(kg)
# 输出：BMI 值和体型评价
# BMI = 体重(kg) / 身高(m)²
# 你的答案：




# 题3.4：创建一个简单登录页面
# 用户名：admin，密码：123456
# 显示登录成功或失败
# 你的答案：




# 题3.5：创建一个留言板
# 支持添加留言和显示所有留言
# 用列表存储留言（模拟数据库）
# 你的答案：




# ========================================
# 第4关：模板使用（共5题）
# ========================================

# 题4.1：使用模板显示学生信息
# 学生数据：name, age, grade, score
# 你的答案：




# 题4.2：使用模板循环显示九九乘法表
# 你的答案：




# 题4.3：使用模板条件判断显示成绩等级
# 输入分数，显示：优秀/良好/及格/不及格
# 你的答案：




# 题4.4：创建一个带导航栏的页面
# 导航栏包含：首页、关于、联系
# 所有页面共享同一个导航栏（模板继承）
# 你的答案：




# 题4.5：使用模板过滤器
# 显示一个列表，用 join 过滤器连接
# 显示一个数字，用 round 过滤器保留2位小数
# 你的答案：




# ========================================
# 第5关：综合挑战（共4题）
# ========================================

# 题5.1：创建一个简单的待办事项（Todo）应用
# 功能：添加、显示、删除待办事项
# 你的答案：




# 题5.2：创建一个简单的计数器 API
# GET /counter：返回当前计数
# POST /counter/increase：计数+1
# POST /counter/decrease：计数-1
# DELETE /counter：重置为0
# 你的答案：




# 题5.3：创建一个简单的 RESTful API
# 管理图书数据（id, title, author）
# 支持增删改查
# 你的答案：




# 题5.4：创建一个简单的聊天机器人
# 规则：
# - 用户说"你好"，回复"你好呀！"
# - 用户说"名字"，回复"我是聊天机器人"
# - 用户说"时间"，回复当前时间
# - 其他情况，回复"我不明白"
# 你的答案：




# ========================================
# 答案区（先自己做再看！）
# ========================================

"""
【第1关答案】

1.1
@app.route('/hi')
def hi():
    return '你好，世界！'

1.2
import datetime

@app.route('/date')
def show_date():
    today = datetime.date.today()
    return str(today)

1.3
import random

@app.route('/random')
def random_number():
    num = random.randint(1, 100)
    return f'随机数是：{num}'

1.4
@app.route('/pages/about')
def about():
    return '<h1>关于我们</h1><p>这是一个学习网站</p>'

1.5
@app.route('/user-info')
def user_info():
    return jsonify({
        'name': '小明',
        'age': 14,
        'city': '北京'
    })

1.6
@app.route('/redirect-test')
def redirect_test():
    return redirect(url_for('hi'))

1.7
@app.route('/styled')
def styled():
    return '''
    <html>
    <head>
        <style>
            h1 { color: blue; }
            p { color: gray; }
        </style>
    </head>
    <body>
        <h1>蓝色标题</h1>
        <p>灰色段落</p>
    </body>
    </html>
    '''

1.8
@app.route('/headers')
def headers():
    user_agent = request.headers.get('User-Agent')
    return f'你的浏览器是：{user_agent}'
"""

"""
【第2关答案】

2.1
@app.route('/square/<int:n>')
def square(n):
    return f'{n} 的平方是 {n * n}'

2.2
@app.route('/greet/<name>/<int:times>')
def greet_times(name, times):
    greeting = (f'{name}你好！' * times)
    return greeting

2.3
@app.route('/calculate/<int:a>/<operation>/<int:b>')
def calculate(a, operation, b):
    if operation == 'add':
        result = a + b
        symbol = '+'
    elif operation == 'sub':
        result = a - b
        symbol = '-'
    elif operation == 'mul':
        result = a * b
        symbol = '×'
    elif operation == 'div':
        result = a / b if b != 0 else '错误'
        symbol = '÷'
    else:
        return '未知操作'

    return f'{a} {symbol} {b} = {result}'

2.4
@app.route('/items')
def items():
    page = request.args.get('page', '1')
    return f'第 {page} 页'

2.5
@app.route('/profile')
def profile():
    name = request.args.get('name', '匿名')
    age = request.args.get('age', '未知')
    city = request.args.get('city', '未知')
    return f'姓名：{name}，年龄：{age}，城市：{city}'

2.6
@app.route('/fibonacci/<int:n>')
def fibonacci(n):
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return f'斐波那契数列前{n}项：{fib[:n]}'
"""

"""
【第3关答案】

3.1 加法计算器
@app.route('/calc', methods=['GET', 'POST'])
def calc():
    if request.method == 'GET':
        return '''
        <form method="POST">
            <input name="a" type="number"> +
            <input name="b" type="number">
            <button>计算</button>
        </form>
        '''
    else:
        a = float(request.form.get('a'))
        b = float(request.form.get('b'))
        return f'{a} + {b} = {a + b}'

3.2 温度转换器
@app.route('/temperature', methods=['GET', 'POST'])
def temperature():
    if request.method == 'GET':
        return '''
        <form method="POST">
            <input name="temp" type="number" step="0.1">
            <select name="type">
                <option value="c2f">摄氏→华氏</option>
                <option value="f2c">华氏→摄氏</option>
            </select>
            <button>转换</button>
        </form>
        '''
    else:
        temp = float(request.form.get('temp'))
        conv_type = request.form.get('type')
        if conv_type == 'c2f':
            result = temp * 9/5 + 32
            return f'{temp}°C = {result:.1f}°F'
        else:
            result = (temp - 32) * 5/9
            return f'{temp}°F = {result:.1f}°C'

3.3 BMI 计算器
@app.route('/bmi', methods=['GET', 'POST'])
def bmi():
    if request.method == 'GET':
        return '''
        <form method="POST">
            身高(cm)：<input name="height" type="number"><br>
            体重(kg)：<input name="weight" type="number"><br>
            <button>计算</button>
        </form>
        '''
    else:
        height = float(request.form.get('height')) / 100
        weight = float(request.form.get('weight'))
        bmi_value = weight / (height ** 2)

        if bmi_value < 18.5:
            status = '偏瘦'
        elif bmi_value < 24:
            status = '正常'
        elif bmi_value < 28:
            status = '偏胖'
        else:
            status = '肥胖'

        return f'BMI: {bmi_value:.1f}，体型：{status}'
"""

"""
【第4关答案】

4.1 学生信息模板
@app.route('/student-card')
def student_card():
    student = {'name': '小明', 'age': 14, 'grade': '七年级', 'score': 95}
    template = '''
    <div style="border: 1px solid #ccc; padding: 20px; width: 300px;">
        <h2>{{ student.name }} 的学生卡</h2>
        <p>年龄：{{ student.age }}</p>
        <p>年级：{{ student.grade }}</p>
        <p>成绩：{{ student.score }}</p>
    </div>
    '''
    return render_template_string(template, student=student)

4.2 九九乘法表
@app.route('/multiplication')
def multiplication():
    template = '''
    <table border="1" cellpadding="5">
    {% for i in range(1, 10) %}
        <tr>
        {% for j in range(1, i + 1) %}
            <td>{{ j }} × {{ i }} = {{ j * i }}</td>
        {% endfor %}
        </tr>
    {% endfor %}
    </table>
    '''
    return render_template_string(template)

4.3 成绩等级
@app.route('/grade/<int:score>')
def grade(score):
    template = '''
    <h1>成绩查询</h1>
    <p>分数：{{ score }}</p>
    <p>等级：
        {% if score >= 90 %}优秀
        {% elif score >= 80 %}良好
        {% elif score >= 60 %}及格
        {% else %}不及格{% endif %}
    </p>
    '''
    return render_template_string(template, score=score)
"""


# ========================================
# 评分标准
# ========================================
"""
【评分标准】

第1关（8题）：每题2分，共16分
第2关（6题）：每题3分，共18分
第3关（5题）：每题4分，共20分
第4关（5题）：每题4分，共20分
第5关（4题）：每题5分，共20分
附加创意分：最高6分

总分100分，评分等级：
90-100分：Web 开发大师！
70-89分：Web 开发高手
50-69分：Web 开发学徒
30-49分：继续加油
0-29分：需要复习教程
"""


# ========================================
# 测试路由
# ========================================

@app.route('/')
def index():
    return '''
    <h1>Web 服务练习题</h1>
    <p>请打开 webserver_exercises.py 文件，按照题目要求编写代码</p>
    <p>完成后取消注释你的代码，运行文件测试</p>
    '''


if __name__ == '__main__':
    print("=" * 50)
    print("Web 服务练习题")
    print("=" * 50)
    print("请打开文件查看题目，编写代码后运行测试")
    print("访问 http://localhost:5001 查看提示")
    app.run(port=5001, debug=True)
