"""
Usage:
$ python reverse_file.py folder_to_reverse
Will create a new folder named "reversed_N", where N is a timestamp
"""

import os, sys, datetime, calendar, re, itertools
from sys import argv
from time import gmtime, strftime

script, input_dir = argv

def filerev(somefile, buffer=0x20000):
    """
    http://stackoverflow.com/questions/2301789/read-a-file-in-reverse-order-using-python/2301867#2301867
    """
    somefile.seek(0, os.SEEK_END)
    size = somefile.tell()
    lines = ['']
    rem = size % buffer
    pos = max(0, (size // buffer - 1) * buffer)
    while pos >= 0:
        somefile.seek(pos, os.SEEK_SET)
        data = somefile.read(rem + buffer) + lines[0]
        rem = 0
        lines = re.findall('[^\n]*\n?', data)
        ix = len(lines) - 2
        while ix > 0:
            yield lines[ix]
            ix -= 1
        pos -= buffer
    else:
        yield lines[0]

try:
    input_dir = os.path.abspath(input_dir)
    output_dir = "reversed_%s" % strftime("%Y%m%d_%H_%M_%S", gmtime())
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
        
        #read only the lpa files
        if file_extension == "lpa":
            with open(os.path.join(input_dir,i), 'r') as f:
                for line_a in filerev(f):
                    new_file.write(line_a)
                
        else:
            print "[not a lpa file! skipping]",
        print " closing."
        
        new_file.close()
        
        count += 1
    print "Done. Output files created in %s" \
          % (os.path.abspath(output_dir))
          
except:
    print "Unexpected error",  sys.exc_info()

raw_input("Press enter to exit")

        