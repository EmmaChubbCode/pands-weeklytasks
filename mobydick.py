#INSTRUCTIONS:
# enter this command in the terminal or in command line: python mobydick.py mobydick.txt


# Assumption:s 
# first assumption is that the file this program will operate on is a txt file.
# I am assuming I should count only lower case e's because im interpreting the instructions as literal and exhaustive.
# this text is in the English language so I'm assuming there are no accented e's, which would be different characters. i will not be searching them to count.
# another assumption made in this code is that the txt file and the program are in the same directory. i checked this in the command line before using (e.g. "dir") 

# instructions say read from the command file so used these resources to adapt code: 
# https://www.geeksforgeeks.org/python-sys-module/ 
# https://stackoverflow.com/questions/7439145/i-want-to-read-in-a-file-from-the-command-line-in-python 

import sys
# the 1 here is the file name. the 0 is the script name. it indicates the first argument passed to the script. 
# so im saying my variable FILENAME is whatever file name i actually pass to the script when i run it.
# see: https://docs.python.org/3/library/sys.html#sys.argv 
FILENAME = sys.argv[1]

# this bit is basically the lecture notes + debugging from online sources. specifying that im reading a text file.
with open (FILENAME, "rt") as f:
   
   # got error: <built-in method read of _io.TextIOWrapper object> first time because i wasnt using brackets here.
   # According to https://wiki.python.org/moin/Asking%20for%20Help/Why%20when%20I%20read%20a%20text%20file%20python%20reads%20it%20as%20%22%3Cbuilt-in%20method%20read%20of%20_io.TextIOWrapper%20object%20at%200x02954558%3E%22%20and%20how%20do%20I%20stop%20this%3F
   # i was printing the read method, i wasnt calling the read method. 
    data = f.read()

    # for counting e, i took very simple approach of treating the file components as one big string and copied what i found here: https://www.w3schools.com/python/ref_string_count.asp
    e = data.count("e")
    # now return the count of e's
    print(e)

