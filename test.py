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


class MyTest(unittest.TestCase):
    dao = Dao.get_instance()

    def test_dao(self):
        self.dao.execute_sql("create table test (id,name)")

    def test_insert(self):
        self.dao.execute_sql('''insert into test values (?,?)''', ('149', 'will'))

    def test_query(self):
        print(self.dao.execute_sql('''select * from test where name=?''', ('ksl',)))
