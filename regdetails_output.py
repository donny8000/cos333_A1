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

def print_output(class_row, course_row, crosslistings_list, prof_list):
    crosslistings_list = sort_crosslisting_rows(crosslistings_list)
    prof_list = sorted(prof_list)

    result = wrap("Course Id: %s" %class_row[0])
    result += "\n\n"

    result += wrap("Days: %s" %class_row[1])
    result += "\n"
    result += wrap("Start time: %s" %class_row[2])
    result += "\n"
    result += wrap("End time: %s" %class_row[3])
    result += "\n"
    result += wrap("Building: %s" %class_row[4])
    result += "\n"
    result += wrap("Room: %s" %class_row[5])

    result += "\n\n"

    for crosslisting_row in crosslistings_list:
        result += wrap("Dept and Number: %s %s"
            %(crosslisting_row[0], crosslisting_row[1]))
        result += "\n"

    result += "\n"

    area_val = course_row[0]
    if area_val == '':
        result += "Area: "
    else:
        result += wrap("Area: %s" %area_val)

    result += "\n\n"

    result += wrap("Title: %s" %course_row[1])

    result += "\n\n"

    result += wrap("Description: %s" %course_row[2])

    result += "\n\n"

    result += wrap("Prerequisites: %s" %course_row[3])

    result += "\n"

    for prof in prof_list:
        result += "\n"
        result += wrap("Professor: %s" %prof)

    print(result)
