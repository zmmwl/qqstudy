-- ========================================
-- MySQL 练习题集
-- ========================================
-- 完成这些练习来巩固你的 SQL 技能！
-- 建议先自己思考，实在不会再看答案

-- 使用学校数据库
USE school;

-- ========================================
-- 第1关：基础查询（共10题）
-- ========================================

-- 题1.1：查询所有学生的姓名和班级
-- 你的答案：
-- SELECT __________ FROM students;




-- 题1.2：查询所有女生的信息
-- 你的答案：




-- 题1.3：查询年龄大于14岁的学生
-- 你的答案：




-- 题1.4：查询成绩在80到90之间的学生
-- 你的答案：




-- 题1.5：查询姓"小"的所有学生（使用 LIKE）
-- 你的答案：




-- 题1.6：查询七年级1班和七年级2班的学生（使用 IN）
-- 你的答案：




-- 题1.7：按成绩从高到低显示所有学生
-- 你的答案：




-- 题1.8：显示成绩最高的3名学生
-- 你的答案：




-- 题1.9：查询有多少名学生
-- 你的答案：




-- 题1.10：查询所有学生来自哪些班级（不重复）
-- 你的答案：




-- ========================================
-- 第2关：聚合与分组（共8题）
-- ========================================

-- 题2.1：计算所有学生的平均成绩
-- 你的答案：




-- 题2.2：找出最高分和最低分
-- 你的答案：




-- 题2.3：统计每个班级有多少人
-- 你的答案：




-- 题2.4：统计男生和女生的人数
-- 你的答案：




-- 题2.5：计算每个班级的平均成绩
-- 你的答案：




-- 题2.6：找出平均成绩大于85分的班级
-- 你的答案：




-- 题2.7：统计每个班级的最高分、最低分、平均分
-- 你的答案：




-- 题2.8：找出人数超过2人的班级
-- 你的答案：




-- ========================================
-- 第3关：多表查询（共6题）
-- ========================================

-- 题3.1：查询每个学生的考试成绩（显示学生名、课程名、成绩）
-- 你的答案：




-- 题3.2：查询"小明"的所有考试成绩
-- 你的答案：




-- 题3.3：查询"数学"课程的所有成绩
-- 你的答案：




-- 题3.4：查询每个学生的考试科目数和平均成绩
-- 你的答案：




-- 题3.5：查询每门课程的平均成绩
-- 你的答案：




-- 题3.6：找出数学成绩最高的学生
-- 你的答案：




-- ========================================
-- 第4关：综合挑战（共5题）
-- ========================================

-- 题4.1：给每个学生的成绩添加等级评价
-- 优秀(>=90), 良好(>=80), 及格(>=60), 不及格(<60)
-- 你的答案：




-- 题4.2：统计每个等级有多少人
-- 你的答案：




-- 题4.3：找出每个班级成绩最好的学生
-- 提示：使用子查询或排序
-- 你的答案：




-- 题4.4：计算每个学生的总分和平均分，并排名
-- 你的答案：




-- 题4.5：设计一个查询：显示学生信息，包括：
-- 姓名、班级、入学成绩、考试科目数、考试平均分、等级
-- 你的答案：




-- ========================================
-- 答案区（先自己做再看！）
-- ========================================

/*
【第1关答案】

1.1
SELECT name, class_name FROM students;

1.2
SELECT * FROM students WHERE gender = 'F';

1.3
SELECT * FROM students WHERE age > 14;

1.4
SELECT * FROM students WHERE score BETWEEN 80 AND 90;

1.5
SELECT * FROM students WHERE name LIKE '小%';

1.6
SELECT * FROM students WHERE class_name IN ('七年级1班', '七年级2班');

1.7
SELECT * FROM students ORDER BY score DESC;

1.8
SELECT * FROM students ORDER BY score DESC LIMIT 3;

1.9
SELECT COUNT(*) AS 学生人数 FROM students;

1.10
SELECT DISTINCT class_name FROM students;
*/

