#!/usr/bin/env python

#-----------------------------------------------------------------------
# testreg.py
# Authors: Donovan Pearce and Annette Lee
#-----------------------------------------------------------------------

from sys import argv
import os

#-----------------------------------------------------------------------

def execute_command(args):
	os.system('python ' + argv[1] + ' ' + args)


#-----------------------------------------------------------------------

def main():
	# execute_command('a qr')
	# execute_command('-A qr')
	# execute_command('"-a " qr')
	# execute_command('-a qr st')
	# execute_command('-a')
	# execute_command('-a qr -d')
	# execute_command('-a -d cos')
	# execute_command('-x')
	execute_command('')
	execute_command('-d COS')
	execute_command('-n 333')
	execute_command('-n b')
	execute_command('-a Qr')
	execute_command('-t intro')
	execute_command('-t science')
	execute_command('-t C_S')
	execute_command('-t c%S')
	execute_command('-d cos -n 3')
	execute_command('-d cos -a qr -n 2 -t intro')
	execute_command('-t "Independent Study"')
	execute_command('-t "Independent Study "')
	execute_command('-t "Independent Study  "')
	execute_command('-t " Independent Study"')
	execute_command('-t "  Independent Study"')
	execute_command('-t=-c')


#-----------------------------------------------------------------------

if __name__ == '__main__':
	main()