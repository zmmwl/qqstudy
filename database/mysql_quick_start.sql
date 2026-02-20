-- ========================================
-- MySQL 数据库快速入门教程 (1-2小时学习计划)
-- ========================================
-- 适合人群：初中生、编程初学者
--
-- 建议学习时间分配：
-- - 第1-3节：20分钟（概念理解和环境准备）
-- - 第4-6节：25分钟（数据增删改查基础）
-- - 第7-9节：20分钟（查询进阶）
-- - 第10-12节：25分钟（聚合和分组）
-- - 综合练习：20分钟

/*
使用方法：
1. 先安装 MySQL（或使用在线环境如 db-fiddle.com）
2. 逐节阅读 SQL 语句
3. 在 MySQL 中执行代码查看结果
4. 完成"练习"部分的题目
5. 阅读注释理解概念

如何运行本教程：
方法一：命令行
  mysql -u root -p < mysql_quick_start.sql

方法二：MySQL Workbench
  打开文件，逐段选中执行（选中后按 Ctrl+Shift+Enter）

方法三：在线环境
  访问 https://www.db-fiddle.com 复制代码执行
*/


-- ========================================
-- 第1节：什么是数据库？(5分钟)
-- ========================================

/*
【用生活中的例子理解数据库】

想象你有一个超级强大的 Excel 表格：
- 数据库(Database) = 整个 Excel 文件
- 表(Table) = Excel 中的一个工作表
- 字段/列(Column) = 表格的列（如：姓名、年龄、班级）
- 行/记录(Row) = 表格的每一行数据

【为什么需要数据库？】
1. 可以存储海量数据（百万、千万条记录）
2. 多人同时访问不会冲突
3. 快速查找数据（毫秒级）
4. 数据安全，有备份和恢复功能

【MySQL 是什么？】
MySQL 是一种关系型数据库管理系统，就像 Word 处理文档一样，
MySQL 专门用来处理数据库。它是免费的，被全世界广泛使用！

【SQL 是什么？】
SQL（Structured Query Language）= 结构化查询语言
就是用来和数据库"对话"的语言。

SQL 四大基本操作（CRUD）：
- CREATE/INSERT → 创建/插入数据
- READ/SELECT  → 读取/查询数据
- UPDATE       → 更新数据
- DELETE       → 删除数据

记住这四个单词：增删改查！
*/


-- ========================================
-- 第2节：环境准备 (10分钟)
-- ========================================

/*
【安装 MySQL】
Windows/Mac: 访问 https://dev.mysql.com/downloads/mysql/
或安装 XAMPP（包含 MySQL）：https://www.apachefriends.org/

【在线练习（无需安装）】
- https://www.db-fiddle.com （推荐）
- https://sqliteonline.com

【连接 MySQL 命令行】
mysql -u root -p
输入密码后进入 MySQL 命令行

【常用命令】
SHOW DATABASES;          -- 显示所有数据库
USE 数据库名;            -- 选择数据库
SHOW TABLES;             -- 显示当前数据库的所有表
DESCRIBE 表名;           -- 查看表结构
*/

-- 查看当前 MySQL 版本（验证连接成功）
SELECT VERSION();

-- 显示所有数据库
SHOW DATABASES;


-- ========================================
-- 第3节：创建数据库和表 (10分钟)
-- ========================================

-- 创建一个"学校"数据库（如果已存在则先删除）
DROP DATABASE IF EXISTS school;  -- 删除旧数据库（谨慎使用！）
CREATE DATABASE school DEFAULT CHARACTER SET utf8mb4;  -- 创建新数据库

-- 使用这个数据库
USE school;

-- 创建"学生"表
/*
表结构设计：
+------------+-------------+------+-----+---------+----------------+
| 字段名      | 类型        | 允许空|默认值|自增     | 说明           |
+------------+-------------+------+-----+---------+----------------+
| id         | INT         | 否   |     | 是      | 学生编号(主键)  |
| name       | VARCHAR(50) | 否   |     |         | 学生姓名       |
| gender     | CHAR(1)     | 是   | 'M' |         | 性别 M/F       |
| age        | INT         | 是   |     |         | 年龄           |
| class_name | VARCHAR(20) | 是   |     |         | 班级           |
| score      | DECIMAL(5,2)| 是   |     |         | 入学成绩       |
| created_at | DATETIME    | 是   |当前时间|       | 创建时间       |
+------------+-------------+------+-----+---------+----------------+
*/

CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT COMMENT '学生编号',
    name VARCHAR(50) NOT NULL COMMENT '学生姓名',
    gender CHAR(1) DEFAULT 'M' COMMENT '性别：M男/F女',
    age INT COMMENT '年龄',
    class_name VARCHAR(20) COMMENT '班级',
    score DECIMAL(5,2) COMMENT '入学成绩（最多5位，小数2位）',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间'
) COMMENT '学生信息表';

-- 查看表结构
DESCRIBE students;

-- 创建"课程"表
CREATE TABLE courses (
    id INT PRIMARY KEY AUTO_INCREMENT COMMENT '课程编号',
    name VARCHAR(50) NOT NULL COMMENT '课程名称',
    teacher VARCHAR(50) COMMENT '授课老师',
    credit INT DEFAULT 1 COMMENT '学分'
) COMMENT '课程信息表';

-- 创建"成绩"表（学生和课程的关联表）
CREATE TABLE scores (
    id INT PRIMARY KEY AUTO_INCREMENT COMMENT '成绩编号',
    student_id INT COMMENT '学生编号',
    course_id INT COMMENT '课程编号',
    score DECIMAL(5,2) COMMENT '成绩',
    exam_date DATE COMMENT '考试日期',
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
    -- 外键（FOREIGN KEY）作用：
    -- 1. 确保数据正确：student_id 必须是 students 表中存在的 id
    -- 2. 级联操作：删除学生时，该学生的成绩也会自动删除
    -- 就像：成绩表里的学生编号必须对应一个真实存在的学生
) COMMENT '学生成绩表';

-- 查看所有表
SHOW TABLES;

/*
【数据类型速查】
INT          - 整数（如：年龄、数量）
DECIMAL(m,n) - 小数（m总位数，n小数位）
VARCHAR(n)   - 可变长字符串（最多n个字符）
CHAR(n)      - 固定长字符串
DATE         - 日期（YYYY-MM-DD）
DATETIME     - 日期时间（YYYY-MM-DD HH:MM:SS）
TEXT         - 长文本

【约束速查】
PRIMARY KEY     - 主键（唯一标识每一行，就像身份证号）
AUTO_INCREMENT  - 自动递增（新数据自动+1，不用手动填）
NOT NULL        - 不允许为空（必填项）
DEFAULT         - 默认值（不填时自动使用这个值）
FOREIGN KEY     - 外键（关联其他表，保证数据一致性）
*/

-- 练习3：创建一个"图书"表，包含：编号、书名、作者、价格、出版日期
-- _______________________________________



-- ========================================
-- 第4节：插入数据 INSERT (5分钟)
-- ========================================

-- 插入单条数据（指定字段）
INSERT INTO students (name, gender, age, class_name, score)
VALUES ('小明', 'M', 14, '七年级1班', 95.5);

-- 插入单条数据（所有字段，按顺序）
INSERT INTO students
VALUES (NULL, '小红', 'F', 13, '七年级1班', 98.0, NULL);
-- NULL 表示让数据库自动填充（如自增ID、默认时间）

-- 批量插入（推荐！效率更高）
INSERT INTO students (name, gender, age, class_name, score) VALUES
('小刚', 'M', 14, '七年级2班', 88.5),
('小芳', 'F', 13, '七年级1班', 92.0),
('小强', 'M', 15, '七年级2班', 75.5),
('小丽', 'F', 14, '七年级3班', 89.0),
('小伟', 'M', 14, '七年级1班', 82.5),
('小雯', 'F', 13, '七年级3班', 94.5),
('小军', 'M', 15, '七年级2班', 78.0),
('小燕', 'F', 14, '七年级3班', 91.5);

-- 插入课程数据
INSERT INTO courses (name, teacher, credit) VALUES
('语文', '王老师', 4),
('数学', '李老师', 4),
('英语', '张老师', 3),
('物理', '陈老师', 3),
('化学', '刘老师', 2);

-- 插入成绩数据
INSERT INTO scores (student_id, course_id, score, exam_date) VALUES
(1, 1, 88.5, '2024-03-15'),  -- 小明的语文成绩
(1, 2, 95.0, '2024-03-16'),  -- 小明的数学成绩
(2, 1, 92.0, '2024-03-15'),  -- 小红的语文成绩
(2, 2, 98.5, '2024-03-16'),  -- 小红的数学成绩
(3, 1, 75.5, '2024-03-15'),
(3, 2, 82.0, '2024-03-16'),
(4, 1, 90.0, '2024-03-15'),
(4, 3, 95.5, '2024-03-17');  -- 小芳的英语成绩

