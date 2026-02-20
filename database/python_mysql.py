# ========================================
# Python 操作 MySQL 教程
# ========================================
# 学会用 Python 程序来操作数据库
# 前置要求：已完成 MySQL 快速入门教程
#
# 使用方法：
# 1. 先安装 pymysql：pip install pymysql
# 2. 修改下面的 config 中的密码
# 3. 逐节阅读代码，运行示例

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

# 【重要】数据库连接配置 - 请修改成你的密码！
config = {
    'host': 'localhost',      # 数据库地址（本地是 localhost）
    'port': 3306,             # 端口（MySQL 默认 3306）
    'user': 'root',           # 用户名
    'password': 'your_password',  # ← 改成你的密码！
    'database': 'school',     # 数据库名
    'charset': 'utf8mb4',     # 字符编码
}

# 方式1：基本连接（不推荐，需要手动关闭）
def connect_basic():
    """基本连接方式"""
    conn = pymysql.connect(**config)
    print("连接成功！")
    conn.close()  # 记得关闭连接，否则会占用资源

# 方式2：使用 with 语句（推荐，自动关闭）
def connect_with():
    """推荐的连接方式（自动关闭）"""
    with pymysql.connect(**config) as conn:
        print("连接成功！")
        # 这里执行数据库操作
    # 离开 with 块后自动关闭连接

# 【示例1.1】测试连接
if __name__ == "__main__":
    print("=== 第1节示例：测试连接 ===")
    # connect_basic()  # 方式1
    # connect_with()   # 方式2（推荐）


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

# 【示例2.1】查询所有学生
def example_query_all():
    """
    调用方式：直接运行函数
    返回：每行是一个元组 (id, name, gender, age, class_name, score, created_at)
    """
    print("=== 示例2.1：查询所有学生 ===")
    query_students()


def query_students_dict():
    """查询学生（返回字典格式，更易读）"""
    with pymysql.connect(**config) as conn:
        # DictCursor 让结果变成字典而不是元组
        with conn.cursor(DictCursor) as cursor:
            sql = "SELECT name, class_name, score FROM students"
            cursor.execute(sql)

            for row in cursor.fetchall():
                # row 是字典，可以用 key 访问
                print(f"姓名: {row['name']}, 班级: {row['class_name']}, 成绩: {row['score']}")

# 【示例2.2】用字典方式查询
def example_query_dict():
    """
    调用方式：直接运行函数
    优点：返回字典，可以用字段名访问，更直观
    """
    print("=== 示例2.2：字典方式查询 ===")
    query_students_dict()


def query_with_condition():
    """条件查询"""
    with pymysql.connect(**config) as conn:
        with conn.cursor(DictCursor) as cursor:
            # 使用参数化查询（防止 SQL 注入）
            class_name = "七年级1班"
            min_score = 80

            sql = "SELECT * FROM students WHERE class_name = %s AND score >= %s"
            # 参数作为元组传入
            cursor.execute(sql, (class_name, min_score))

            for row in cursor.fetchall():
                print(row)

# 【示例2.3】条件查询
def example_query_condition():
    """
    调用方式：
    可以修改 class_name 和 min_score 的值

    参数说明：
    - class_name: 班级名称
    - min_score: 最低分数
    """
    print("=== 示例2.3：条件查询 ===")
    query_with_condition()


# ========================================
# 第3节：插入数据 INSERT (5分钟)
# ========================================

def insert_student(name, gender, age, class_name, score):
    """
    插入一个学生

    参数说明：
    - name: 学生姓名，字符串，如 "小明"
    - gender: 性别，字符串 'M' 或 'F'
    - age: 年龄，整数，如 14
    - class_name: 班级，字符串，如 "七年级1班"
    - score: 成绩，数字，如 85.5
    """
    with pymysql.connect(**config) as conn:
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO students (name, gender, age, class_name, score)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (name, gender, age, class_name, score))
            conn.commit()  # 提交事务（重要！不提交数据不会保存）
            print(f"插入成功！新增ID: {cursor.lastrowid}")
            return cursor.lastrowid

# 【示例3.1】插入单个学生
def example_insert_one():
    """
    调用方式：
    insert_student("学生姓名", "性别", 年龄, "班级", 成绩)
    """
    print("=== 示例3.1：插入单个学生 ===")

    # 插入一个学生
    new_id = insert_student(
        name="小华",        # 学生姓名
        gender="M",         # 性别：M=男，F=女
        age=14,             # 年龄
        class_name="七年级3班",  # 班级
        score=88.5          # 成绩
    )
    print(f"新学生的ID是: {new_id}")


