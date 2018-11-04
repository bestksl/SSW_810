# Haoxuan Li
# Student ID: 10434197
from collections import defaultdict
from haoxuanli_810_09.People import People


class Instructor(People):
    def say(self):
        print("Thank you professor!")

    def __init__(self, cwid: str, name: str, dept: str):
        self.cwid = cwid
        self.name = name
        self.dept = dept
        self.courses = defaultdict(int)

    def add_course(self, course_name):
        self.courses[course_name] += 1

    def pt_show(self):
        pt_list = []
        for course_name in self.courses.keys():
            pt_list.append([self.cwid, self.name, self.dept, course_name, self.courses[course_name]])
        return pt_list

    @staticmethod
    def get_fields():
        return ["CWID", "Name", "Dept", "Course", "Students"]
