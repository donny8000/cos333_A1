#!/usr/bin/env python

#-----------------------------------------------------------------------
# reg_table.py
# Authors: Donovan Pearce and Annette Lee
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------

def sort_rows(row_list):
	result = sorted(row_list, key=itemgetter(0))
	result = sorted(result, key=itemgetter(2))
	result = sorted(result, key=itemgetter(1))
	return result