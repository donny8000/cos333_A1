#!/usr/bin/env python

#-----------------------------------------------------------------------
# testreg_details.py
# Authors: Donovan Pearce and Annette Lee
#-----------------------------------------------------------------------

from sys import argv
import os

#-----------------------------------------------------------------------

def execute_command(args):
	os.system('python ' + argv[1] + ' ' + args)


#-----------------------------------------------------------------------

def main():
	execute_command('8321')
	execute_command('8597')
	execute_command('9032')
	execute_command('9977')
	execute_command('10188')
	execute_command('9012')

#-----------------------------------------------------------------------

if __name__ == '__main__':
	main()