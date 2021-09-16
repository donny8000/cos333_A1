#!/usr/bin/env python

#-----------------------------------------------------------------------
# reg.py
# Authors: Donovan Pearce and Annette Lee
#-----------------------------------------------------------------------

from reg_arg_parser import parse_args

#-----------------------------------------------------------------------

def main():
	parse_args()

	if (args.dept != ''):
		print('department: ' + args.dept)
	if (args.num != ''):
		print('num: ' + args.num[0])
	if (args.area != ''):
		print('area: ' + args.area[0])
	if (args.title != ''):
		print('title: ' + args.title[0])


#-----------------------------------------------------------------------

if __name__ == '__main__':
	main()