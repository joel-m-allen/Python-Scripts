#script to test the arguments parser, the system call, and the
# "cycle through a file
       
#arg parser
from optparse import OptionParser
#system call
from subprocess import call
# call didn't work, let's try os
import os

parser = OptionParser()

parser.add_option("-f","--file",dest="filename",help="file to open")

options, arguments = parser.parse_args()

if options.filename:
    print(options.filename)
    #call(["dir","shell=True"])
    os.system("dir")

    #open the specified file
    f = open(options.filename, 'r')
    print ("contents of {}:".format(options.filename))
    for line in f:
        print line,
        
