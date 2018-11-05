# @Author: HaoxuanLi
# @Date 2018/11/4
# CWID: 10434197
from haoxuanli_810_09.People import People
from haoxuanli_810_09.major import Major


class Student(People):

    def say(self):
        print("Thank you professor!")

    def __init__(self, cwid: str, name: str, major: Major):
        self.cwid = cwid
        self.name = name
        self.major = major
        self.Courses = dict()

    def add_course(self, course_name: str, score: str):
        self.Courses[course_name] = score

    def pt_show(self):
        remaining_courses = self.major.get_remaining_courses(self.Courses)
        remaining_electives = [course for course in remaining_courses.keys() if
                               remaining_courses[course] == "E"]
        remaining_required = [course for course in remaining_courses.keys() if
                              remaining_courses[course] == "R"]
        if_required = lambda: None if len(remaining_electives) < len(
            [course for course in self.major.courses.keys() if
             self.major.courses[course] == "E"]) else remaining_electives
        return [self.cwid, self.name, self.major.name, list(self.Courses.keys()), remaining_required, if_required()]

    @staticmethod
    def get_fields():
        return ["CWID", "Name", "Major", "Completed Course", "Required", "Electives"]
