# @Author: HaoxuanLi  
# @Date 2018/11/11
# CWID: 10434197
from haoxuanli_810_09.DAO.dao import Dao
from haoxuanli_810_09.Domain.grade import Grade
from haoxuanli_810_09.Utils.FileReader import FileReader


class GradeService:
    def __init__(self):
        self.dao = Dao.get_instance()

    def save_grade(self, grade: Grade):
        if not self.dao.if_exist("grade"):
            raise Exception(f"Error: grade table not exist")
        sql = '''insert into grade values (?,?,?,?)'''
        args = (grade.stu_id, grade.course_name, grade.score, grade.ins_id)
        self.dao.execute_sql(sql, args)

    def create_grade_table(self, header: tuple):
        self.dao.create_table("grade", header)

    def find_grade(self, stu_id: str, course_name: str):
        sql = '''select Student_CWID, Course, Grade,Instructor_CWID from grade where grade.Student_CWID=? and grade.Course=?'''
        arg = (stu_id, course_name)
        result_tuple = self.dao.execute_sql(sql, arg)[0]
        result_grade = Grade(result_tuple[0], result_tuple[1], result_tuple[2], result_tuple[3])
        return result_grade

    def read_grade_from_file(self, path: str):
        if self.dao.if_exist("grade"):
            return
        lines = FileReader.read_lines(path)
        header = [attr + " varchar(50)" for attr in lines[0]]
        header[len(header) - 1] += ", PRIMARY KEY(Student_CWID, Course)"
        self.create_grade_table(tuple(header))
        for attr in lines[1:len(lines)]:
            grade = Grade(attr[0], attr[1], attr[2], attr[3])
            self.save_grade(grade)

    def most_frequent_grade(self):
        sql = '''select Grade, count(*)  from grade group by grade.Grade order by grade.Grade asc limit 1'''
        result = self.dao.execute_sql(sql)
        return result

    def find_signed_courses(self, cwid: str):
        sql = '''select Course  from grade where grade.Student_CWID=?'''
        arg = (cwid,)
        result = self.dao.execute_sql(sql, arg)
        return result

    def get_grades_course_name(self):
        pass
