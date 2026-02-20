# MySQL 数据库快速入门教程

适合初中生学习的数据库教程，简单、快速、易懂、边学边练。

## 教程结构

```
database/
├── mysql_quick_start.sql   # 主教程（约1-2小时）
├── mysql_exercises.sql     # 练习题集（29道题，带答案）
├── python_mysql.py         # Python操作MySQL教程
└── README.md               # 本文件
```

## 学习路径

### 第一步：学习 SQL 基础
1. 打开 `mysql_quick_start.sql`
2. 按顺序学习13节课
3. 每节完成后做练习

### 第二步：做练习题
1. 打开 `mysql_exercises.sql`
2. 先自己做，不会再看答案
3. 共4关，29道题

### 第三步：学 Python 操作数据库
1. 安装 pymysql：`pip install pymysql`
2. 打开 `python_mysql.py` 学习
3. 用程序操作数据库

## 环境准备

### 方式一：在线练习（推荐初学者）
- [DB Fiddle](https://www.db-fiddle.com) - 无需安装
- [SQLite Online](https://sqliteonline.com) - 支持 MySQL

### 方式二：本地安装 MySQL
1. 下载 [MySQL Community Server](https://dev.mysql.com/downloads/mysql/)
2. 或安装 [XAMPP](https://www.apachefriends.org/)（包含 MySQL）

### 方式三：Docker
```bash
docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 mysql
```

## 如何运行教程

### MySQL 命令行
```bash
mysql -u root -p < mysql_quick_start.sql
```

### MySQL Workbench
1. 打开 SQL 文件
2. 选中要执行的代码
3. 按 Ctrl+Shift+Enter 执行

### 在线环境
1. 打开 db-fiddle.com
2. 复制粘贴代码
3. 点击 Run

## 学习时间规划

| 内容 | 预计时间 | 说明 |
|-----|---------|------|
| 第1-3节 | 20分钟 | 概念理解和环境准备 |
| 第4-6节 | 25分钟 | 数据增删改查基础 |
| 第7-9节 | 20分钟 | 查询进阶 |
| 第10-12节 | 25分钟 | 聚合和分组 |
| 练习题 | 30分钟 | 巩固所学 |
| Python操作 | 30分钟 | 进阶内容 |

## 教程大纲

### mysql_quick_start.sql（主教程）
1. 什么是数据库？
2. 环境准备
3. 创建数据库和表
4. 插入数据 INSERT
5. 查询数据 SELECT 基础
6. 条件查询 WHERE
7. 排序 ORDER BY 和 限制 LIMIT
8. 更新数据 UPDATE
9. 删除数据 DELETE
10. 聚合函数
11. 分组 GROUP BY
12. 多表查询 JOIN
13. 实用技巧
14. 综合练习

### mysql_exercises.sql（练习题）
- 第1关：基础查询（10题）
- 第2关：聚合与分组（8题）
- 第3关：多表查询（6题）
- 第4关：综合挑战（5题）

### python_mysql.py（Python操作）
1. 连接数据库
2. 查询数据 SELECT
3. 插入数据 INSERT
4. 更新数据 UPDATE
5. 删除数据 DELETE
6. 事务处理
7. 实用函数封装
8. 综合示例

## SQL 学习口诀

```
SELECT 从哪查，WHERE 筛选啥
GROUP BY 分组用，HAVING 组后筛
ORDER BY 排序来，LIMIT 限数量
INSERT 加数据，UPDATE 改数据
DELETE 删数据，切记加 WHERE！
```

## 常见问题

**Q: 忘记 MySQL 密码怎么办？**
A: 可以重置密码，或者重新安装 MySQL

**Q: 中文显示乱码？**
A: 确保数据库和表的字符集是 utf8mb4

**Q: SQL 语句报错？**
A: 检查是否用了中文符号（引号、分号）

## 推荐资源

- [MySQL 官方文档](https://dev.mysql.com/doc/)
- [SQLZoo](https://sqlzoo.net/) - 在线练习
- [LeetCode Database](https://leetcode.com/problemset/database/) - 进阶练习

---

祝你女儿学习愉快！
