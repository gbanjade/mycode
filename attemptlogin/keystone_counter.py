#!/usr/bin/python3
# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
# open the file for reading
keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r")
# turn the file into a list of lines in memory
keystone_file_lines=keystone_file.readlines()
# loop over the list of lines
    # if this 'fail pattern' appears in the line..

print(keystone_file_lines.count("- - - - -] Authorization failed"))




