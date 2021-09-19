#!/usr/bin/env python

#-----------------------------------------------------------------------
# regdetails_table.py
# Authors: Donovan Pearce and Annette Lee
#-----------------------------------------------------------------------

from operator import itemgetter
import textwrap

#-----------------------------------------------------------------------

def sort_crosslisting_rows(row_list):
	result = sorted(row_list, key=itemgetter(1))
	result = sorted(result, key=itemgetter(0))
	return result

def wrap(text):
	return textwrap.fill(text, width=72)

def print_table(class_row, course_row, crosslistings_list, prof_list): 
	crosslistings_list = sort_crosslisting_rows(crosslistings_list)
	prof_list = sorted(prof_list)

	print(format("Course Id:", str(class_row[0])))

	# result += "\n"

	# result += wrap(format("Days:", class_row[1]))
	# result += wrap(format("Start Time:", class_row[2]))
	# result += wrap(format("End Time:", class_row[3]))
	# result += wrap(format("Building:", class_row[4]))
	# result += wrap(format("Room:", class_row[5]))

	# result += "\n"

	# for crosslisting_row in crosslistings_list:
	# 	result += wrap(format("Dept and Number: %s %s" 
	# 		%(crosslisting_row[0], crosslisting_row[1])))

	# result += "\n"

	# result += wrap(format("Area:", course_row[0]))

	# result += "\n"

	# result += wrap(format("Title:", course_row[1]))

	# result += "\n"

	# result += wrap(format("Description:", course_row[2]))

	# result += "\n"

	# result += wrap(format("Prerequisites:", course_row[3]))

	# result += "\n"

	# for prof in prof_list:
	# 	result += wrap(format("Professor:", prof))
	# print(result)
