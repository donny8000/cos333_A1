#!/usr/bin/env python

#-----------------------------------------------------------------------
# meta_testreg.py
# Authors: Donovan Pearce and Annette Lee
#-----------------------------------------------------------------------

import os
import testreg

#-----------------------------------------------------------------------


#-----------------------------------------------------------------------

def main():
	os.system('python testreg.py reg.py > out1 2>&1')
	os.system('python testreg.py /../u/cos333/Asgt1Solution/ref_reg.pyc > out2 2>&1')
	os.system('diff out1 out2')

#-----------------------------------------------------------------------

if __name__ == '__main__':
	main()