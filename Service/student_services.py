# @Author: HaoxuanLi  
# @Date 2018/11/11
# CWID: 10434197
from haoxuanli_810_09.DAO.dao import Dao
from haoxuanli_810_09.Domain.Student import Student


class StudentService:
    def __init__(self):
        self.dao = Dao.get_instance()
        self.table_exist=False
    def save_student(self, student: Student):
        sql = ''
        self.dao.execute_sql(sql)

    def create_student_table(self):
        sql='create table '
        self.dao.execute_sql(sql)