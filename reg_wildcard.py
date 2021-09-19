#!/usr/bin/env python

#-----------------------------------------------------------------------
# reg_wildcard.py
# Authors: Donovan Pearce and Annette Lee
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------

def wildcard(goal):
    replace = goal.replace("%", "\\%")
    replace = replace.replace("_", "\\_")
    return '%' + replace + '%'
