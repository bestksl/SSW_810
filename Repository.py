# Haoxuan Li
# Student ID: 10434197
from .Student import Student
from .instructor import Instructor
from .grade import Grade
import os
from haoxuanli_810_09.Utils import Utils
from prettytable import PrettyTable
from operator import itemgetter


class Repository:
    def __init__(self, init_dir: str):
        self.students = dict()  # key: student_CWID  value: student(OBJ)
        self.instructors = dict()  # key: instructor_CWID  value: instructor(OBJ)
        self.grades = dict()  # key: (student_CWID, course_name)  value: grade(OBJ)
        self.students_path = os.path.join(init_dir, "students.txt")
        self.instructors_path = os.path.join(init_dir, "instructors.txt")
        self.grades_path = os.path.join(init_dir, "grades.txt")
        self.read_student(self.students_path)
        self.read_instructors(self.instructors_path)
        self.read_grades(self.grades_path)

    def read_student(self, path: str):
        for cwid, name, major in Utils.read_lines(path):
            student = Student(cwid, name, major)
            self.students[student.cwid] = student
        return self.students

    def read_instructors(self, path: str):
        for cwid, name, dept in Utils.read_lines(path):
            instructor = Instructor(cwid, name, dept)
            self.instructors[instructor.cwid] = instructor
        return self.instructors

    def read_grades(self, path: str):
        for s_cwid, course_name, score, ins_id in Utils.read_lines(path):
            grade = Grade(s_cwid, course_name, score, ins_id)
            self.grades[grade.stu_id, grade.course_name] = grade
        return self.grades

    def show_students(self):
        student_summary_table = PrettyTable()
        student_summary_table.field_names = Student.get_fields()
        sorted_students = sorted(self.students.items(), key=itemgetter(0))  # <-------------- here!
        for item in sorted_students:
            student_summary_table.add_row(item[1].pt_show())  # <-------------- here!
        print(student_summary_table.get_string())

    def show_instructors(self):
        instructor_summary_table = PrettyTable()
        instructor_summary_table.field_names = Instructor.get_fields()
        sorted_instructors = sorted(self.instructors.items(), key=itemgetter(0))  # <-------------- here!
        for item in sorted_instructors:
            for data in item[1].pt_show():  # <-------------- here!
                instructor_summary_table.add_row(data)
        print(instructor_summary_table.get_string())

    def analysis_grades(self):
        for grade in self.grades.values():
            self.students.get(grade.stu_id).add_course(grade.course_name, grade.score)
            self.instructors.get(grade.ins_id).add_course(grade.course_name)