-- 查看插入的数据
SELECT * FROM students;
SELECT * FROM courses;
SELECT * FROM scores;

-- 练习4：再添加2名学生和他们的成绩
-- _______________________________________



-- ========================================
-- 第5节：查询数据 SELECT 基础 (8分钟)
-- ========================================

-- 查询所有列（* 表示所有）
SELECT * FROM students;

-- 查询指定列
SELECT name, age, class_name FROM students;

-- 给列起别名（AS 可以省略）
SELECT
    name AS 姓名,
    age AS 年龄,
    class_name AS 班级
FROM students;

-- 去除重复值
SELECT DISTINCT class_name FROM students;  -- 查看有哪些班级
SELECT DISTINCT gender FROM students;      -- 查看性别有哪些

-- 计算字段
SELECT
    name,
    score,
    score + 5 AS 加分后成绩,
    score * 1.1 AS 提高10后的成绩
FROM students;

-- 字符串拼接
SELECT
    CONCAT(name, '同学') AS 姓名,
    CONCAT(class_name, '-', name) AS 班级姓名
FROM students;

-- 练习5：查询所有学生的姓名和入学成绩，并计算成绩的等级线（60分及格）
-- 提示：score - 60 可以看出超过及格线多少分
-- _______________________________________



-- ========================================
-- 第6节：条件查询 WHERE (10分钟)
-- ========================================

-- 基本条件
SELECT * FROM students WHERE age = 14;        -- 年龄等于14
SELECT * FROM students WHERE age > 14;        -- 年龄大于14
SELECT * FROM students WHERE age >= 14;       -- 年龄大于等于14
SELECT * FROM students WHERE age < 14;        -- 年龄小于14
SELECT * FROM students WHERE age != 14;       -- 年龄不等于14

-- 字符串条件
SELECT * FROM students WHERE name = '小明';   -- 等于
SELECT * FROM students WHERE name != '小明';  -- 不等于

-- 模糊查询（LIKE）
SELECT * FROM students WHERE name LIKE '小%';  -- 以"小"开头
SELECT * FROM students WHERE name LIKE '%明';  -- 以"明"结尾
SELECT * FROM students WHERE name LIKE '%红%'; -- 包含"红"

-- % 表示任意多个字符，_ 表示单个字符
SELECT * FROM students WHERE class_name LIKE '七年级_班';  -- 七年级X班

-- 范围查询
SELECT * FROM students WHERE score BETWEEN 80 AND 90;  -- 成绩80-90之间
SELECT * FROM students WHERE age IN (13, 15);          -- 年龄是13或15

-- 逻辑运算符
SELECT * FROM students WHERE gender = 'F' AND score > 90;  -- 女生且成绩>90
SELECT * FROM students WHERE gender = 'M' OR age > 14;     -- 男生或年龄>14

-- NOT 取反
SELECT * FROM students WHERE NOT gender = 'M';  -- 不是男生
SELECT * FROM students WHERE class_name NOT IN ('七年级1班', '七年级2班');

-- 处理 NULL 值
SELECT * FROM students WHERE score IS NULL;     -- 成绩为空
SELECT * FROM students WHERE score IS NOT NULL; -- 成绩不为空

-- 练习6：
-- 6.1 查询所有女生的信息
-- 6.2 查询七年级1班成绩大于85分的学生
-- 6.3 查询年龄是13岁或14岁的学生
-- _______________________________________



-- ========================================
-- 第7节：排序 ORDER BY 和 限制 LIMIT (5分钟)
-- ========================================

-- 按成绩升序排列（ASC 可省略）
SELECT name, score FROM students ORDER BY score ASC;
SELECT name, score FROM students ORDER BY score;  -- 默认升序

-- 按成绩降序排列（DESC 不能省略）
SELECT name, score FROM students ORDER BY score DESC;

-- 多字段排序（先按班级，再按成绩）
SELECT name, class_name, score
FROM students
ORDER BY class_name, score DESC;

-- 限制返回数量
SELECT * FROM students LIMIT 3;           -- 只返回前3条
SELECT * FROM students LIMIT 3, 3;        -- 跳过前3条，返回后3条（分页用）
SELECT * FROM students LIMIT 3 OFFSET 3;  -- 同上，写法更清晰

