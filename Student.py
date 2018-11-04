# Haoxuan Li
# Student ID: 10434197
from haoxuanli_810_09.People import People


class Student(People):

    def say(self):
        print("Thank you professor!")

    def __init__(self, cwid: str, name: str, major: str):
        self.cwid = cwid
        self.name = name
        self.major = major
        self.Courses = dict()

    def add_course(self, course_name: str, score: str):
        self.Courses[course_name] = score

    def pt_show(self):
        return [self.cwid, self.name, list(self.Courses.keys())]

    @staticmethod
    def get_fields():
        return ["CWID", "Name", "Completed Course"]
