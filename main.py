# Haoxuan Li
# Student ID: 10434197

import os

from haoxuanli_810_09.Repository import Repository


def main():
    # create a STEVENS Repository
    STEVEMS = Repository(os.path.abspath("stevens_dir"))

    # add courses to students and instructor
    STEVEMS.analysis_grades()

    # print student table
    STEVEMS.show_students()

    # print instructor table
    STEVEMS.show_instructors()


if __name__ == '__main__':
    main()
