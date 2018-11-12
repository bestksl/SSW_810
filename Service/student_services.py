# @Author: HaoxuanLi  
# @Date 2018/11/11
# CWID: 10434197
from haoxuanli_810_09.DAO.dao import Dao
from haoxuanli_810_09.Domain.Student import Student


class StudentService:
    def __init__(self):
        self.dao = Dao.get_instance()
        self.table_exist = False

    def save_student(self, student: Student):
        if not self.table_exist:
            raise Exception(f"Error: student table not exist")
        sql = '''insert into student values (?,?,?)'''
        args = (student.cwid, student.name, student.major_name)
        self.dao.execute_sql(sql, args)

    def create_student_table(self, header: tuple):
        sql = f'''create table student ('''
        for i in range(0, len(header)):
            sql += f'''{header[i]},'''
        sql = sql[:-1] + ''');'''
        self.dao.execute_sql(sql)
        self.table_exist = True

    def find_student(self, cwid: str):
        sql = '''select cwid, name, major_name from student where student.cwid=?'''
        arg = (cwid,)
        result_tuple = self.dao.execute_sql(sql, arg)[0]
        result_stu = Student(result_tuple[0], result_tuple[1], result_tuple[2])
        return result_stu