def insert_many_students(students_list):
    """
    批量插入学生

    参数说明：
    - students_list: 学生列表，是一个包含多个元组的列表

    示例参数：
    students_list = [
        ("学生A", "M", 14, "七年级1班", 85.0),
        ("学生B", "F", 13, "七年级2班", 90.0),
        ("学生C", "M", 14, "七年级1班", 78.5),
    ]

    注意：
    - 每个元组的顺序必须和 SQL 中的字段顺序一致
    - 元组内的数据类型要正确（字符串、数字）
    """
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
            return cursor.rowcount

# 【示例3.2】批量插入学生
def example_insert_many():
    """
    调用方式：
    先准备好学生列表，然后调用函数
    """
    print("=== 示例3.2：批量插入学生 ===")

    # 准备学生数据 - 这是一个列表，里面每个元素是一个元组
    # 元组的顺序：(姓名, 性别, 年龄, 班级, 成绩)
    students = [
        ("小龙", "M", 14, "七年级1班", 82.0),
        ("小凤", "F", 13, "七年级2班", 91.5),
        ("小虎", "M", 15, "七年级3班", 76.0),
    ]

    # 调用函数批量插入
    insert_many_students(students)


# ========================================
# 第4节：更新数据 UPDATE (5分钟)
# ========================================

def update_student_score(student_id, new_score):
    """
    更新学生成绩

    参数说明：
    - student_id: 学生ID（整数）
    - new_score: 新成绩（数字）
    """
    with pymysql.connect(**config) as conn:
        with conn.cursor() as cursor:
            sql = "UPDATE students SET score = %s WHERE id = %s"
            affected = cursor.execute(sql, (new_score, student_id))
            conn.commit()
            print(f"更新成功！影响了 {affected} 行")
            return affected

# 【示例4.1】更新学生成绩
def example_update_score():
    """
    调用方式：
    update_student_score(学生ID, 新成绩)
    """
    print("=== 示例4.1：更新学生成绩 ===")

    # 假设 ID=1 的学生成绩改为 99
    update_student_score(student_id=1, new_score=99.0)


def update_student_class(old_class, new_class):
    """
    批量更新班级

    参数说明：
    - old_class: 原班级名称
    - new_class: 新班级名称

    注意：会更新所有匹配的学生！
    """
    with pymysql.connect(**config) as conn:
        with conn.cursor() as cursor:
            sql = "UPDATE students SET class_name = %s WHERE class_name = %s"
            affected = cursor.execute(sql, (new_class, old_class))
            conn.commit()
            print(f"更新成功！影响了 {affected} 行")
            return affected

# 【示例4.2】批量更新班级
def example_update_class():
    """
    调用方式：
    update_student_class("原班级", "新班级")
    """
    print("=== 示例4.2：批量更新班级 ===")

    # 把"七年级3班"改名为"七年级(3)班"
    # update_student_class("七年级3班", "七年级(3)班")


# ========================================
# 第5节：删除数据 DELETE (5分钟)
# ========================================

def delete_student(student_id):
    """
    删除一个学生

    参数说明：
    - student_id: 学生ID（整数）

    警告：删除后无法恢复！
    """
    with pymysql.connect(**config) as conn:
        with conn.cursor() as cursor:
            sql = "DELETE FROM students WHERE id = %s"
            affected = cursor.execute(sql, (student_id,))
            conn.commit()
            print(f"删除成功！影响了 {affected} 行")
            return affected

# 【示例5.1】删除学生
def example_delete_one():
    """
    调用方式：
    delete_student(学生ID)

    注意：删除前最好先查询确认！
    """
    print("=== 示例5.1：删除学生 ===")

    # 先查询要删除的学生
    # ...
    # 确认后再删除
    # delete_student(student_id=100)


def delete_low_scores(min_score=60):
    """
    删除低分学生（演示用，实际不执行删除）

    参数说明：
    - min_score: 分数阈值，低于这个分数的会被删除
    """
    with pymysql.connect(**config) as conn:
        with conn.cursor() as cursor:
            # 先查询要删除的记录（安全做法）
            cursor.execute("SELECT * FROM students WHERE score < %s", (min_score,))
            to_delete = cursor.fetchall()
            print(f"将要删除 {len(to_delete)} 条记录：")
            for row in to_delete:
                print(f"  {row}")

            # 确认后再删除（这里注释掉了，防止误删）
            # sql = "DELETE FROM students WHERE score < %s"
            # cursor.execute(sql, (min_score,))
            # conn.commit()

# 【示例5.2】查询低分学生
def example_delete_low():
    """
    这个示例只查询不删除，演示安全做法
    """
    print("=== 示例5.2：查询低分学生 ===")
    delete_low_scores(min_score=60)


# ========================================
# 第6节：事务处理 (5分钟)
# ========================================

