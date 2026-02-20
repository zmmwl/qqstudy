/*
 * ========================================
 * JavaScript 示例文件
 * ========================================
 *
 * JavaScript 让网页"动起来"，实现交互功能
 *
 * 使用方法：
 * 在 HTML 中引入：
 * <script src="script.js"></script>
 */

// ========== 1. 基础语法 ==========

// 变量声明
let name = '小明';        // 可变变量
const age = 14;           // 常量（不可改变）

// 数据类型
let score = 95.5;         // 数字
let isStudent = true;     // 布尔值
let hobbies = ['阅读', '游戏', '音乐'];  // 数组
let person = {            // 对象
    name: '小红',
    age: 13,
    city: '北京'
};

// 函数定义
function greet(name) {
    return `你好，${name}！`;
}

// 箭头函数（ES6）
const add = (a, b) => a + b;

// 条件判断
function getGrade(score) {
    if (score >= 90) return '优秀';
    if (score >= 80) return '良好';
    if (score >= 60) return '及格';
    return '不及格';
}

// 循环
function showHobbies() {
    hobbies.forEach((hobby, index) => {
        console.log(`${index + 1}. ${hobby}`);
    });
}


// ========== 2. DOM 操作 ==========

// DOM = Document Object Model（文档对象模型）
// JavaScript 通过 DOM 操作 HTML 元素

// 获取元素
function getElementExamples() {
    // 通过 ID 获取
    const header = document.getElementById('header');

    // 通过类名获取
    const cards = document.getElementsByClassName('card');

    // 通过标签名获取
    const paragraphs = document.getElementsByTagName('p');

    // 通过选择器获取（推荐）
    const firstCard = document.querySelector('.card');
    const allCards = document.querySelectorAll('.card');
}

// 修改元素内容
function changeContent() {
    const title = document.getElementById('title');
    if (title) {
        title.textContent = '新标题';           // 纯文本
        title.innerHTML = '<em>新标题</em>';    // HTML 内容
    }
}

// 修改元素样式
function changeStyle() {
    const box = document.getElementById('box');
    if (box) {
        box.style.backgroundColor = '#667eea';
        box.style.color = 'white';
        box.style.padding = '20px';
        box.style.borderRadius = '10px';
    }
}

// 添加/删除类
function toggleClass() {
    const element = document.getElementById('myElement');
    if (element) {
        element.classList.add('active');      // 添加类
        element.classList.remove('hidden');   // 删除类
        element.classList.toggle('highlight'); // 切换类
    }
}

// 创建新元素
function createElement() {
    const newDiv = document.createElement('div');
    newDiv.className = 'card';
    newDiv.textContent = '这是一个新创建的元素';

    const container = document.getElementById('container');
    if (container) {
        container.appendChild(newDiv);
    }
}


// ========== 3. 事件处理 ==========

// 事件 = 用户的操作（点击、输入、鼠标移动等）

// 页面加载完成后执行
document.addEventListener('DOMContentLoaded', function() {
    console.log('页面加载完成！');
    initEventListeners();
});

// 初始化事件监听器
function initEventListeners() {
    // 点击事件
    const clickBtn = document.getElementById('clickBtn');
    if (clickBtn) {
        clickBtn.addEventListener('click', function() {
            alert('按钮被点击了！');
        });
    }

    // 输入事件
    const nameInput = document.getElementById('nameInput');
    if (nameInput) {
        nameInput.addEventListener('input', function(e) {
            console.log('输入内容：', e.target.value);
        });
    }

    // 表单提交事件
    const myForm = document.getElementById('myForm');
    if (myForm) {
        myForm.addEventListener('submit', function(e) {
            e.preventDefault();  // 阻止默认提交行为
            console.log('表单提交了！');
        });
    }

    // 键盘事件
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Enter') {
            console.log('按下了回车键');
        }
    });
}


// ========== 4. 实用函数 ==========

// 显示当前时间
function showCurrentTime() {
    const now = new Date();
    const timeStr = now.toLocaleString('zh-CN');
    const timeElement = document.getElementById('currentTime');
    if (timeElement) {
        timeElement.textContent = timeStr;
    }
}

// 每秒更新时间
function startTimeClock() {
    showCurrentTime();
    setInterval(showCurrentTime, 1000);
}

// 计算器
function calculate() {
    const num1 = parseFloat(document.getElementById('num1').value) || 0;
    const num2 = parseFloat(document.getElementById('num2').value) || 0;
    const operation = document.getElementById('operation').value;

    let result;
    switch (operation) {
        case 'add':
            result = num1 + num2;
            break;
        case 'sub':
            result = num1 - num2;
            break;
        case 'mul':
            result = num1 * num2;
            break;
        case 'div':
            result = num2 !== 0 ? num1 / num2 : '不能除以0';
            break;
        default:
            result = '未知操作';
    }

    document.getElementById('calcResult').textContent = `结果：${result}`;
}