-- 实际应用：成绩排行榜
SELECT name, class_name, score
FROM students
ORDER BY score DESC
LIMIT 5;  -- 前5名

-- 练习7：
-- 7.1 查询年龄最大的3名学生
-- 7.2 查询每个班级成绩最低的学生（按班级升序，成绩升序）
-- _______________________________________



-- ========================================
-- 第8节：更新数据 UPDATE (5分钟)
-- ========================================

-- 【重要】UPDATE 一定要加 WHERE，否则会更新所有行！

-- 更新单个字段
UPDATE students SET age = 15 WHERE name = '小明';

-- 更新多个字段
UPDATE students
SET age = 14, score = 96.0
WHERE name = '小明';

-- 条件更新
UPDATE students
SET score = score + 2
WHERE class_name = '七年级1班';  -- 给1班所有学生加2分

-- 查看更新结果
SELECT * FROM students WHERE name = '小明';
SELECT * FROM students WHERE class_name = '七年级1班';

-- 练习8：
-- 8.1 把"小刚"转到"七年级3班"
-- 8.2 给所有不及格（<60分）的学生加10分
-- _______________________________________



-- ========================================
-- 第9节：删除数据 DELETE (5分钟)
-- ========================================

-- 【警告】DELETE 一定要加 WHERE，否则会删除所有数据！

-- 先插入一条测试数据
INSERT INTO students (name, gender, age, class_name, score)
VALUES ('测试学生', 'M', 99, '测试班', 0);

-- 删除指定数据
DELETE FROM students WHERE name = '测试学生';

-- 条件删除
DELETE FROM students WHERE score < 60;  -- 删除不及格的学生

-- 删除所有数据（保留表结构）- 危险操作！
-- TRUNCATE TABLE students;  -- 慎用！不可恢复！

-- 练习9：
-- 先插入一条临时数据，然后删除它
-- _______________________________________



-- ========================================
-- 第10节：聚合函数 (8分钟)
-- ========================================

-- 统计数量
SELECT COUNT(*) AS 学生总数 FROM students;
SELECT COUNT(DISTINCT class_name) AS 班级数量 FROM students;

-- 求和
SELECT SUM(score) AS 成绩总和 FROM students;

-- 平均值
SELECT AVG(score) AS 平均成绩 FROM students;

-- 最大值和最小值
SELECT
    MAX(score) AS 最高分,
    MIN(score) AS 最低分,
    MAX(score) - MIN(score) AS 分数差距
FROM students;

-- 综合统计
SELECT
    COUNT(*) AS 人数,
    SUM(score) AS 总分,
    AVG(score) AS 平均分,
    MAX(score) AS 最高分,
    MIN(score) AS 最低分
FROM students
WHERE gender = 'F';  -- 统计女生

-- 练习10：
-- 10.1 统计七年级1班的学生人数
-- 10.2 计算所有14岁学生的平均成绩
-- _______________________________________



-- ========================================
-- 第11节：分组 GROUP BY (10分钟)
-- ========================================

-- 按性别分组统计
SELECT
    gender AS 性别,
    COUNT(*) AS 人数,
    AVG(score) AS 平均成绩
FROM students
GROUP BY gender;

-- 按班级分组统计
SELECT
    class_name AS 班级,
    COUNT(*) AS 学生人数,
    ROUND(AVG(score), 2) AS 平均成绩,  -- ROUND 保留2位小数
    MAX(score) AS 最高分,
    MIN(score) AS 最低分
FROM students
GROUP BY class_name
ORDER BY 平均成绩 DESC;

-- HAVING：分组后的筛选（类似WHERE，但用于分组后）
SELECT
    class_name AS 班级,
    COUNT(*) AS 人数,
    AVG(score) AS 平均分
FROM students
GROUP BY class_name
HAVING AVG(score) > 85  -- 筛选平均分>85的班级
ORDER BY 平均分 DESC;

-- WHERE vs HAVING 的区别：
-- WHERE：分组前筛选（筛选行）
-- HAVING：分组后筛选（筛选组）

-- 示例：查询班级人数超过2人的班级
SELECT
    class_name,
    COUNT(*) AS 人数
FROM students
GROUP BY class_name
HAVING COUNT(*) >= 2;

