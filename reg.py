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
	parser.add_argument('-d', type=str, nargs='?', metavar='dept'
		dest='dept', action='store', default='', 
		help='show only those classes whose department contains dept')

	parser.add_argument('-n', type=str, nargs='?', metavar='num'
		dest='num', action='store', default='', 
		help='show only those classes whose course number contains num')

	parser.add_argument('-a', type=str, nargs='?', metavar='area'
		dest='area', action='store', default='', 
		help='show only those classes whose distrib area contains area')

	titleHelperStr = 'show only those classes whose course title '
	titleHelperStr +='contains title'

	parser.add_argument('-t', type=str, nargs='?', metavar='title'
		dest='title', action='store', default='', 
		help=titleHelperStr)

	args = parser.parse_args()

	if (args.dept != ''):
		print('department: ' + args.dept)
	if (args.num != ''):
		print('num: ' + args.num[0])
	if (args.area != ''):
		print('area' + args.area)
	if (args.title != ''):
		print('title' + args.title)


#-----------------------------------------------------------------------

if __name__ == '__main__':
	main()