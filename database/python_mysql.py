# ========================================
# Python 操作 MySQL 教程
# ========================================
# 学会用 Python 程序来操作数据库
# 前置要求：已完成 MySQL 快速入门教程

"""
安装 pymysql 库：
pip install pymysql

或者使用 mysql-connector-python（官方库）：
pip install mysql-connector-python
"""

import pymysql
from pymysql.cursors import DictCursor

# ========================================
# 第1节：连接数据库 (3分钟)
# ========================================

# 数据库连接配置
config = {
    'host': 'localhost',      # 数据库地址（本地是 localhost）
    'port': 3306,             # 端口（MySQL 默认 3306）
    'user': 'root',           # 用户名
    'password': 'your_password',  # 密码（改成你的密码）
    'database': 'school',     # 数据库名
    'charset': 'utf8mb4',     # 字符编码
}

# 方式1：基本连接
def connect_basic():
    """基本连接方式"""
    conn = pymysql.connect(**config)
    print("连接成功！")
    conn.close()  # 记得关闭连接

# 方式2：使用 with 语句（推荐，自动关闭）
def connect_with():
    """推荐的连接方式（自动关闭）"""
    with pymysql.connect(**config) as conn:
        print("连接成功！")
        # 这里执行数据库操作
    # 离开 with 块后自动关闭连接


# ========================================
# 第2节：查询数据 SELECT (5分钟)
# ========================================

def query_students():
    """查询所有学生"""
    with pymysql.connect(**config) as conn:
        with conn.cursor() as cursor:  # 创建游标
            # 执行 SQL
            sql = "SELECT * FROM students"
            cursor.execute(sql)

            # 获取所有结果
            results = cursor.fetchall()

            # 遍历结果
            for row in results:
                print(row)  # 每行是一个元组

def query_students_dict():
    """查询学生（返回字典格式，更易读）"""
    with pymysql.connect(**config) as conn:
        # DictCursor 让结果变成字典而不是元组
        with conn.cursor(DictCursor) as cursor:
            sql = "SELECT name, class_name, score FROM students"
            cursor.execute(sql)

            for row in cursor.fetchall():
                print(f"姓名: {row['name']}, 班级: {row['class_name']}, 成绩: {row['score']}")

def query_with_condition():
    """条件查询"""
    with pymysql.connect(**config) as conn:
        with conn.cursor(DictCursor) as cursor:
            # 使用参数化查询（防止 SQL 注入）
            class_name = "七年级1班"
            min_score = 80

            sql = "SELECT * FROM students WHERE class_name = %s AND score >= %s"
            cursor.execute(sql, (class_name, min_score))  # 参数作为元组传入

            for row in cursor.fetchall():
                print(row)


# ========================================
# 第3节：插入数据 INSERT (5分钟)
# ========================================

def insert_student(name, gender, age, class_name, score):
    """插入一个学生"""
    with pymysql.connect(**config) as conn:
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO students (name, gender, age, class_name, score)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (name, gender, age, class_name, score))
            conn.commit()  # 提交事务（重要！）
            print(f"插入成功！新增ID: {cursor.lastrowid}")

