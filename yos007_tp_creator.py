"""
Filename: yos007_tp_creator.py

Usage:
$ python yos007_tp_creator.py sourcefile.csv outputfile.csv

Input file must be:
Easting, Northing, Bearing

Use Cases:
The sourcefile.csv has points for every 2 meters. We write a line to the file
(outputfile.csv) for every bearing change. We will end up with fewer lines 
instead of having points for every 2 meters.

*Do not forget to remove the header!

"""
import os, sys
from sys import argv
import linecache

script, input_file, output_file = argv

try:
    new_file = open(output_file, 'w')
    new_file.truncate()
    previous_bearing = ""
    previous_easting = ""
    previous_northing = ""
    bearing = "0"
    northing = ""
    easting = ""
    
    first_line = ""
    for line in open(input_file, 'r'):
        #print line        
        line = line.replace("\"", "")
        line = line.replace(";", ",")
        line = line.replace("\r\n","")
        pieces = line.split(",")
        
        previous_bearing = bearing
        previous_easting = easting
        previous_northing = northing
        
        easting = pieces[0]
        northing = pieces[1]
        bearing = pieces[2]
        
        #remove the if-condition below when implementing the "tolerance"
        if(float(previous_bearing) != float(bearing)):
            new_file.write("%s,%s,%s\n" % (previous_easting,previous_northing,previous_bearing))
            #pass
                
    print "done."
    new_file.close()
    new_file = open(output_file, 'a')
    new_file.write("%s,%s,%s\n" % (easting,northing,bearing))
    new_file.close()
except:
    print "Unexpected error",  sys.exc_info()

raw_input("Press enter to exit")