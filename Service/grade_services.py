# @Author: HaoxuanLi  
# @Date 2018/11/11
# CWID: 10434197
from haoxuanli_810_09.DAO.dao import Dao
from haoxuanli_810_09.Domain.grade import Grade


class GradeService:
    def __init__(self):
        self.dao = Dao.get_instance()
        self.table_exist = False

    def save_grade(self, grade: Grade):
        if not self.table_exist:
            raise Exception(f"Error: grade table not exist")
        sql = '''insert into grade values (?,?,?,?)'''
        args = (grade.stu_id, grade.course_name, grade.score, grade.ins_id)
        self.dao.execute_sql(sql, args)

    def create_grade_table(self, header: tuple):
        sql = f'''create table grade ('''
        for i in range(0, len(header)):
            sql += f'''{header[i]},'''
        sql = sql[:-1] + ''');'''
        self.dao.execute_sql(sql)
        self.table_exist = True

    def find_grade(self, stu_id: str, course_name: str):
        sql = '''select Srudent_CWID, Course, Grade,Instructor_CWID from grade where grade.Student_CWID=? and grade.Course=?'''
        arg = (stu_id, course_name)
        result_tuple = self.dao.execute_sql(sql, arg)[0]
        result_grade = Grade(result_tuple[0], result_tuple[1], result_tuple[2], result_tuple[3])
        return result_grade