def transfer_score(from_id, to_id, points):
    """
    模拟：从一个学生转移分数到另一个学生（事务示例）

    参数说明：
    - from_id: 转出分数的学生ID
    - to_id: 接收分数的学生ID
    - points: 转移的分数

    事务的作用：
    - 要么全部成功，要么全部失败
    - 不会出现只扣分没加分的情况
    """
    conn = pymysql.connect(**config)
    try:
        with conn.cursor(DictCursor) as cursor:
            # 1. 查询双方分数
            cursor.execute("SELECT score FROM students WHERE id = %s FOR UPDATE", (from_id,))
            from_student = cursor.fetchone()

            cursor.execute("SELECT score FROM students WHERE id = %s FOR UPDATE", (to_id,))
            to_student = cursor.fetchone()

            # 检查学生是否存在
            if not from_student or not to_student:
                raise Exception("学生不存在")

            # 检查分数是否足够
            if from_student['score'] < points:
                raise Exception(f"分数不够！当前只有 {from_student['score']} 分")

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
            print(f"转移成功！{points} 分已从学生{from_id}转移到学生{to_id}")

    except Exception as e:
        # 出错则回滚（撤销所有操作）
        conn.rollback()
        print(f"转移失败：{e}")

    finally:
        conn.close()

# 【示例6.1】事务演示
def example_transfer():
    """
    调用方式：
    transfer_score(转出学生ID, 接收学生ID, 分数)
    """
    print("=== 示例6.1：分数转移（事务） ===")

    # 从学生1转5分给学生2
    # transfer_score(from_id=1, to_id=2, points=5)


# ========================================
# 第7节：实用函数封装 (5分钟)
# ========================================

class StudentManager:
    """
    学生管理类（封装常用操作）

    使用方法：
    1. 创建管理器：manager = StudentManager(config)
    2. 调用方法：manager.get_all()
    """

    def __init__(self, config):
        """初始化，传入数据库配置"""
        self.config = config

    def _get_connection(self):
        """获取数据库连接（内部方法）"""
        return pymysql.connect(**self.config, cursorclass=DictCursor)

    def get_all(self):
        """获取所有学生"""
        with self._get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM students ORDER BY score DESC")
                return cursor.fetchall()

    def get_by_id(self, student_id):
        """
        根据ID获取学生

        参数：student_id - 学生ID
        返回：学生信息字典，或 None
        """
        with self._get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))
                return cursor.fetchone()

    def search(self, keyword):
        """
        搜索学生（按姓名模糊搜索）

        参数：keyword - 搜索关键词
        返回：匹配的学生列表
        """
        with self._get_connection() as conn:
            with conn.cursor() as cursor:
                sql = "SELECT * FROM students WHERE name LIKE %s"
                cursor.execute(sql, (f"%{keyword}%",))
                return cursor.fetchall()

    def add(self, name, gender='M', age=None, class_name=None, score=None):
        """
        添加学生

        参数：
        - name: 姓名（必填）
        - gender: 性别，默认 'M'
        - age: 年龄
        - class_name: 班级
        - score: 成绩

        返回：新学生的ID
        """
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
        """
        更新学生信息

        参数：
        - student_id: 学生ID
        - **kwargs: 要更新的字段，如 score=90, class_name="新班级"

        示例：
        manager.update(1, score=95, class_name="七年级2班")
        """
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
    """
    综合示例：学生成绩管理系统

    这个函数演示了 StudentManager 类的所有功能
    """

    # 【步骤1】创建管理器
    manager = StudentManager(config)

    print("=" * 50)
    print("学生成绩管理系统")
    print("=" * 50)

    # 【步骤2】显示所有学生
    print("\n【查询】所有学生：")
    students = manager.get_all()
    for s in students:
        print(f"  {s['id']:2d}. {s['name']} - {s['class_name']} - {s['score']}分")

    # 【步骤3】搜索单个学生
    print("\n【搜索】姓名包含'小'的学生：")
    results = manager.search("小")
    for s in results:
        print(f"  {s['name']} - {s['class_name']}")

    # 【步骤4】添加学生
    print("\n【添加】新学生：")
    new_id = manager.add(
        name="小新",           # 姓名
        gender="M",           # 性别
        age=14,               # 年龄
        class_name="七年级1班",  # 班级
        score=85.0            # 成绩
    )
    print(f"  添加成功！新学生ID: {new_id}")

    # 【步骤5】查看刚添加的学生
    print("\n【查询】刚添加的学生：")
    new_student = manager.get_by_id(new_id)
    print(f"  {new_student['name']} - {new_student['score']}分")

    # 【步骤6】更新学生信息
    print("\n【更新】学生信息：")
    manager.update(new_id, score=90.0, class_name="七年级2班")
    print(f"  已将ID={new_id}的成绩改为90分，班级改为七年级2班")

    # 再次查看
    updated = manager.get_by_id(new_id)
    print(f"  更新后：{updated['name']} - {updated['class_name']} - {updated['score']}分")

    # 【步骤7】查看统计数据
    print("\n【统计】整体数据：")
    stats = manager.get_statistics()
    print(f"  总人数: {stats['overall']['total']}")
    print(f"  平均分: {stats['overall']['avg_score']:.2f}")
    print(f"  最高分: {stats['overall']['max_score']}")
    print(f"  最低分: {stats['overall']['min_score']}")

    print("\n【统计】按班级：")
    for cls in stats['by_class']:
        print(f"  {cls['class_name']}: {cls['count']}人, 平均{cls['avg_score']:.2f}分")

    # 【步骤8】删除测试学生
    print("\n【删除】测试学生：")
    manager.delete(new_id)
    print(f"  已删除ID={new_id}的学生")


