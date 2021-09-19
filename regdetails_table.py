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

	result = wrap("Course Id: %s\n" %class_row[0])
	result += "\n"

	result += wrap("Days: %s\n" %class_row[1])
	result += wrap("Start Time: %s\n" %class_row[2])
	result += wrap("End Time: %s\n" %class_row[3])
	result += wrap("Building: %s\n" %class_row[4])
	result += wrap("Room: %s\n" %class_row[5])

	result += "\n"

	for crosslisting_row in crosslistings_list:
		result += wrap("Dept and Number: %s %s\n" 
			%(crosslisting_row[0], crosslisting_row[1]))

	result += "\n"

	result += wrap("Area: %s\n" %course_row[0])

	result += "\n"

	result += wrap("Title: %s\n" %course_row[1])

	result += "\n"

	result += wrap("Description: %s\n" %course_row[2])

	result += "\n"

	result += wrap("Prerequisites: %s\n" %course_row[3])

	result += "\n"

	for prof in prof_list:
		result += wrap("Professor: %s\n" %prof)

	print(result)
