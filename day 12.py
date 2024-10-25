"""
What is meant by File operation?

    File operations are actions that can be performed on files, such as reading, writing, appending, and closing.

What are the modes available in File Operation?

    Common modes: "r" (read), "w" (write), "a" (append), "x" (create), "r+" (read and write), "w+" (write and read), "a+" (append and read), and binary modes like "rb", "wb".

Is it possible to write in file under "r" mode?

    No, "r" mode is read-only.

Explain the purpose of writable(), readable(), close()?

    writable(): Checks if a file is writable.

    readable(): Checks if a file is readable.
    
    close(): Closes the file and releases system resources.

Write a code for writing multiple lines in a file?

    with open("file.txt", "w") as file:

    lines = ["First line\n", "Second line\n", "Third line\n"]
    
    file.writelines(lines)

What is the difference between readlines() and readline()?

    readlines(): Reads all lines of a file and returns them as a list.
    
    readline(): Reads one line at a time from the file.

What is the purpose of tell() and seek() methods?

    tell(): Returns the current file pointer position.
    
    seek(): Changes the file pointer to a specified position.

Is it possible to read and write parallel?

    Yes, using modes like "r+", "w+", and "a+".

What is the difference between r+ and w+?

    "r+": Opens a file for reading and writing; fails if the file doesn't exist.
    
    "w+": Opens a file for reading and writing; creates the file if it doesn't exist and overwrites existing content.

What is meant by Binary File?
    
    A binary file stores data in binary (0s and 1s) format and is not human-readable.

What are modes used for binary files?
    
    "rb", "wb", "ab", "rb+", "wb+", "ab+".

What is meant by CSV File? In which module is CSV file related?

    CSV (Comma Separated Values) is a file format used for storing tabular data. The csv module in Python handles CSV files.

What are methods used for writing and reading files?

    Writing: write(), writelines()
    
    Reading: read(), readline(), readlines()

What is meant by a Zip File?
    
    A Zip file is a compressed file format used to store multiple files in a reduced size.

What is the difference between os.makedirs() and os.mkdir()?

    os.makedirs(): Creates a directory and all intermediate directories.
    
    os.mkdir(): Creates a single directory.

What are methods available in OS Module?

    os.remove(): Deletes a file.
    
    os.rename(): Renames a file.
    
    os.getcwd(): Gets the current working directory.
    
    os.chdir(): Changes the current working directory.
    
    os.listdir(): Lists files in a directory.
    
    os.path.exists(): Checks if a file or directory exists.

"""

"""
QUESTIONS[practical]:
-------------------------
QUESTION 1:
-----------
QUESTION 1.1:
-------------
Description :Create a File  in "D:\\File Operations\\read.txt with "r" mode and close file
             a.Check whether file is readable or not?
             b.Check whether file is writable or not?
             c.Check whether file is closed or not?

"""
"""
print("====== read =====")
f = open("F:\\PROJECTS\\PYTHON WITH SELENIUM\\read.txt", "r")
print(f.readable())                                            # True
print(f.writable())                                            # False
print(f.closed)                                                # False
f.close()
print(f.closed)                                                # True

"""
"""
QUESTION 1.2:
-------------
Description :Create a File  in "D:\\File Operations\\write.txt with "w" mode and close file
             a.Check whether file is readable or not?
             b.Check whether file is writable or not?
             c.Check whether file is closed or not?

"""
"""
print("====== write =====")
f = open("F:\\PROJECTS\\PYTHON WITH SELENIUM\\read.txt", "w")
print(f.readable())                                            # False
print(f.writable())                                            # True
print(f.closed)                                                # False
f.close()
print(f.closed)                                                # True

"""
"""
QUESTION 1.3:
-------------
Description :Create a File  in "E:\\File\\append.txt with "a" mode and close file
             a.Check whether file is readable or not?
             b.Check whether file is writable or not?
             c.Check whether file is closed or not?

"""
"""
print("====== append =====")
f = open("F:\\PROJECTS\\PYTHON WITH SELENIUM\\read.txt", "a")
print(f.readable())                                            # False
print(f.writable())                                            # True
print(f.closed)                                                # False
f.close()
print(f.closed)                                                # True

"""