-- 练习11：
-- 11.1 统计每个班级的男生和女生人数
-- 11.2 查询平均成绩大于90分的班级
-- _______________________________________



-- ========================================
-- 第12节：多表查询 JOIN (10分钟)
-- ========================================

-- 笛卡尔积（不推荐，会产生大量重复数据）
-- SELECT * FROM students, courses;

-- 内连接（INNER JOIN）：只返回两表都有匹配的记录
-- 用生活例子理解：就像"配对游戏"，只有两边都存在才显示
SELECT
    students.name AS 学生姓名,
    courses.name AS 课程名称,
    scores.score AS 成绩
FROM scores
INNER JOIN students ON scores.student_id = students.id  -- 成绩表和学生表连接
INNER JOIN courses ON scores.course_id = courses.id;    -- 再和课程表连接
-- 结果：只显示有成绩的学生和课程

-- 使用表别名简化
SELECT
    s.name AS 学生,
    c.name AS 课程,
    sc.score AS 成绩
FROM scores sc
JOIN students s ON sc.student_id = s.id
JOIN courses c ON sc.course_id = c.id;

-- 左连接（LEFT JOIN）：返回左表所有记录，右表没有则为NULL
-- 用生活例子理解：以左边的学生表为主，即使学生没有成绩也要显示
-- 就像点名：每个学生都要喊到，没交卷的显示"未考试"
SELECT
    s.name AS 学生,
    c.name AS 课程,
    sc.score AS 成绩
FROM students s
LEFT JOIN scores sc ON s.id = sc.student_id  -- 以学生表为主
LEFT JOIN courses c ON sc.course_id = c.id;
-- 结果：所有学生都会显示，没成绩的学生课程和成绩显示NULL

-- 查询每个学生的平均成绩
SELECT
    s.name AS 学生姓名,
    ROUND(AVG(sc.score), 2) AS 平均成绩,
    COUNT(sc.id) AS 考试科目数
FROM students s
LEFT JOIN scores sc ON s.id = sc.student_id
GROUP BY s.id, s.name
ORDER BY 平均成绩 DESC;

-- 练习12：
-- 12.1 查询"数学"课程的所有成绩
-- 12.2 查询每个学生的考试总成绩和平均成绩
-- _______________________________________



-- ========================================
-- 第13节：实用技巧 (5分钟)
-- ========================================

-- CASE WHEN 条件表达式（相当于 if-else）
SELECT
    name,
    score,
    CASE
        WHEN score >= 90 THEN '优秀'
        WHEN score >= 80 THEN '良好'
        WHEN score >= 60 THEN '及格'
        ELSE '不及格'
    END AS 等级
FROM students;

-- IF 函数（简化版的 CASE）
SELECT
    name,
    score,
    IF(score >= 60, '及格', '不及格') AS 是否及格
FROM students;

-- 时间函数
SELECT NOW();                          -- 当前时间
SELECT CURDATE();                      -- 当前日期
SELECT YEAR(NOW());                    -- 当前年份
SELECT DATE_FORMAT(NOW(), '%Y年%m月%d日');  -- 格式化日期

-- 字符串函数
SELECT UPPER('hello');                 -- 转大写
SELECT LOWER('HELLO');                 -- 转小写
SELECT LENGTH('你好世界');              -- 字符串长度
SELECT SUBSTRING('Hello World', 1, 5); -- 截取字符串

-- 数学函数
SELECT ABS(-10);        -- 绝对值
SELECT ROUND(3.14159, 2); -- 四舍五入
SELECT CEIL(3.1);       -- 向上取整
SELECT FLOOR(3.9);      -- 向下取整
SELECT RAND();          -- 随机数 0-1

-- COALESCE：返回第一个非NULL值
SELECT COALESCE(NULL, NULL, '默认值', '其他');



-- ========================================
-- 综合练习：学生成绩管理系统
-- ========================================

/*
【项目需求】
你已经建立了一个学校数据库，现在来完成以下任务：

1. 查询"七年级1班"所有学生的信息
2. 查询成绩排名前5的学生
3. 统计每个班级的平均成绩，按平均成绩降序排列
4. 查询所有女生的数学成绩
5. 给每个学生添加一个"等级"字段（优秀/良好/及格/不及格）
6. 查询每个学生参加了几门考试，以及平均成绩
*/

-- 练习1：查询"七年级1班"所有学生的信息
SELECT * FROM students WHERE class_name = '七年级1班';

