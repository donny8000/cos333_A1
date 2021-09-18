#!/usr/bin/env python

#-----------------------------------------------------------------------
# reg_table.py
# Authors: Donovan Pearce and Annette Lee
#-----------------------------------------------------------------------

from operator import itemgetter
import textwrap

#-----------------------------------------------------------------------

def sort_rows(row_list):
	result = sorted(row_list, key=itemgetter(0))
	result = sorted(result, key=itemgetter(2))
	result = sorted(result, key=itemgetter(1))
	return result

def print_table(row_list): 
	row_list = sort_rows(row_list)

	print("ClsId Dept CrsNum Area Title")
	print("----- ---- ------ ---- -----")

	for row in row_list:
		row_string = '{:>5} {:>4} {:>6} {:>4} {:}'.format(*row)
		print(textwrap.fill(row_string, width=72, tabsize=29,
			subsequent_index="\t"))