# @Author: HaoxuanLi
# @Date 2018/11/4
# CWID: 10434197
import os
import unittest
import random
from haoxuanli_810_09.Domain.Student import Student
from haoxuanli_810_09.Domain.Repository import Repository
from haoxuanli_810_09.Domain.major import Major
from haoxuanli_810_09.Domain.instructor import Instructor
from haoxuanli_810_09.DAO.dao import Dao
from haoxuanli_810_09.Service.student_services import StudentService
from haoxuanli_810_09.Service.instructor_services import InstructorService


class MyTest(unittest.TestCase):
    dao = Dao.get_instance()
    sc = StudentService()
    ic = InstructorService()

    def test_dao(self):
        self.dao.execute_sql("create table test (id,name)")

    def test_insert(self):
        self.dao.execute_sql('''insert into test values (?,?)''', ('149', 'will'))

    def test_query(self):
        print(self.dao.execute_sql('''select * from test where name=?''', ('ksl',)))

    def test_create_student_table(self):
        # header = ("cwid varchar(50)", "name varchar(50)", "major_name varchar(50)")
        # self.sc.create_student_table(header)
        # stu = Student("15555", "kslksl", "software engineering")
        # self.sc.save_student(stu)
        stu_new = self.sc.find_student("15555")
        print(stu_new.cwid, stu_new.name, stu_new.major_name)

    def test_create_instructor_table(self):
        header = ("CWID varchar(50)", "NAME varchar(50)", "DEPT varchar(50)")
        self.ic.create_instructor_table(header)
        ins = Instructor("777555", "instrucname", "se")
        self.ic.save_instructor(ins)
        new_ins = self.ic.find_instructor("777555")
        print(new_ins.cwid, new_ins.name, new_ins.dept)
