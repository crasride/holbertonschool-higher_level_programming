<h1 align="center">Python - Hello World</h1>

[Python programming](https://github.com/guillaume/holbertonschool-higher_level_programming/blob/main/0x00-python-hello_world/MoreInfo.md)

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/231/48a9fdbd67c84a328a9df9ec8d93b9ac2458ac37721d7d53e51a27fb2bdc5263.jpg)
<h1 align="center">Author’s disclaimer</h1>

```
Welcome to the Python world!

The first projects are more "C-oriented" - no tricks, no funky syntax - simple!
If you've already played with Python, don't worry, fun things will come.
You'll soon find that with Python (and the majority of higher level languages), there are ten different ways to do the same thing. Some tasks will expect only one implementation, while other tasks will have multiple possible implementations.
Like C, Python also has a linter / style guide like Betty, called PEP8, also now known as PyCode. At Holberton, we won't start off with using PyCode, because it's much more strict compared to PEP8. Don't worry if you see a warning when you are running PEP8, you can ignore it.

Enjoy!

- Guillaume


```
## Resources


- [The Python tutorial](https://docs.python.org/3/tutorial/index.html) (only the first three chapters below)
- [Whetting Your Appetite](https://docs.python.org/3/tutorial/appetite.html)
- [Using the Python Interpreter](https://docs.python.org/3/tutorial/interpreter.html)
- [An Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html) (Read up until “3.1.2. Strings” included)
- [How To Use String Formatters in Python 3](https://realpython.com/python-f-strings/)
- [Learn to Program](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
- [Pycodestyle – Style Guide for Python Code](https://pypi.org/project/pycodestyle/)

## General

- Why Python programming is awesome
- Who created Python
- Who is Guido van Rossum
- Where does the name ‘Python’ come from
- What is the Zen of Python
- How to use the Python interpreter
- How to print text and variables using `print`
- How to use strings
- What are indexing and slicing in Python
- What is the official Python coding style and how to check your code with `pycodestyle`

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the repo, containing a description of the repository
- A `README.md` file, at the root of the folder of this project, is mandatory
- Your code should use the pycodestyle (version `2.8.*`)
A- ll your files must be executable
- The length of your files will be tested using `wc`

## Shell Scripts

- Allowed editors: `vi`, `vim`, `emacs`
- All your scripts will be tested on Ubuntu 20.04 LTS
- All your scripts should be exactly two lines long (`wc -l file` should print 2)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/bin/bash`
- All your files must be executable

## C Scripts

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be compiled on Ubuntu 20.04 LTS using gcc, using the options -Wall -Werror -Wextra -pedantic -std=gnu89
- All your files should end with a new line
- Your code should use the `Betty` style. It will be checked using [`betty-style.pl`](https://github.com/holbertonschool/Betty/blob/master/betty-style.pl) and [`betty-doc.pl`](https://github.com/holbertonschool/Betty/blob/master/betty-doc.pl)
- You are not allowed to use global variables
- No more than 5 functions per file
- In the following examples, the `main.c` files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own `main.c` files at compilation. Our `main.c` files might be different from the one shown in the examples
- The prototypes of all your functions should be included in your header file called `lists.h`
- Don’t forget to push your header file
- All your header files should be include guarded.

## Zen

```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

Pycodestyle

`Pycodestyle` is now the [`new standard of Python style code`](https://github.com/PyCQA/pycodestyle/issues/466)

![Flyingcircus](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/231/Flyingcircus_2.jpg)

## Tasks

## [0. Run Python file](./0-run)
mandatory
Score: 100.00% (Checks completed: 100.00%)

Write a Shell script that runs a Python script.

The Python file name will be saved in the environment variable $PYFILE

```
guillaume@ubuntu:~/py/$ cat main.py 
#!/usr/bin/python3
print("Best School")

guillaume@ubuntu:~/py/$ export PYFILE=main.py
guillaume@ubuntu:~/py/$ ./0-run
Best School
guillaume@ubuntu:~/py/$ 
```
### Repo:

    GitHub repository: holbertonschool-higher_level_programming
    Directory: python-hello_world
    File: 0-run

## 1. Run inline 

Write a Shell script that runs Python code.

The Python code will be saved in the environment variable $PYCODE

```
guillaume@ubuntu:~/py/$ export PYCODE='print(f"Best School: {88+10}")'
guillaume@ubuntu:~/py/$ ./1-run_inline 
Best School: 98
guillaume@ubuntu:~/py/$ 
```
### Repo:

    GitHub repository: holbertonschool-higher_level_programming
    Directory: python-hello_world
    File: 1-run_inline

## 2. Hello, print

Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.

Use the function print

```
guillaume@ubuntu:~/py/$ ./2-print.py 
"Programming is like building a multilingual puzzle
guillaume@ubuntu:~/py/$
```
### Repo:

    GitHub repository: holbertonschool-higher_level_programming
    Directory: python-hello_world
    File: 2-print.py

## 3. Print integer

Complete this source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.

You can find the source [code here](https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py)
    
- The output of the script should be:
- The number, followed by Battery street,   
  - followed by a new line
  - You are not allowed to cast the variable number into a string
-Your code must be 3 lines long
-You have to use f-strings tips

```
guillaume@ubuntu:~/py/0x00$ ./3-print_number.py
98 Battery street
guillaume@ubuntu:~/py/0x00$ 

```

### Repo:

    GitHub repository: holbertonschool-higher_level_programming
    Directory: python-hello_world
    File: 3-print_number.py

## 4. Print float

Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.

-    You can find the source code here
-    The output of the program should be:
    -    Float:, followed by the float with only 2 digits
    -    followed by a new line
-    You are not allowed to cast number to string
-    You have to use f-strings

```
guillaume@ubuntu:~/py/0x00$ ./4-print_float.py
Float: 3.14
guillaume@ubuntu:~/py/0x00$ 
```
### Repo:

    GitHub repository: holbertonschool-higher_level_programming
    Directory: python-hello_world
    File: 4-print_float.py


## 5. Print string

Complete this source code in order to print 3 times a string stored in the variable str, followed by its first 9 characters.

-    You can find the source code here
-    The output of the program should be:
     -   3 times the value of str
     -   followed by a new line
     -   followed by the 9 first characters of str
        followed by a new line
-    You are not allowed to use any loops or conditional statement
-    Your program should be maximum 5 lines long

```
guillaume@ubuntu:~/py/$ ./5-print_string.py 
Holberton SchoolHolberton SchoolHolberton School
Holberton
guillaume@ubuntu:~/py/$ 
```

### Repo:

    GitHub repository: holbertonschool-higher_level_programming
    Directory: python-hello_world
    File: 5-print_string.py


## 6. Play with strings

Complete this source code to print Welcome to Holberton School!

-    You can find the source code here
-    You are not allowed to use any loops or conditional statements.
-    You have to use the variables str1 and str2 in your new line of code
-    Your program should be exactly 5 lines long

```
guillaume@ubuntu:~/py/$ ./6-concat.py
Welcome to Holberton School!
guillaume@ubuntu:~/py/$ wc -l 6-concat.py
5 6-concat.py
guillaume@ubuntu:~/py/$ 
```

### Repo:

    GitHub repository: holbertonschool-higher_level_programming
    Directory: python-hello_world
    File: 6-concat.py

## 7. Copy - Cut - Paste

Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/7-edges.py)

-  You can find the source code here
-  You are not allowed to use any loops or conditional statements
-  Your program should be exactly 8 lines long
-  word_first_3 should contain the first 3 letters of the variable word
-  word_last_2 should contain the last 2 letters of the variable word
-  middle_word should contain the value of the variable word without the first and last -    letters

```
guillaume@ubuntu:~/py/$ ./7-edges.py
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
guillaume@ubuntu:~/py/$ wc -l 7-edges.py
8 7-edges.py
guillaume@ubuntu:~/py/$ 
```
### Repo:

    GitHub repository: holbertonschool-higher_level_programming
    Directory: python-hello_world
    File: 7-edges.py


## 8. Create a new sentence


Complete this source code to print object-oriented programming with Python, followed by a new line.

-    You can find the source [code here](https://github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py)
-    You are not allowed to use any loops or conditional statements
-    Your program should be exactly 5 lines long
-    You are not allowed to create new variables
-    You are not allowed to use string literals

```
guillaume@ubuntu:~/py/$ ./8-concat_edges.py
object-oriented programming with Python
guillaume@ubuntu:~/py/$ wc -l 8-concat_edges.py
5 8-concat_edges.py
guillaume@ubuntu:~/py/$ 
```

### Repo:

    GitHub repository: holbertonschool-higher_level_programming
    Directory: python-hello_world
    File: 8-concat_edges.py


## 9. Easter Egg

Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.

Your script should be maximum 98 characters long (please check with wc -m 9-easter_egg.py)

```
guillaume@ubuntu:~/py/$ ./9-easter_egg.py
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
guillaume@ubuntu:~/py/$
```
### Repo:

    GitHub repository: holbertonschool-higher_level_programming
    Directory: python-hello_world
    File: 9-easter_egg.py


## 10. Hello, write 

Write a Python script that prints exactly and that piece of art is useful - Dora Korpar, 2015-10-19, followed by a new line.

-    Use the function write from the sys module
-    You are not allowed to use print
-    Your script should print to stderr
-    Your script should exit with the status code 1


```
guillaume@ubuntu:~/py/$ ./100-write.py
and that piece of art is useful - Dora Korpar, 2015-10-19
guillaume@ubuntu:~/py/$ echo $?
1
guillaume@ubuntu:~/py/$ ./100-write.py 2> q
guillaume@ubuntu:~/py/$ cat q
and that piece of art is useful - Dora Korpar, 2015-10-19
guillaume@ubuntu:~/py/$ 
```
### Repo:

    GitHub repository: holbertonschool-higher_level_programming
    Directory: python-hello_world
    File: 100-write.py

## 11. Compile 

Write a script that compiles a Python script file.

The Python file name will be stored in the environment variable $PYFILE

The output filename has to be $PYFILEc (ex: export PYFILE=my_main.py => output filename: my_main.pyc)

```
guillaume@ubuntu:~/py/$ cat main.py 
#!/usr/bin/python3
print("Best School")

guillaume@ubuntu:~/py/$ export PYFILE=main.py
guillaume@ubuntu:~/py/$ ./101-compile
Compiling main.py ...
guillaume@ubuntu:~/py/$ ls
101-compile  main.py  main.pyc
guillaume@ubuntu:~/py/$ cat main.pyc | zgrep -c "Best School"
1
guillaume@ubuntu:~/py/$ od -t x1 main.pyc # SYSTEM DEPENDANT => CAN BE DIFFERENT
0000000 ee 0c 0d 0a 91 26 3e 58 31 00 00 00 e3 00 00 00
0000020 00 00 00 00 00 00 00 00 00 02 00 00 00 40 00 00
0000040 00 73 0e 00 00 00 65 00 00 64 00 00 83 01 00 01
0000060 64 01 00 53 29 02 7a 10 48 6f 6c 62 65 72 74 6f
0000100 6e 20 53 63 68 6f 6f 6c 4e 29 01 da 05 70 72 69
0000120 6e 74 a9 00 72 02 00 00 00 72 02 00 00 00 fa 07
0000140 6d 61 69 6e 2e 70 79 da 08 3c 6d 6f 64 75 6c 65
0000160 3e 02 00 00 00 73 00 00 00 00
0000172
guillaume@ubuntu:~/py/$ 
```

### Repo:

    GitHub repository: holbertonschool-higher_level_programming
    Directory: python-hello_world
    File: 101-compile

## 12. ByteCode -> Python #1 

Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:

```
  3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
```

    Tip: Python bytecode 

### Repo:

    GitHub repository: holbertonschool-higher_level_programming
    Directory: python-hello_world
    File: 102-magic_calculation.py

