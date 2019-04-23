# -*- coding: cp1252 -*-
#Assessment #3 – (String Maniulation, Sorting)
def AlphabetSoup(str):
	f = ''.join(sorted(str))
	return f
str = raw_input("Input:")
print AlphabetSoup(str)
