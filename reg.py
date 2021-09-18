#!/usr/bin/env python

#-----------------------------------------------------------------------
# reg.py
# Authors: Donovan Pearce and Annette Lee
#-----------------------------------------------------------------------

from reg_arg_parser import parse_args
from reg_wildcard import wildcard
from sqlite3 import connect
from sys import stderr, exit 
from contextlib import closing

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
			cursor = connection.cursor()

			with closing(connection.cursor()) as cursor:

				stmt_str = "SELECT classid, dept, coursenum, "
				stmt_str += "area, title "
				stmt_str += "FROM classes, courses, crosslistings "
				stmt_str += "WHERE classes.courseid = courses.courseid "
				stmt_str += "AND classes.courseid = "
				stmt_str += "crosslistings.courseid"
				# stmt_str += "AND dept LIKE ? AND coursenum LIKE ? "
				# stmt_str += "AND area LIKE ? AND title LIKE ?"
				cursor.execute(stmt_str)
				#[dept_goal, num_goal, area_goal, title_goal]

				row = cursor.fetchone()
				if (row is None):
					print ('Too bad...')
				# print ('classid:', str(row[0]))
				# print ('dept:', str(row[1]))
				# print ('coursenum:', str(row[2]))
				# print ('area:', str(row[3]))
				# print ('title:', str(row[4]))

	except Exception as ex:
		print(ex, file=stderr)
		exit(1)

	# if (dept != ''):
	# 	print('department: ' + dept)
	# if (num != ''):
	# 	print('num: ' + num)
	# if (area != ''):
	# 	print('area: ' + area)
	# if (title != ''):
	# 	print('title: ' + title)


#-----------------------------------------------------------------------

if __name__ == '__main__':
	main()
