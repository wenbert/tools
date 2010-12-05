"""
Usage:
$ python trimdash.py sourcedirectory

Creates a "nodash_XXX" directory containing the XYZ with no dashes.
XXX is a timestamp formated: YYYYMMDDHHMMSS 
Example: nodash_20101205141004
"""
import os, sys, datetime, calendar
from sys import argv
from time import gmtime, strftime

script, input_dir = argv

try:
    input_dir = os.path.abspath(input_dir)
    output_dir = "nodash_%s" % strftime("%Y%m%d_%H_%M_%S", gmtime())
    print "Opening directory: %s" % input_dir
    
    contents = os.listdir(str(input_dir)) 
    total_files = len(contents)
    
    os.mkdir(output_dir)
    print "Output directory: %s" % os.path.abspath(output_dir)
    
    count = 1
    
    for i in contents:
        output_dir = os.path.join(os.path.abspath(output_dir))
        
        new_file = open(os.path.join(output_dir,i), 'w')
        new_file.truncate()
        
        print "Processing file (%s of %s): %s"% (count, total_files, i),
        
        file_extension = i.split(".")[-1]
        
        if file_extension == "xyz":
            for line in open(os.path.join(input_dir,i), 'r'):
                line = line.replace("-", "")
                new_file.write(line)
        else:
            print "[not an XYZ file! skipping]",
        print " closing."
        
        new_file.close()
        
        count += 1
    print "Done. Output files created in %s" \
          % (os.path.abspath(output_dir))
          
except:
    print "Unexpected error",  sys.exc_info()

raw_input("Press enter to exit")