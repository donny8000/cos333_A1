#!/usr/bin/env python

#-----------------------------------------------------------------------
# testreg.py
# Authors: Donovan Pearce and Annette Lee
#-----------------------------------------------------------------------

import reg.py as reg

#-----------------------------------------------------------------------

def execute_command(args):
	os.system('python ' + args)


#-----------------------------------------------------------------------

def main():
	execute_command('a qr')
	execute_command('-A qr')
	execute_command('"-a " qr')
	execute_command('-a qr st')
	execute_command('-a')
	execute_command('-a qr -d')
	execute_command('-a -d cos')
	execute_command('-x')

#-----------------------------------------------------------------------

if __name__ == '__main__':
	main()