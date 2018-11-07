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
        remaining_courses = self.major.get_remaining_courses(self.get_pass_courses())
        remaining_electives = [course for course in remaining_courses.keys() if
                               remaining_courses[course] == "E"]
        remaining_required = [course for course in remaining_courses.keys() if
                              remaining_courses[course] == "R"]
        return [self.cwid, self.name, self.major.name,
                (lambda: list(self.get_pass_courses().keys()) if len(self.get_pass_courses().keys()) > 0 else None)(),
                remaining_required,
                (lambda: None if len(remaining_electives) < len(
                    [course for course in self.major.courses.keys() if
                     self.major.courses[course] == "E"]) else remaining_electives)()]

    def get_pass_courses(self):  # <--------------- Here is the change!!!!!!!!!!!
        pass_courses_names = [c_name for c_name in self.Courses.keys() if self.Courses[c_name] != "F"]
        pass_courses = dict()
        for p_c_name in pass_courses_names:
            pass_courses[p_c_name] = self.Courses[p_c_name]
        return pass_courses

    @staticmethod
    def get_fields():
        return ["CWID", "Name", "Major", "Completed Course", "Remaining Required", "Remaining Electives"]