def insert_many_students(students_list):
    """批量插入学生"""
    with pymysql.connect(**config) as conn:
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO students (name, gender, age, class_name, score)
                VALUES (%s, %s, %s, %s, %s)
            """
            # executemany 批量执行
            cursor.executemany(sql, students_list)
            conn.commit()
            print(f"批量插入成功！共插入 {cursor.rowcount} 条记录")


# ========================================
# 第4节：更新数据 UPDATE (5分钟)
# ========================================

def update_student_score(student_id, new_score):
    """更新学生成绩"""
    with pymysql.connect(**config) as conn:
        with conn.cursor() as cursor:
            sql = "UPDATE students SET score = %s WHERE id = %s"
            affected = cursor.execute(sql, (new_score, student_id))
            conn.commit()
            print(f"更新成功！影响了 {affected} 行")

def update_student_class(old_class, new_class):
    """批量更新班级"""
    with pymysql.connect(**config) as conn:
        with conn.cursor() as cursor:
            sql = "UPDATE students SET class_name = %s WHERE class_name = %s"
            affected = cursor.execute(sql, (new_class, old_class))
            conn.commit()
            print(f"更新成功！影响了 {affected} 行")


# ========================================
# 第5节：删除数据 DELETE (5分钟)
# ========================================

def delete_student(student_id):
    """删除一个学生"""
    with pymysql.connect(**config) as conn:
        with conn.cursor() as cursor:
            sql = "DELETE FROM students WHERE id = %s"
            affected = cursor.execute(sql, (student_id,))
            conn.commit()
            print(f"删除成功！影响了 {affected} 行")

def delete_low_scores(min_score=60):
    """删除低分学生（谨慎使用！）"""
    with pymysql.connect(**config) as conn:
        with conn.cursor() as cursor:
            # 先查询要删除的记录
            cursor.execute("SELECT * FROM students WHERE score < %s", (min_score,))
            to_delete = cursor.fetchall()
            print(f"将要删除 {len(to_delete)} 条记录")

            # 确认后再删除
            # sql = "DELETE FROM students WHERE score < %s"
            # cursor.execute(sql, (min_score,))
            # conn.commit()


# ========================================
# 第6节：事务处理 (5分钟)
# ========================================

def transfer_score(from_id, to_id, points):
    """模拟：从一个学生转移分数到另一个学生（事务示例）"""
    conn = pymysql.connect(**config)
    try:
        with conn.cursor(DictCursor) as cursor:
            # 开始事务（pymysql 默认就在事务中）

            # 1. 查询双方分数
            cursor.execute("SELECT score FROM students WHERE id = %s FOR UPDATE", (from_id,))
            from_student = cursor.fetchone()

            cursor.execute("SELECT score FROM students WHERE id = %s FOR UPDATE", (to_id,))
            to_student = cursor.fetchone()

            if not from_student or not to_student:
                raise Exception("学生不存在")

            if from_student['score'] < points:
                raise Exception("分数不够")

            # 2. 扣除分数
            cursor.execute(
                "UPDATE students SET score = score - %s WHERE id = %s",
                (points, from_id)
            )

            # 3. 增加分数
            cursor.execute(
                "UPDATE students SET score = score + %s WHERE id = %s",
                (points, to_id)
            )

            # 4. 提交事务
            conn.commit()
            print(f"转移成功！{points}分已从{from_id}转移到{to_id}")

    except Exception as e:
        # 出错则回滚
        conn.rollback()
        print(f"转移失败：{e}")
    finally:
        conn.close()


# ========================================
# 第7节：实用函数封装 (5分钟)
# ========================================

class StudentManager:
    """学生管理类（封装常用操作）"""

    def __init__(self, config):
        self.config = config

    def _get_connection(self):
        """获取数据库连接"""
        return pymysql.connect(**self.config, cursorclass=DictCursor)

    def get_all(self):
        """获取所有学生"""
        with self._get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM students ORDER BY score DESC")
                return cursor.fetchall()

    def get_by_id(self, student_id):
        """根据ID获取学生"""
        with self._get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))
                return cursor.fetchone()

    def search(self, keyword):
        """搜索学生"""
        with self._get_connection() as conn:
            with conn.cursor() as cursor:
                sql = "SELECT * FROM students WHERE name LIKE %s"
                cursor.execute(sql, (f"%{keyword}%",))
                return cursor.fetchall()

    def add(self, name, gender='M', age=None, class_name=None, score=None):
        """添加学生"""
        with self._get_connection() as conn:
            with conn.cursor() as cursor:
                sql = """
                    INSERT INTO students (name, gender, age, class_name, score)
                    VALUES (%s, %s, %s, %s, %s)
                """
                cursor.execute(sql, (name, gender, age, class_name, score))
                conn.commit()
                return cursor.lastrowid

    def update(self, student_id, **kwargs):
        """更新学生信息"""
        if not kwargs:
            return 0

        with self._get_connection() as conn:
            with conn.cursor() as cursor:
                # 动态构建 SQL
                set_clause = ", ".join([f"{k} = %s" for k in kwargs.keys()])
                values = list(kwargs.values()) + [student_id]

                sql = f"UPDATE students SET {set_clause} WHERE id = %s"
                affected = cursor.execute(sql, values)
                conn.commit()
                return affected

    def delete(self, student_id):
        """删除学生"""
        with self._get_connection() as conn:
            with conn.cursor() as cursor:
                affected = cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
                conn.commit()
                return affected

    def get_statistics(self):
        """获取统计数据"""
        with self._get_connection() as conn:
            with conn.cursor() as cursor:
                # 总体统计
                cursor.execute("""
                    SELECT
                        COUNT(*) as total,
                        AVG(score) as avg_score,
                        MAX(score) as max_score,
                        MIN(score) as min_score
                    FROM students
                """)
                overall = cursor.fetchone()

                # 按班级统计
                cursor.execute("""
                    SELECT
                        class_name,
                        COUNT(*) as count,
                        AVG(score) as avg_score
                    FROM students
                    GROUP BY class_name
                """)
                by_class = cursor.fetchall()

                return {
                    'overall': overall,
                    'by_class': by_class
                }


# ========================================
# 第8节：综合示例 (5分钟)
# ========================================

def main():
    """综合示例：学生成绩管理系统"""

    # 创建管理器
    manager = StudentManager(config)

    print("=" * 50)
    print("学生成绩管理系统")
    print("=" * 50)

    # 1. 显示所有学生
    print("\n【所有学生】")
    for s in manager.get_all():
        print(f"  {s['name']} - {s['class_name']} - {s['score']}分")

    # 2. 搜索学生
    print("\n【搜索"小"】")
    for s in manager.search("小"):
        print(f"  {s['name']} - {s['class_name']}")

    # 3. 添加学生
    print("\n【添加学生】")
    new_id = manager.add("小新", "M", 14, "七年级1班", 85.0)
    print(f"  添加成功，ID: {new_id}")

    # 4. 更新学生
    print("\n【更新学生】")
    manager.update(new_id, score=90.0, class_name="七年级2班")
    print(f"  更新成功")

    # 5. 查看统计
    print("\n【统计数据】")
    stats = manager.get_statistics()
    print(f"  总人数: {stats['overall']['total']}")
    print(f"  平均分: {stats['overall']['avg_score']:.2f}")
    print(f"  最高分: {stats['overall']['max_score']}")

    # 6. 删除测试学生
    print("\n【删除测试学生】")
    manager.delete(new_id)
    print("  删除成功")


# ========================================
# 错误处理最佳实践
# ========================================

def safe_query(sql, params=None):
    """安全的查询函数（带错误处理）"""
    try:
        with pymysql.connect(**config) as conn:
            with conn.cursor(DictCursor) as cursor:
                cursor.execute(sql, params)
                return cursor.fetchall()
    except pymysql.Error as e:
        print(f"数据库错误: {e}")
        return []
    except Exception as e:
        print(f"其他错误: {e}")
        return []


# ========================================
# 学习建议
# ========================================
"""
【重要知识点】

