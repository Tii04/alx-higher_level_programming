**Task 0**

Write a function that reads a text file (UTF8) and prints it to stdout:

* Prototype: def read_file(filename=""):
* You must use the with statement
* You don’t need to manage file permission or file doesn't exist exceptions.
* You are not allowed to import any module

**Expected Output:**

guillaume@ubuntu:~/0x0B$ cat 0-main.py
#!/usr/bin/python3
read_file = __import__('0-read_file').read_file

read_file("my_file_0.txt")

guillaume@ubuntu:/0x0B$ cat my_file_0.txt
We offer a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!
guillaume@ubuntu:/0x0B$ ./0-main.py
We offer a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!

guillaume@ubuntu:/0x0B$ 

**Task 1**

Write a function that writes a string to a text file (UTF8) and returns the number of characters written:

Prototype: def write_file(filename="", text=""):
* You must use the with statement
* You don’t need to manage file permission exceptions.
* Your function should create the file if doesn’t exist.
* Your function should overwrite the content of the file if it already exists.
* You are not allowed to import any module

**Expected Output:**

guillaume@ubuntu:/0x0B$ cat 1-main.py
#!/usr/bin/python3
write_file = __import__('1-write_file').write_file

nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)

guillaume@ubuntu:/0x0B$ ./1-main.py
29

guillaume@ubuntu:~/0x0B$ cat my_first_file.txt

This School is so cool!

**Task 2**

Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:

* Prototype: def append_write(filename="", text=""):
* If the file doesn’t exist, it should be created
* You must use the with statement
* You don’t need to manage file permission or file doesn't exist exceptions.
* You are not allowed to import any module

**Expected Output:**

guillaume@ubuntu:~/0x0B$ cat 2-main.py
#!/usr/bin/python3
append_write = __import__('2-append_write').append_write

nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
print(nb_characters_added)

guillaume@ubuntu:/0x0B$ cat file_append.txt
cat: file_append.txt: No such file or directory
guillaume@ubuntu:/0x0B$ ./2-main.py
29
guillaume@ubuntu:/0x0B$ cat file_append.txt
This School is so cool!
guillaume@ubuntu:/0x0B$ ./2-main.py
29
guillaume@ubuntu:/0x0B$ cat file_append.txt
This School is so cool!
This School is so cool!

**Task 3**



**Expected Output:**



**Task 4**



**Expected Output:**



**Task 5**



**Expected Output:**



**Task 6**



**Expected Output:**



**Task 7**



**Expected Output:**



**Task 8**



**Expected Output:**



**Task 9**



**Expected Output:**



**Task 10**



**Expected Output:**



**Task 11**



**Expected Output:**



**Task 12**


**Expected Output:**