-- 练习2：查询成绩排名前5的学生
SELECT name, class_name, score
FROM students
ORDER BY score DESC
LIMIT 5;

-- 练习3：统计每个班级的平均成绩
SELECT
    class_name AS 班级,
    COUNT(*) AS 人数,
    ROUND(AVG(score), 2) AS 平均成绩
FROM students
GROUP BY class_name
ORDER BY 平均成绩 DESC;

-- 练习4：查询所有女生的数学成绩
SELECT
    s.name AS 学生姓名,
    c.name AS 课程,
    sc.score AS 成绩
FROM students s
JOIN scores sc ON s.id = sc.student_id
JOIN courses c ON sc.course_id = c.id
WHERE s.gender = 'F' AND c.name = '数学';

-- 练习5：添加等级字段
SELECT
    name AS 姓名,
    score AS 成绩,
    CASE
        WHEN score >= 90 THEN '优秀'
        WHEN score >= 80 THEN '良好'
        WHEN score >= 60 THEN '及格'
        ELSE '不及格'
    END AS 等级
FROM students
ORDER BY score DESC;

-- 练习6：每个学生的考试情况
SELECT
    s.name AS 学生姓名,
    s.class_name AS 班级,
    COUNT(sc.id) AS 考试科目数,
    ROUND(AVG(sc.score), 2) AS 平均成绩,
    MAX(sc.score) AS 最高分,
    MIN(sc.score) AS 最低分
FROM students s
LEFT JOIN scores sc ON s.id = sc.student_id
GROUP BY s.id, s.name, s.class_name
ORDER BY 平均成绩 DESC;



-- ========================================
-- 学习建议
-- ========================================
/*
【SQL 学习口诀】
SELECT 从哪查，WHERE 筛选啥
GROUP BY 分组用，HAVING 组后筛
ORDER BY 排序来，LIMIT 限数量
INSERT 加数据，UPDATE 改数据
DELETE 删数据，切记加 WHERE！

【常见错误】
1. UPDATE/DELETE 忘记加 WHERE → 全表被修改/删除！
2. 字符串忘记加引号 → name = 小明 ❌  name = '小明' ✓
3. 中文符号问题 → 用英文引号和分号
4. 关键字拼写错误 → SELCET ❌  SELECT ✓

【练习建议】
1. 每学完一节，自己写一遍 SQL
2. 尝试修改条件，观察结果变化
3. 设计自己的数据（如：图书、商品、电影）
4. 多用 SELECT 练习，少做 DELETE！

【进阶学习方向】
1. 索引（Index）- 提高查询速度
2. 事务（Transaction）- 保证数据安全
3. 视图（View）- 虚拟表
4. 存储过程（Stored Procedure）
5. Python + MySQL（pymysql 库）

【推荐资源】
- MySQL 官方文档：https://dev.mysql.com/doc/
- 在线练习：SQLZoo、LeetCode Database
- 视频教程：B站搜索"MySQL教程"

【下一步建议】
1. 完成 50 道 SQL 练习题
2. 设计一个完整的项目数据库
3. 学习 Python 操作 MySQL
4. 了解数据库设计原则（范式）
*/


-- ========================================
-- 附录：常用 SQL 速查表
-- ========================================

/*
【创建】
CREATE DATABASE 数据库名;
CREATE TABLE 表名 (字段名 类型 约束, ...);

【插入】
INSERT INTO 表名 (字段1, 字段2) VALUES (值1, 值2);
INSERT INTO 表名 VALUES (值1, 值2, ...);

【查询】
SELECT * FROM 表名;
SELECT 字段1, 字段2 FROM 表名;
SELECT * FROM 表名 WHERE 条件;
SELECT * FROM 表名 ORDER BY 字段 DESC LIMIT 10;

【更新】
UPDATE 表名 SET 字段=新值 WHERE 条件;

【删除】
DELETE FROM 表名 WHERE 条件;
TRUNCATE TABLE 表名;  -- 清空表

【聚合】
COUNT(), SUM(), AVG(), MAX(), MIN()
GROUP BY 字段
HAVING 条件

【连接】
JOIN / INNER JOIN  -- 内连接
LEFT JOIN          -- 左连接
RIGHT JOIN         -- 右连接
*/

-- 教程结束
SELECT '🎉 恭喜完成 MySQL 快速入门教程！' AS 消息;
SELECT '记住：多练习是掌握 SQL 的最好方法！' AS 建议;
