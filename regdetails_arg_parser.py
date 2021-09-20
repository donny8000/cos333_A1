#!/usr/bin/env python

#-----------------------------------------------------------------------
# regdetails_arg_parser.py
# Authors: Donovan Pearce and Annette Lee
#-----------------------------------------------------------------------

import argparse

#-----------------------------------------------------------------------

def parse_args():

    parser = argparse.ArgumentParser(description=
		"Registrar application: show details about a class")

    parser.add_argument('classid', type=int, metavar='classid',
		action='store',
        help='show only those classes whose department contains dept')

    args = parser.parse_args()

    return args
