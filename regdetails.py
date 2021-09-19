#!/usr/bin/env python

#-----------------------------------------------------------------------
# regdetails.py
# Authors: Donovan Pearce and Annette Lee
#-----------------------------------------------------------------------

from regdetails_arg_parser import parse_args

def main():
	args = parse_args
	print (args.classid)

#-----------------------------------------------------------------------	

if __name__ == '__main__':
	main()