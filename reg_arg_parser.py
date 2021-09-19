#!/usr/bin/env python

#-----------------------------------------------------------------------
# reg_arg_parser.py
# Authors: Donovan Pearce and Annette Lee
#-----------------------------------------------------------------------

import argparse

#-----------------------------------------------------------------------

def parse_args():

	parser = argparse.ArgumentParser(allow_abbrev=False, description=
		"Registrar application: show overviews of classes")

	parser.add_argument('-d', type=str, metavar='dept',
		dest='dept', action='store', default='',
		help='show only those classes whose department contains dept')

	parser.add_argument('-n', type=str, metavar='num',
		dest='num', action='store', default='',
		help='show only those classes whose course number contains num')

	parser.add_argument('-a', type=str, metavar='area',
		dest='area', action='store', default='',
		help='show only those classes whose distrib area contains area')

	title_helper_str = 'show only those classes whose course title '
	title_helper_str +='contains title'

	parser.add_argument('-t', type=str, metavar='title',
		dest='title', action='store', default='',
		help=title_helper_str)

	args = parser.parse_args()

	return args