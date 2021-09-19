#!/usr/bin/env python

#-----------------------------------------------------------------------
# regdetails.py
# Authors: Donovan Pearce and Annette Lee
#-----------------------------------------------------------------------

from regdetails_arg_parser import parse_args
from regdetails_table import print_table

#-----------------------------------------------------------------------

DATABASE_URL ='file:reg.sqlite?mode=ro'

def main():
	args = parse_args()
	id_goal = args.classid


	try: 
		with connect (DATABASE_URL, uri=True) as connection:
			cursor = connection.cursor()

			with closing(connection.cursor()) as cursor:

				stmt_str = "SELECT courseid, days, starttime, endtime, "
				stmt_str += "bldg, roomnum WHERE classid = ?" 

				cursor.execute(stmt_str, [id_goal])

				class_row = cursor.fetchone()

				if class_row is None:
					raise ValueError(
						'no class with classid %d exists' % id_goal)

				course_id_goal = class_row[0]

				stmt_str = "SELECT area, title, descrip, prereqs "
				stmt_str += "FROM courses WHERE courses.courseid = ?"

				cursor.execute(stmt_str, [course_id_goal])

				course_row = cursor.fetchone()

				stmt_str = "SELECT dept, coursenum from crosslistings "
				stmt_str += "WHERE crosslistings.courseid = ?"


				cursor.execute(stmt_str, [course_id_goal])

				crossliststings_list = [] 
				row = cursor.fetchone() 
				while row is not None:
					crosslistings_list.append(row)
					row = cursor.fetchone()

				stmt_str = "SELECT profid from courseprofs "
				stmt_str += "WHERE courseprofs.courseid = ?"

				cursor.execute(stmt_str, [course_id_goal])

				courseprofs_list = [] 
				row = cursor.fetchone() 
				while row is not None:
					courseprofs_list.append(row)
					row = cursor.fetchone()


				prof_list = []
				for courseprofs_row in courseprofs_list:
					stmt_str = "SELECT profname from profs "
					stmt_str += "WHERE profs.profid = ?"

					cursor.execute(stmt_str, [courseprofs_row[0]])

					row = cursor.fetchone()
					prof_list.append(row[0])
				exit(0)
				
	except Exception as ex:
		print(ex, file=stderr)
		exit(1)


#-----------------------------------------------------------------------	

if __name__ == '__main__':
	main()