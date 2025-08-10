#!/usr/bin/env python
#Sequence Types Examples (Tuples, Strings and Lists)
#Tuple Type
tTuple = (16, 'Rohtash', 1, (2 , 5), 20, "Lakra")
print tTuple
print "First item in Tuple:"
print tTuple[0]
print "Second from right in tTuple"
print tTuple[-2]
print "Slicing:[1:4]"
print tTuple[1:4]
print

#List Type
tList = ["Rohtash", "Singh", "Lakra", 'RS', 34, "Great!"]
print tList
print "Fourth item in list:"
print tList[3]
print "Slicing:[3:-1]"
print tList[3:-1]
print

#String Type
tString = "Rohtash Lakra"
tString1 = "Lakra's Office"
tString2 = """Rohtash Lakra's Office 
Near 101"""
print tString
print "Ninth letter in " + tString + ":" + tString[8]
print tString1
print tString2
