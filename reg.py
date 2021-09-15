#!/usr/bin/env python

#-----------------------------------------------------------------------
# reg.py
# Authors: Donovan Pearce and Annette Lee
#-----------------------------------------------------------------------

import argparse

#-----------------------------------------------------------------------

def main():

	parser = argparse.ArgumentParser(description=
		"Registrar application: show overviews of classes")
	parser.add_argument('-d', '-dept', type=str, nargs='?', 
		dest='dept', action='store', default='', 
		help='show only those classes whose department contains dept')

	parser.add_argument('-n', '-num', type=str, nargs='?', 
		dest='num', action='store', default='', 
		help='show only those classes whose course number contains num')

	parser.add_argument('-a', '-area', type=str, nargs='?', 
		dest='area', action='store', default='', 
		help='show only those classes whose distrib area contains area')

	titleHelperStr = 'show only those classes whose course title '
	titleHelperStr +='contains title'

	parser.add_argument('-t', '-title', type=str, nargs='?', 
		dest='title', action='store', default='', 
		help=titleHelperStr)

	args = parser.parse_args()

	# if (dept != ''):
	# 	print('title: ' + dept)
	# if (num != ''):
	# 	print('num: ' + num)
	# if (area != ''):
	# 	print('area' + area)
	# if (title != ''):
	# 	print('title' + title)


#-----------------------------------------------------------------------

if __name__ == '__main__':
	main()