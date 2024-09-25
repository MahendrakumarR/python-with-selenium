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
print("====== read =====")
f = open("F:\\PROJECTS\\PYTHON WITH SELENIUM\\read.txt", "r")
print(f.readable())                                            # True
print(f.writable())                                            # False
print(f.closed)                                                # False
f.close()
print(f.closed)                                                # True

"""

QUESTION 1.2:
-------------
Description :Create a File  in "D:\\File Operations\\write.txt with "w" mode and close file
             a.Check whether file is readable or not?
             b.Check whether file is writable or not?
             c.Check whether file is closed or not?

"""
print("====== write =====")
f = open("F:\\PROJECTS\\PYTHON WITH SELENIUM\\read.txt", "w")
print(f.readable())                                            # False
print(f.writable())                                            # True
print(f.closed)                                                # False
f.close()
print(f.closed)                                                # True

"""
QUESTION 1.3:
-------------
Description :Create a File  in "E:\\File\\append.txt with "a" mode and close file
             a.Check whether file is readable or not?
             b.Check whether file is writable or not?
             c.Check whether file is closed or not?

"""
print("====== append =====")
f = open("F:\\PROJECTS\\PYTHON WITH SELENIUM\\read.txt", "a")
print(f.readable())                                            # False
print(f.writable())                                            # True
print(f.closed)                                                # False
f.close()
print(f.closed)                                                # True

"""
QUESTION 2:
-----------
QUESTION 2.1:
-------------
Description :Create a File  in "E:\\Python Notes\\read.txt with "W" mode and follow below steps
             Step 1: Write "Welcome to Greens Technology Java Class . Java is simple language ." in that file
             Step 2: Close the file

"""
f = open("F:\\PROJECTS\\PYTHON WITH SELENIUM\\read.txt", "w")
f.write("Welcome to Greens Technology Java Class . Java is simple language .")
f.close()

"""
QUESTION 2.2:
-------------
Description :Create a File  in "E:\\Python Notes\\read.txt with "a" mode and follow below steps
             Step 1: Write "Welcome to Greens Technology Java Class . Java is simple language ." in that file
             Step 2: Replace word java as Python 
             Step 2: Close the file

"""