"""
Usage:
$ python freespan.py sourcefile.csv outputfile.csv

More details are found in our wiki (log-in required):
http://wiki.npo-inc.com/index.php/Getting_KP_for_Freespans

Notes:
Script removes double quotes and newlines.
Script replaces all semi-colons with a comma.
"""
import os, sys, datetime, calendar
from sys import argv

script, input_file, output_file = argv

try:        
    #output_file = input_file,"converted.txt"
    new_file = open(output_file, 'w')
    new_file.truncate()
    
    i = 1
    for line in open(input_file, 'r'):
        #print line        
        line = line.replace("\"", "")
        line = line.replace(";", ",")
        line = line.replace("\r\n","")
        pieces = line.split(",")
        kp = pieces[8]
        print kp
        new_file.write("%s " % (kp))
        if(i%2 == 0):
            print "\n"
            new_file.write("\n")
        i += 1
    
    print "done. From KP - To KP generated. always double check!"
    new_file.close()
except:
    print "Unexpected error",  sys.exc_info()

raw_input("Press enter to exit")