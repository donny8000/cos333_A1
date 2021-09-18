#!/usr/bin/env python

#-----------------------------------------------------------------------
# reg_wildcard.py
# Authors: Donovan Pearce and Annette Lee
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------

def wildcard(argument):
	replacement = argument.replace("%", "\\%")
	replacement = replacement.replace("_", "\\_")
	return replacement

def main():
	str1 = "Hello%World"
	print(str1)
	print(wildcard(str1))

	str2 = "Goodbye_World"
	print(str2)
	print(wildcard(str2))

if __name__ == '__main__':
	main()