/*
【第2关答案】

2.1
SELECT AVG(score) AS 平均成绩 FROM students;

2.2
SELECT MAX(score) AS 最高分, MIN(score) AS 最低分 FROM students;

2.3
SELECT class_name, COUNT(*) AS 人数
FROM students
GROUP BY class_name;

2.4
SELECT gender, COUNT(*) AS 人数
FROM students
GROUP BY gender;

2.5
SELECT class_name, AVG(score) AS 平均成绩
FROM students
GROUP BY class_name;

2.6
SELECT class_name, AVG(score) AS 平均成绩
FROM students
GROUP BY class_name
HAVING AVG(score) > 85;

2.7
SELECT class_name,
       MAX(score) AS 最高分,
       MIN(score) AS 最低分,
       ROUND(AVG(score), 2) AS 平均分
FROM students
GROUP BY class_name;

2.8
SELECT class_name, COUNT(*) AS 人数
FROM students
GROUP BY class_name
HAVING COUNT(*) > 2;
*/

/*
【第3关答案】

3.1
SELECT s.name AS 学生, c.name AS 课程, sc.score AS 成绩
FROM scores sc
JOIN students s ON sc.student_id = s.id
JOIN courses c ON sc.course_id = c.id;

3.2
SELECT c.name AS 课程, sc.score AS 成绩
FROM scores sc
JOIN courses c ON sc.course_id = c.id
JOIN students s ON sc.student_id = s.id
WHERE s.name = '小明';

3.3
SELECT s.name AS 学生, sc.score AS 成绩
FROM scores sc
JOIN students s ON sc.student_id = s.id
JOIN courses c ON sc.course_id = c.id
WHERE c.name = '数学';

3.4
SELECT s.name AS 学生,
       COUNT(sc.id) AS 科目数,
       ROUND(AVG(sc.score), 2) AS 平均成绩
FROM students s
LEFT JOIN scores sc ON s.id = sc.student_id
GROUP BY s.id, s.name;

3.5
SELECT c.name AS 课程,
       COUNT(*) AS 考试人数,
       ROUND(AVG(sc.score), 2) AS 平均成绩
FROM courses c
JOIN scores sc ON c.id = sc.course_id
GROUP BY c.id, c.name;

3.6
SELECT s.name AS 学生, sc.score AS 数学成绩
FROM scores sc
JOIN students s ON sc.student_id = s.id
JOIN courses c ON sc.course_id = c.id
WHERE c.name = '数学'
ORDER BY sc.score DESC
LIMIT 1;
*/

/*
【第4关答案】

4.1
SELECT name, score,
       CASE
           WHEN score >= 90 THEN '优秀'
           WHEN score >= 80 THEN '良好'
           WHEN score >= 60 THEN '及格'
           ELSE '不及格'
       END AS 等级
FROM students;

4.2
SELECT
    CASE
        WHEN score >= 90 THEN '优秀'
        WHEN score >= 80 THEN '良好'
        WHEN score >= 60 THEN '及格'
        ELSE '不及格'
    END AS 等级,
    COUNT(*) AS 人数
FROM students
GROUP BY 等级;

4.3
SELECT s.class_name, s.name, s.score
FROM students s
WHERE s.score = (
    SELECT MAX(score)
    FROM students
    WHERE class_name = s.class_name
)
ORDER BY s.class_name;

4.4
SELECT s.name AS 学生,
       s.class_name AS 班级,
       SUM(sc.score) AS 总分,
       ROUND(AVG(sc.score), 2) AS 平均分
FROM students s
JOIN scores sc ON s.id = sc.student_id
GROUP BY s.id, s.name, s.class_name
ORDER BY 平均分 DESC;

4.5
SELECT s.name AS 姓名,
       s.class_name AS 班级,
       s.score AS 入学成绩,
       COUNT(sc.id) AS 考试科目数,
       ROUND(AVG(sc.score), 2) AS 考试平均分,
       CASE
           WHEN AVG(sc.score) >= 90 THEN '优秀'
           WHEN AVG(sc.score) >= 80 THEN '良好'
           WHEN AVG(sc.score) >= 60 THEN '及格'
           ELSE '不及格'
       END AS 等级
FROM students s
LEFT JOIN scores sc ON s.id = sc.student_id
GROUP BY s.id, s.name, s.class_name, s.score
ORDER BY 考试平均分 DESC;
*/


-- ========================================
-- 评分标准
-- ========================================
/*
第1关（10题）：每题1分，共10分
第2关（8题）：每题2分，共16分
第3关（6题）：每题3分，共18分
第4关（5题）：每题6分，共30分
附加创意分：最高26分

总分100分，评分等级：
90-100分：SQL大师！
70-89分：SQL高手
50-69分：SQL学徒
30-49分：继续加油
0-29分：需要复习教程
*/
