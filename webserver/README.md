# Web 服务快速入门教程

适合初中生学习的 Web 开发教程，简单、快速、易懂、边学边练。

## 教程结构

```
webserver/
├── webserver_quick_start.py   # 主教程（约2-3小时）
├── webserver_exercises.py     # 练习题集（28道题，带答案）
├── templates/
│   └── index.html             # HTML 模板示例
├── static/
│   ├── style.css              # CSS 样式示例
│   └── script.js              # JavaScript 示例
└── README.md                  # 本文件
```

## 学习路径

### 第一步：理解 Web 基础
1. 阅读 `webserver_quick_start.py` 第1-2节
2. 理解 BS 架构和 HTTP 协议

### 第二步：动手实践
1. 安装 Flask：`pip install flask`
2. 运行主教程：`python webserver_quick_start.py`
3. 打开浏览器访问：http://localhost:5000
4. 逐节学习，完成练习

### 第三步：前端基础
1. 学习 `templates/index.html`
2. 学习 `static/style.css`
3. 学习 `static/script.js`

### 第四步：完成练习
1. 打开 `webserver_exercises.py`
2. 先自己做，不会再看答案
3. 共5关，28道题

## 环境准备

### 安装 Flask
```bash
pip install flask
```

### 运行教程
```bash
python webserver_quick_start.py
```

### 访问网站
打开浏览器访问：http://localhost:5000

## 学习时间规划

| 内容 | 预计时间 | 说明 |
|-----|---------|------|
| 第1-2节 | 15分钟 | 概念理解 |
| 第3-4节 | 25分钟 | 基础服务器 |
| 第5-6节 | 30分钟 | 路由和参数 |
| 第7-8节 | 30分钟 | 模板和表单 |
| 第9-10节 | 30分钟 | 数据库和 API |
| 练习题 | 40分钟 | 巩固所学 |
| 前端基础 | 30分钟 | HTML/CSS/JS |

## 教程大纲

### webserver_quick_start.py（主教程）
1. 什么是 Web 服务？（BS 架构概念）
2. HTTP 协议基础
3. 最简单的 Web 服务器
4. 用 Flask 创建 Web 应用
5. URL 参数
6. HTTP 方法（GET 和 POST）
7. 模板（Jinja2）
8. 表单和文件上传
9. 连接数据库
10. API 接口

### webserver_exercises.py（练习题）
- 第1关：基础路由（8题）
- 第2关：URL 参数（6题）
- 第3关：表单处理（5题）
- 第4关：模板使用（5题）
- 第5关：综合挑战（4题）

### 前端文件
- `index.html`：HTML 基础示例
- `style.css`：CSS 样式示例
- `script.js`：JavaScript 交互示例

## 核心概念速查

### BS 架构
```
浏览器（客户端） ←→ HTTP 协议 ←→ 服务器（后端）
     ↓                                  ↓
   显示网页                          处理请求
```

### HTTP 方法
- **GET**：获取数据（打开网页、搜索）
- **POST**：提交数据（登录、注册）

### HTTP 状态码
- **200**：成功
- **301/302**：重定向
- **404**：找不到
- **500**：服务器错误

### Flask 路由
```python
@app.route('/hello')
def hello():
    return 'Hello, World!'
```

### URL 参数
```python
# 路径参数
@app.route('/user/<name>')
def user(name):
    return f'你好，{name}'

# 查询参数
@app.route('/search')
def search():
    keyword = request.args.get('q')
    return f'搜索：{keyword}'
```

### 模板语法
```html
<!-- 显示变量 -->
<p>{{ name }}</p>

<!-- 条件判断 -->
{% if score >= 90 %}
    <p>优秀</p>
{% endif %}

<!-- 循环 -->
{% for item in items %}
    <p>{{ item }}</p>
{% endfor %}
```

## 学习口诀

```
路由决定去哪里，请求带来用户意
模板渲染成网页，响应返回给浏览器
GET获取POST提交，状态码告诉你结果
```

## 常见问题

**Q: 为什么访问网页显示"无法访问此网站"？**
A: 检查 Python 程序是否在运行，端口是否正确

**Q: 修改代码后网页没有变化？**
A: 开启 debug 模式（`app.run(debug=True)`）会自动重启

**Q: 如何让其他电脑访问我的网站？**
A: 使用 `app.run(host='0.0.0.0')`，但注意安全风险

**Q: 中文显示乱码怎么办？**
A: 确保文件编码是 UTF-8，HTML 中添加 `<meta charset="UTF-8">`

## 推荐资源

- [Flask 官方文档](https://flask.palletsprojects.com/)
- [MDN Web 教程](https://developer.mozilla.org/zh-CN/)
- [菜鸟教程](https://www.runoob.com/)

## 下一步建议

1. 完成本教程的所有练习
2. 学习 HTML/CSS/JavaScript 基础
3. 做一个小项目（待办事项、博客）
4. 学习数据库集成（MySQL）
5. 尝试部署到云服务器

---

祝你女儿学习愉快！
