# @Author: HaoxuanLi  
# @Date 2018/11/10
# CWID: 10434197
import sqlite3


class Dao:

    def __init__(self, db_name: str):
        self.db_name = db_name
        self.con = None

    def open_close(self, func: function):
        def inner(self):
            self.con = sqlite3.connect(self.db_name)
            cursor = self.con.cursor()
            result_list = None
            try:
                return_value = func(self)
                if type(return_value) is list and type(return_value[1]) is tuple:
                    cursor.execute(return_value[0], return_value[1])
                elif type(return_value) is list and type(return_value[1]) is not tuple:
                    for sql in return_value:
                        cursor.execute(sql)
                else:
                    cursor.execute(return_value)
                result_list = cursor.fetchall()
            except Exception as e:
                self.con.rollback()
                print(f"some thing wrong and the database {self.db_name} was rollback")
            finally:
                self.con.commit()
                self.con.close()
            return result_list

        return inner

    @open_close
    def execute_sql(self, *args):
        if len(*args) == 1:
            return args[0]
        else:
            return [item for item in args]