1. 连接数据库步骤：
   - 导入 pymysql
   - 配置连接参数
   - 使用 with 语句连接
   - 创建游标
   - 执行 SQL
   - 获取结果
   - commit()（增删改时）

2. 防止 SQL 注入：
   - 永远使用参数化查询 %s
   - 不要用字符串拼接 f"WHERE name = '{name}'"
   - 参数作为元组传入 execute(sql, (param1, param2))

3. 事务处理：
   - 默认在事务中
   - 增删改后要 commit()
   - 出错要 rollback()

4. 游标类型：
   - 默认返回元组 (1, '小明', 14)
   - DictCursor 返回字典 {'id': 1, 'name': '小明'}

【进阶学习】

1. 使用 ORM（对象关系映射）
   - SQLAlchemy
   - Django ORM
   - Peewee

2. 连接池
   - DBUtils
   - SQLAlchemy 连接池

3. 异步操作
   - aiomysql
   - databases

【练习任务】

1. 写一个函数：根据班级查询学生
2. 写一个函数：批量更新学生成绩
3. 写一个函数：导出学生数据到 CSV
4. 写一个函数：计算每个学生的成绩排名
"""


# ========================================
# 运行示例（取消注释测试）
# ========================================

if __name__ == "__main__":
    # 注意：运行前需要修改 config 中的密码

    # 简单测试
    print("Python MySQL 教程加载成功！")
    print("请修改 config 中的密码后运行示例代码")

    # 运行综合示例
    # main()