# ========================================
# 错误处理最佳实践
# ========================================

def safe_query(sql, params=None):
    """
    安全的查询函数（带错误处理）

    参数：
    - sql: SQL 语句
    - params: 参数（元组）

    返回：查询结果列表，出错返回空列表
    """
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
# 快速参考卡片
# ========================================
"""
╔══════════════════════════════════════════════════════════════╗
║                    Python MySQL 快速参考                      ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  【连接数据库】                                                ║
║  with pymysql.connect(**config) as conn:                     ║
║      with conn.cursor(DictCursor) as cursor:                 ║
║          cursor.execute(sql, params)                         ║
║                                                              ║
║  【查询】cursor.fetchall()  返回所有结果                        ║
║        cursor.fetchone()   返回一条结果                        ║
║                                                              ║
║  【增删改后】conn.commit()  提交事务                            ║
║                                                              ║
║  【参数化查询】使用 %s 占位符                                    ║
║  cursor.execute("SELECT * FROM students WHERE id = %s", (1,))║
║                                                              ║
║  【结果类型】                                                  ║
║  默认游标：返回元组 (1, '小明', 14)                              ║
║  DictCursor：返回字典 {'id': 1, 'name': '小明', 'age': 14}      ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""


# ========================================
# 学习建议
# ========================================
"""
【重要知识点】

1. 连接数据库步骤：
   - 导入 pymysql
   - 配置连接参数（config 字典）
   - 使用 with 语句连接
   - 创建游标 cursor
   - 执行 SQL
   - 获取结果
   - commit()（增删改时必须）

2. 防止 SQL 注入：
   - 永远使用参数化查询 %s
   - 不要用字符串拼接！❌ f"WHERE name = '{name}'"
   - 参数作为元组传入 execute(sql, (param1, param2))
   - 单个参数也要写成元组 (param,) ← 注意逗号！

3. 事务处理：
   - 默认在事务中
   - 增删改后要 commit()
   - 出错要 rollback()

4. 游标类型：
   - 默认返回元组 (1, '小明', 14)
   - DictCursor 返回字典 {'id': 1, 'name': '小明'}

【练习任务】

1. 写一个函数：根据班级查询学生
   提示：参考 query_with_condition 函数

2. 写一个函数：批量更新学生成绩
   提示：参考 update_student_score，使用 executemany

3. 写一个函数：导出学生数据到 CSV 文件
   提示：先查询，再用 Python 写入文件

4. 写一个函数：计算每个学生的成绩排名
   提示：用 SQL 排序，或用 Python 处理

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
"""


# ========================================
# 运行示例（取消注释测试）
# ========================================

if __name__ == "__main__":
    # 注意：运行前需要修改 config 中的密码！

    print("Python MySQL 教程加载成功！")
    print("请先修改 config 中的密码，然后运行示例代码")
    print()

    # ============ 取消下面的注释来运行示例 ============

    # 【第1节】测试连接
    # connect_with()

    # 【第2节】查询示例
    # example_query_all()      # 查询所有
    # example_query_dict()     # 字典方式查询
    # example_query_condition()  # 条件查询

    # 【第3节】插入示例
    # example_insert_one()     # 插入单个
    # example_insert_many()    # 批量插入

    # 【第4节】更新示例
    # example_update_score()   # 更新成绩
    # example_update_class()   # 批量更新班级

    # 【第5节】删除示例
    # example_delete_one()     # 删除学生
    # example_delete_low()     # 查询低分学生

    # 【第6节】事务示例
    # example_transfer()       # 分数转移

    # 【第8节】综合示例
    # main()  # 运行完整的学生管理系统示例
