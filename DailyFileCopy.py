##Arthur A. Burkey III
##Python Drill: PyDrill_scripting_27_idle
##Title: Daily File Transfer scripting project - Python 2.7 - IDLE

##Scenario: Your company's users create or edit a collection of text files
##throughout the day. These text files represent data about customer
##orders.

##Once per day, any files that are new, or that were edited within the
##previous 24 hours, must be sent to the home office. To facilitate this,
##these new or updated files need to be copied to a specific 'destination'
##folder on a computer, so that a special file transfer program can grab
##them and transfer them to the home office.

##The process of figuring out which files are new or recently edited, and
##copying them to the 'destination' folder, is currently being done
##manually. This is very expensive in terms of manpower.

##You have been asked to create a script that will automate this task,
##saving the company a lot of money over the long term.

##Guidelines:
##You should create two folders; one to hold the files that get created or
##modified throughout the day, and another to receive the folders that your
##script determines should be copied over daily.

##To aid in your development efforts, you should create .txt files to add
##to the first folder, using Notepad or similar program. You should also
##copy some older text files in there if you like.

##You should use files
##that you can edit, so that you can control whether they are meant to be
##detected as 'modified in the last 24 hours' by your program.
import datetime
import shutil 
import os, sys 
import os.path, time

src = "C:/Users/Student/Desktop/Python/" 
dst = "C:/Users/Student/Desktop/Python/copyOver/" 
prntSrc = os.listdir(src) 
prntDst = os.listdir(dst) 

timestamp = (time.time())
vorTimestamp = timestamp - 86400
print timestamp

print 'BEFORE copy operation in Source Dir: ' 
print(prntSrc)
##print ''
##print 'AFTER copy operations in Destination Dir: '
##print(prntDst) 

def modification_date():
    for x in prntSrc:
        filetime = os.path.getmtime(src + x)
        if filetime > vorTimestamp:
            print x
            print filetime
            if x.endswith(".txt"):
                shutil.copy(x, dst)
                print ''
                print 'AFTER copy operations in Destination Dir: '
                print(prntDst) 
modification_date()








