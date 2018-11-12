# @Author: HaoxuanLi  
# @Date 2018/11/11
# CWID: 10434197
from haoxuanli_810_09.DAO.dao import Dao
from haoxuanli_810_09.Domain.instructor import Instructor


class InstructorService:
    def __init__(self):
        self.dao = Dao.get_instance()
        self.table_exist = False

    def save_instructor(self, instructor: Instructor):
        if not self.table_exist:
            raise Exception(f"Error: instructor table not exist")
        sql = '''insert into instructor values (?,?,?)'''
        args = (instructor.cwid, instructor.name, instructor.dept)
        self.dao.execute_sql(sql, args)

    def create_instructor_table(self, header: tuple):
        sql = f'''create table instructor ('''
        for i in range(0, len(header)):
            sql += f'''{header[i]},'''
        sql = sql[:-1] + ''');'''
        self.dao.execute_sql(sql)
        self.table_exist = True

    def find_instructor(self, cwid: str):
        sql = '''select CWID, NAME, DEPT from instructor where instructor.CWID=?'''
        arg = (cwid,)
        result_tuple = self.dao.execute_sql(sql, arg)[0]
        result_ins = Instructor(result_tuple[0], result_tuple[1], result_tuple[2])
        return result_ins
