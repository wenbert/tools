"""
Usage:
$ python trimdash.py sourcedirectory targetdirectory
"""
import os, sys, datetime, calendar
from sys import argv
from time import gmtime, strftime

script, input_dir = argv

try:
    input_dir = os.path.abspath(input_dir)
    output_dir = "converted_%s" % strftime("%Y%m%d_%H_%M_%S", gmtime())
    print input_dir
    
    
    contents = os.listdir(str(input_dir)) 
    
    #os.mkdir("%s/%s", os.path.join(input_dir, "converted"))
    os.mkdir(output_dir)
    print os.path.abspath(output_dir)
    
    count = 1
    for i in contents:
        #filename = i
        #i = os.path.join(input_dir,i)
        
        
        #MAKE SURE TO CHECK THAT THE FILE IS XYZ!
        
        output_dir = os.path.join(os.path.abspath(output_dir))
        
        new_file = open(os.path.join(output_dir,i), 'w')
        new_file.truncate()
        
        print "opening file: ", i,
        
        file_extension = i.split(".")[-1]
        
        if file_extension == "xyz":
            for line in open(os.path.join(input_dir,i), 'r'):
                line = line.replace("-", "")
                new_file.write(line)
        else:
            print "%s is not an XYZ file! skipping... " % i
        print " closing..."
        
        new_file.close()
        
        count += 1
    print "processed. converted contents of: %s to %s" \
          % (input_dir, os.path.abspath(output_dir))
          
except:
    print "Unexpected error",  sys.exc_info()

raw_input("Press enter to exit")