#!/usr/bin/env python

#-----------------------------------------------------------------------
# meta_testregdetails.py
# Authors: Donovan Pearce and Annette Lee
#-----------------------------------------------------------------------

import os
import testreg

#-----------------------------------------------------------------------


#-----------------------------------------------------------------------

def main():
	os.system('python testreg_details.py regdetails.py > out1 2>&1')
	os.system('python testreg_details.py /../u/cos333/Asgt1Solution/ref_regdetails.pyc > out2 2>&1')
	os.system('diff -y out1 out2')

#-----------------------------------------------------------------------

if __name__ == '__main__':
	main()