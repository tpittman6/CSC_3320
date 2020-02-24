#!/bin/python
import sys
import collections

def findKey():
   infile = open(sys.argv[1])
   text = infile.read()
   num = { }

   for i in text:
      if i in num:
         num[i] += 1
      else:
         num[i] = 1
   print str(num)

if len(sys.argv) > 1:
   findKey()
else: 
   print "Enter text file as an argument"
   
