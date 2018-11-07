# @Author: HaoxuanLi
# @Date 2018/11/4
# CWID: 10434197
import os
import unittest
import random
from haoxuanli_810_09.Student import Student
from haoxuanli_810_09.Repository import Repository
from haoxuanli_810_09.major import Major
from haoxuanli_810_09.instructor import Instructor


class MyTest(unittest.TestCase):
    stevens = Repository(os.path.abspath("stevens_dir"))

    # major test is included in this function
    def test_random_student(self):
        file = open("stevens_dir/students.txt")
        lines = file.readlines()
        file.close()
        target_index = random.randint(0, len(lines) - 1)
        random_student = None
        for index, line in enumerate(lines):
            if index == target_index:
                attrs = line.strip().split("\t")
                random_student = Student(attrs[0], attrs[1], self.stevens.majors[attrs[2]])
        # compare students
        self.assertTrue(self.compare(random_student, self.stevens.students[random_student.cwid]))

    # instructor test
    def test_random_instructor(self):
        file = open("stevens_dir/instructors.txt")
        lines = file.readlines()
        file.close()
        target_index = random.randint(0, len(lines) - 1)
        random_instructor = None
        for index, line in enumerate(lines):
            if index == target_index:
                attrs = line.strip().split("\t")
                random_instructor = Instructor(attrs[0], attrs[1], attrs[2])
                break
        # compare instructors   `
        self.assertTrue(self.compare(random_instructor, self.stevens.instructors[random_instructor.cwid]))

    # compare major
    @staticmethod
    def compare(obj1, obj2):
        if type(obj1) and type(obj2) is Student:
            if obj1.cwid == obj2.cwid and obj1.major == obj2.major and obj1.name == obj2.name:
                return True
            else:
                return False
        elif type(obj1) and type(obj2) is Instructor:
            print(obj1.cwid, obj1.cwid, obj1.dept)
            print(obj2.cwid, obj2.cwid, obj2.dept)
            if obj1.cwid == obj2.cwid and obj1.name == obj2.name and obj1.dept == obj2.dept:
                return True
            else:
                return False
        elif type(obj1) and type(obj2) is Major:
            if obj1.name == obj2.name and obj1.courses == obj2.courses:
                return True
            else:
                return False
        else:
            return False
