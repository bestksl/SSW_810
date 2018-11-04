import os
import unittest

from haoxuanli_810_09.Repository import Repository
from haoxuanli_810_09.Utils import Utils


class MyTest(unittest.TestCase):
    stevens = Repository(os.path.abspath("stevens_dir"))

    def test_student_num(self):
        file = open("stevens_dir/students.txt")
        actual_student_num1 = len(self.stevens.students.values())
        actual_student_num2 = len([line for line in file])
        expect_student_num = len(Utils.read_lines("stevens_dir/students.txt"))
        self.assertEqual(expect_student_num, actual_student_num1)
        self.assertEqual(expect_student_num, actual_student_num2)

    def test_instructor_num(self):
        file = open("stevens_dir/instructors.txt")
        actual_instructor_num1 = len(self.stevens.instructors.values())
        actual_instructor_num2 = len([line for line in file])
        expect_instructor_num = len(Utils.read_lines("stevens_dir/instructors.txt"))
        self.assertEqual(expect_instructor_num, actual_instructor_num1)
        self.assertEqual(expect_instructor_num, actual_instructor_num2)