"""
QUESTION 2:
-----------
QUESTION 2.1:
-------------
Description :Create a File  in "E:\\Python Notes\\read.txt with "W" mode and follow below steps
             Step 1: Write "Welcome to Greens Technology Java Class . Java is simple language ." in that file
             Step 2: Close the file

"""
"""
print("===== Create file =====")
f = open("F:\\PROJECTS\\PYTHON WITH SELENIUM\\read.txt", "w")
f.write("Welcome to Greens Technology Java Class . Java is simple language .")
f.close()

"""
"""
QUESTION 2.2:
-------------
Description :Create a File  in "E:\\Python Notes\\read.txt with "a" mode and follow below steps
             Step 1: Write "Welcome to Greens Technology Java Class . Java is simple language ." in that file
             Step 2: Replace word java as Python 
             Step 2: Close the file

"""
"""
print("===== Replace Word =====")
f = open("F:\\PROJECTS\\PYTHON WITH SELENIUM\\read.txt", "a")
text ="\nWelcome to Greens Technology Java Class . Java is simple language ."
c = text.replace("Java","python")
f.write(c + "\n")
f.close()

"""
"""
QUESTION 3:
-----------
QUESTION 3.1:
-------------
Description :Create a File  in "E:\\Python Notes\\read.txt with "w" mode and follow below steps
             Step 1: Write the below content in line by line
                     Java Class
                     Python Class
                     Selenium Class
                     Mobile Testing Class
"""
"""
print("===== Write line by line =====")
f = open("F:\\PROJECTS\\PYTHON WITH SELENIUM\\read.txt", "w")
f.write("Java Class")
f.write("\nPython Class")
f.write("\nSelenium Class")
f.write("\nMobile Testing Class\n")
f.close()

"""
"""
QUESTION 3.2:
-------------
Description :Create a File  in "E:\\Python Notes\\read.txt with "a" mode and follow below steps
             Step 1: Add the below content in line by line
                     Api Testing
                     Postman Tool
                     Appium 
"""
"""
print("===== Write line by line =====")
f = open("F:\\PROJECTS\\PYTHON WITH SELENIUM\\read.txt", "a")
f.write("\nApi Testing")
f.write("\nPostman Tool")
f.write("\nAppium")
f.close()

"""
"""
QUESTION 3.3:
-------------
Description :Create a File  in "E:\\Python Notes\\read.txt with "w" mode and follow below steps
             Step 1: Add the below Employee details as array of file
                     [100,vel,vel@gmail.com]
                     [200,Nisha,Nisha@gmail.com]
                     [300,Bala,Bala@gmail.com]
                     [400,Ganesh,Ganesh@gmail.com]

"""
"""
print("===== Array of file =====")
f = open("F:\\PROJECTS\\PYTHON WITH SELENIUM\\read.txt", "w")
employee = [
            [100,"vel","vel@gmail.com"],
            [200,"Nisha","Nisha@gmail.com"],
            [300,"Bala","Bala@gmail.com"],
            [400,"Ganesh","Ganesh@gmail.com"]
]

for emp in employee:
    f.write(str(emp) + '\n')
f.close()

"""
"""
QUESTION 4:
-----------
QUESTION 4.1:
-------------
Description :Write a file below content
             Velmurugan currently focuses on teaching and delivering placement support for all his students, 
             During this training journey, He has taken 400+ batches through different modes (Online, classroom, corporate). 
             Worked with major IT companies such as Verizon, Infosys, Bank of America, as well as several smaller private companies in delivering high-quality training.
             Through his innovative ideas, Velmurugan has also suggested many customer value adds to different private companies which helped in saving lot of efforts for different customers.

"""


# print("===== Write a content =====")
# f = open("F:\\PROJECTS\\PYTHON WITH SELENIUM\\read.txt", "w")
# f.write("""Velmurugan currently focuses on teaching and delivering placement support for all his students, 
#            During this training journey, He has taken 400+ batches through different modes (Online, classroom, corporate). 
#            Worked with major IT companies such as Verizon, Infosys, Bank of America, as well as several smaller private companies in delivering high-quality training.
#            Through his innovative ideas, Velmurugan has also suggested many customer value adds to different private companies which helped in saving lot of efforts for different customers.""")
# f.close()

"""

QUESTION 4.2:
-------------
Description :Read all content in file  uing read() method

"""
# print("===== Read all content =====")
# f = open("F:\\PROJECTS\\PYTHON WITH SELENIUM\\read.txt", "r")
# f.read()
# f.close()

