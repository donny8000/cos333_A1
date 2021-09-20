#!/usr/bin/env python

#-----------------------------------------------------------------------
# reg.py
# Authors: Donovan Pearce and Annette Lee
#-----------------------------------------------------------------------

from sqlite3 import connect
from sys import stderr, exit, argv
from contextlib import closing
from reg_arg_parser import parse_args
from reg_wildcard import wildcard
from reg_table import print_table

#-----------------------------------------------------------------------

DATABASE_URL ='file:reg.sqlite?mode=ro'

def main():
    args = parse_args()
    dept_goal = wildcard(args.dept)
    num_goal = wildcard(args.num)
    area_goal = wildcard(args.area)
    title_goal = wildcard(args.title)

    try:
        with connect (DATABASE_URL, uri=True) as connection:

            with closing(connection.cursor()) as cursor:

                stmt_str = "SELECT classid, dept, coursenum, "
                stmt_str += "area, title "
                stmt_str += "FROM courses, classes, crosslistings "
                stmt_str += "WHERE classes.courseid = courses"
                stmt_str += ".courseid AND classes.courseid = "
                stmt_str += "crosslistings.courseid "
                stmt_str += "AND dept LIKE ? "
                stmt_str += "AND coursenum LIKE ? "
                stmt_str += "AND area LIKE ? "
                stmt_str += "AND title LIKE ? ESCAPE '\\'"
                cursor.execute(stmt_str, [dept_goal, num_goal,
				    area_goal, title_goal])

                row_list = []
                row = cursor.fetchone()

                while row is not None:
                    row_list.append(row)
                    row = cursor.fetchone()

            print_table (row_list)

    except Exception as ex:
        print(argv[0] + ": " + str(ex), file=stderr)
        exit(1)


#-----------------------------------------------------------------------

if __name__ == '__main__':
    main()
