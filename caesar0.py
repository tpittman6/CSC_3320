#!/bin/python
import sys

def encrypt():

   infile = open(sys.argv[1])
   text = infile.read()
   key = int(sys.argv[2])
   outfile = open(sys.argv[3], 'w')
   cipher = ""
   
   if key > 26 or key  < 1:
      print "Please enter a key between 1 and 26"
   else:    
 
      for i in range(len(text)):
         char = text[i] 
    
         if char == " ":
            cipher += " "

         elif (char.isupper()): 
            cipher += chr((ord(char) + key - 65) % 26 + 65) 
  
         else: 
            cipher += chr((ord(char) + key - 97) % 26 + 97) 

      outfile.write(cipher)

if len(sys.argv) > 1:
   encrypt()
else:
   print ""
   print "To use this program from the command line, enter arguments: plaintext file, key, file to be written to."
   print ""
   print "Example: $ ./caesar0.py message1.txt 16 outputfile.txt"
   print ""