"""
QUESTION 4.3:
-------------
Description :Read all content in file after 100th index 

"""
"""
print("===== Read all content after 100th index (seek) =====")
f = open("F:\\PROJECTS\\PYTHON WITH SELENIUM\\read.txt", "r")
f.seek(100)
v = f.read()
print(v)
f.close()

"""
"""
QUESTION 4.4:
-------------
Description :Read all content in file using readlines() method

"""
"""
print("===== Read all content in file using readlines() =====")
f = open("F:\\PROJECTS\\PYTHON WITH SELENIUM\\read.txt", "r")
c = f.readlines()
print(c)
f.close()
"""
"""
QUESTION 5:
-----------
QUESTION 5.1:
-------------
Description :Copy Jpeg image from Local Disk F to Local Disk D

"""
"""
print("===== copy Jpeg image from Local Disk F to Local Disk D =====")

source_path = r"F:\travel.JPG"

destination_path = r"D:\travel.JPG"

with open(source_path,"rb") as source_file:
    data = source_file.read()

with open(destination_path,"wb") as destination_file:
    destination_file.write(data)

print("copy Jpeg image from Local Disk F to Local Disk D successfully completed")

"""
"""
QUESTION 5.2:
-------------
Description :Copy one video Local Disk F to Local Disk D

"""
"""
print("===== copy video from Local Disk F to Local Disk D =====")

video_source_path = r"F:\modelform.mp4"

video_destination_path = r"D:\modelform.mp4"

with open(video_source_path,"rb") as video_source_file:
    data_video = video_source_file.read()

with open(video_destination_path,"wb") as video_destination_file:
    video_destination_file.write(data_video)

print("copy video from Local Disk F to Local Disk D successfully completed")

"""
"""
QUESTION 6:
-----------
QUESTION 6.1:
-------------
Description :Create a CSV File for 10 Employee Details 

"""
"""
print("===== Create a CSV File for 10 Employee Details =====")

import csv

header = ['id','name','age','position','salary']

employee = [
    [1,'henry',23,'field',20000],
    [2,'jhon',20,'field',20000],
    [3,'virat',35,'manager',30000],
    [4,'kamal',56,'watchman',20000],
    [5,'ajith',45,'field',20000],
    [6,'vijay',34,'field',20000],
    [7,'santhi',43,'hr',34000],
    [8,'rose',54,'reception',18,000],
    [9,'syed',36,'field',20000],
    [10,'nazhir',23,'field',20000]
]

with open('employee_details.csv',mode='w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(employee)

print("csv file created successfully ")


"""
""" 
QUESTION 6.2:
-------------
Description :Read 4 Employee Details from CSV File

"""
"""
import csv

print("===== Read 4 Employee Details from CSV File =====")

try:
    with open('employee_details.csv','r') as e_file:
        emp_r = csv.reader(e_file)
        
        header = next(emp_r)

        count = 0


        for row in emp_r:    
            print(row)
            count += 1
        
            if count == 4:
                break
except FileNotFoundError:
    print("===== FileNotFoundError =====")

"""
"""
QUESTION 7:
-----------
QUESTION 7.1:
-------------
Description :Create a ZIp File with Following text File
             Day1Task
             Day2Task
             Day3Task
"""

"""
print("===== Create a ZIp File with Following text File =====")

import zipfile

file_to_zip = ['task1.txt','task2.txt','task3.txt']

file_name = 'task.zip'

with zipfile.ZipFile(file_name,'w') as zip_:
    for file in file_to_zip:
        zip_.write(file)
        print(f"The{file} is added to {file_name} successfully")
print(f"{file_name} created successfully")

"""

"""
QUESTION 7.2:
-------------
Description :Read a Zip File with Following text File
             Day1Task
             Day2Task
             Day3Task
"""
"""
print("===== Read a Zip File with Following text File =====")

import zipfile

file_path = r'F:\PROJECTS\PYTHON WITH SELENIUM\task.zip'

with zipfile.ZipFile(file_path,mode='r') as zip_f :
    file_list = zip_f.namelist()
    print('files archieved in zip names are:',file_list)

    for file_name in ['task1.txt','task2.txt','task3.txt']:
        if file_name in file_list:
            with zip_f.open(file_name) as file :
                content = file.read().decode('utf-8')
                print(f'\ncontent of {file_name}:\n')
                print(content)
        else:
            print(f'{file_name} not found in archieved zip') 
    
"""

"""
QUESTION 8:
-----------
QUESTION 8.1:
-------------
Description :Create a folder JavaNotes in Local Disk D using Os Module 
             a.Check whether it is directory or not
             b.Check whether it is file or not  

"""
"""
print("===== Create a folder JavaNotes in Local Disk D using Os Module =====")

import os

folder_path = r'F:\PROJECTS\PYTHON WITH SELENIUM\JavaNotes'

if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print('folder JavaNotes created succeessfully')
else:
    print('folder JavaNotes already exists')

if os.path.isdir(folder_path):
    print('JavaNote is a directory')
else:
    print('JavaNote is not a directory')

if os.path.isfile(folder_path):
    print('JavaNote is a file')
else:
    print('JavaNote is not a file')

"""

"""
QUESTION 8.2:
-------------
Description :Create a folder Inheritance with in  JavaNotes in Local Disk D using Os Module
              a.Check whether it is directory or not
              b.Check whether it is file or not 

"""
print("===== Create a folder Inheritance with in  JavaNotes in Local Disk D using Os Module =====")

import os

parent_folder = r'F:\PROJECTS\PYTHON WITH SELENIUM\JavaNotes'

new_folder = os.path.join(parent_folder,'inheritance')

if not os.path.exists(parent_folder):
    os.makedirs(parent_folder)
    print('parent folder JavaNotes created succeessfully')
else:
    print('parent folder JavaNotes already exists')

if not os.path.exists(new_folder):
    os.makedirs(new_folder)
    print('new folder inheritance created succeessfully')
else:
    print('new folder inheritance already exists')


if os.path.isdir(new_folder):
    print('Inheritance is a directory')
else:
    print('Inheritance is not a directory')

if os.path.isfile(new_folder):
    print('Inheritance is a file')
else:
    print('Inheritance is not a file')