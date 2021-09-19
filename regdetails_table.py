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

	a = format("Course Id:", class_row[0])

	print()

	print("Days:", class_row[1])
	print("Start Time:", class_row[2])
	print("End Time:", class_row[3])
	print("Building:", class_row[4])
	print("Room:", class_row[5])

	print()

	for crosslisting_row in crosslistings_list:
		print("Dept and Number: %s %s" 
			%(crosslisting_row[0], crosslisting_row[1]))

	print()

	print("Area:", course_row[0])

	print()

	print("Title:", course_row[1])

	print()

	print("Description:", course_row[2])

	print()

	print("Prerequisites:", course_row[3])

	print()

	for prof in prof_list:
		print("Professor:", prof)