// BMI 计算
function calculateBMI() {
    const height = parseFloat(document.getElementById('height').value) / 100;
    const weight = parseFloat(document.getElementById('weight').value);

    if (height > 0 && weight > 0) {
        const bmi = weight / (height * height);
        let status;

        if (bmi < 18.5) status = '偏瘦';
        else if (bmi < 24) status = '正常';
        else if (bmi < 28) status = '偏胖';
        else status = '肥胖';

        document.getElementById('bmiResult').innerHTML =
            `BMI: ${bmi.toFixed(1)}，体型：<strong>${status}</strong>`;
    }
}

// 表单验证
function validateForm() {
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value;

    let errors = [];

    if (name.length < 2) {
        errors.push('姓名至少2个字符');
    }

    if (!email.includes('@')) {
        errors.push('邮箱格式不正确');
    }

    if (password.length < 6) {
        errors.push('密码至少6个字符');
    }

    if (errors.length > 0) {
        alert('错误：\n' + errors.join('\n'));
        return false;
    }

    return true;
}


// ========== 5. AJAX 请求 ==========

// AJAX = 异步 JavaScript 和 XML
// 用于在不刷新页面的情况下与服务器通信

// 使用 fetch API（现代方式）
async function fetchData(url) {
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('请求失败：', error);
        return null;
    }
}

// GET 请求示例
async function getStudents() {
    const data = await fetchData('/api/students');
    if (data) {
        console.log('学生列表：', data);
        // 在页面上显示数据...
    }
}

// POST 请求示例
async function createStudent(studentData) {
    try {
        const response = await fetch('/api/students', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(studentData)
        });
        const data = await response.json();
        console.log('创建成功：', data);
        return data;
    } catch (error) {
        console.error('创建失败：', error);
    }
}

// DELETE 请求示例
async function deleteStudent(id) {
    try {
        const response = await fetch(`/api/students/${id}`, {
            method: 'DELETE'
        });
        const data = await response.json();
        console.log('删除成功：', data);
        return data;
    } catch (error) {
        console.error('删除失败：', error);
    }
}


// ========== 6. 本地存储 ==========

// localStorage - 持久化存储（关闭浏览器也不会丢失）

// 保存数据
function saveToLocal(key, value) {
    localStorage.setItem(key, JSON.stringify(value));
}

// 读取数据
function getFromLocal(key) {
    const value = localStorage.getItem(key);
    return value ? JSON.parse(value) : null;
}

// 删除数据
function removeFromLocal(key) {
    localStorage.removeItem(key);
}

// 示例：保存用户设置
function saveUserSettings() {
    const settings = {
        theme: 'dark',
        language: 'zh-CN',
        notifications: true
    };
    saveToLocal('userSettings', settings);
}

// 示例：读取用户设置
function loadUserSettings() {
    const settings = getFromLocal('userSettings');
    if (settings) {
        console.log('用户设置：', settings);
    }
}


// ========== 7. 实用工具函数 ==========

// 防抖函数（延迟执行，避免频繁触发）
function debounce(func, delay) {
    let timer = null;
    return function(...args) {
        clearTimeout(timer);
        timer = setTimeout(() => func.apply(this, args), delay);
    };
}

// 节流函数（限制执行频率）
function throttle(func, limit) {
    let inThrottle = false;
    return function(...args) {
        if (!inThrottle) {
            func.apply(this, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

// 格式化日期
function formatDate(date) {
    const d = new Date(date);
    const year = d.getFullYear();
    const month = String(d.getMonth() + 1).padStart(2, '0');
    const day = String(d.getDate()).padStart(2, '0');
    return `${year}-${month}-${day}`;
}

// 生成随机颜色
function randomColor() {
    return '#' + Math.floor(Math.random() * 16777215).toString(16).padStart(6, '0');
}

// 复制文本到剪贴板
async function copyToClipboard(text) {
    try {
        await navigator.clipboard.writeText(text);
        console.log('复制成功！');
    } catch (error) {
        console.error('复制失败：', error);
    }
}


// ========== 学习建议 ==========
/*
【JavaScript 学习路径】

1. 基础语法
   - 变量和数据类型
   - 运算符
   - 条件语句（if/else）
   - 循环（for/while）
   - 函数

2. DOM 操作
   - 获取元素
   - 修改内容
   - 修改样式
   - 创建/删除元素

3. 事件处理
   - 点击事件
   - 表单事件
   - 键盘事件
   - 事件委托

4. 异步编程
   - setTimeout/setInterval
   - Promise
   - async/await
   - fetch API

【常用技巧】

1. 调试：console.log() 是你最好的朋友
2. 查文档：MDN Web Docs (developer.mozilla.org)
3. 多练习：尝试写小项目

【推荐资源】

- MDN JavaScript 教程：https://developer.mozilla.org/zh-CN/docs/Web/JavaScript
- JavaScript.info：https://javascript.info/
- 菜鸟教程：https://www.runoob.com/js/
*/
