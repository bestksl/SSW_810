# @Author: HaoxuanLi  
# @Date 2018/11/13
# CWID: 10434197
import os

from haoxuanli_810_09.Service.instructor_services import InstructorService
from haoxuanli_810_09.Service.student_services import StudentService
from haoxuanli_810_09.Service.grade_services import GradeService
from haoxuanli_810_09.Service.major_services import MajorService


class HW11_controller():

    def __init__(self, path: str):
        # init services layer
        self.ss = StudentService()
        self.i_s = InstructorService()
        self.gs = GradeService()
        # path
        self.init_path = os.path.abspath(path)
        self.grade_path = os.path.join(self.init_path, 'grades.txt')
        self.student_path = os.path.join(self.init_path, 'students.txt')
        self.instructor_path = os.path.join(self.init_path, 'instructors.txt')
        # init data from text file
        self.gs.read_grade_from_file(self.grade_path)
        self.ss.read_student_from_file(self.student_path)
        self.i_s.read_instructor_from_file(self.instructor_path)

    def answers(self):
        # question 1
        stu = self.ss.find_student("11461")
        print("student is", stu.cwid, stu.name, stu.major_name)

        # question 2
        result_list = self.ss.num_of_stu_by_major()
        for result in result_list:
            print(f"{result[0]}: student num = {result[1]}")

        # question 3
        result = self.gs.most_frequent_grade()
        print(f"most frequent score is {result[0][0]}, frequency is {result[0][1]}")

        # question 4
        stu_list = self.ss.get_all_student()
        for stu in stu_list:
            courses = self.gs.find_signed_courses(stu.cwid)
            for course_name in courses:
                grade = self.gs.find_grade(stu.cwid, course_name[0])
                print(f"stu_CWID: {stu.cwid} stu_Name: {stu.name} major: {stu.major_name} grade: {grade.score}")

        # question 5
        name_list=[]
