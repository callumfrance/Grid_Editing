#!/usr/bin/python3

import os.path

''' java '''
a = "public class " # Name
b = "{\n\tpublic char[][] " # name
c = " = {\n"
# The actual grid items
d = "\t};\n}"

''' python '''
a2 = '#!/usr/bin/python3\n\n'

write_file = None

# converts the first character of a string to uppercase
def to_uppercase(instring):
    converted = ''
    to_convert = instring[:1]
    if to_convert.isalpha():
        converted = to_convert.upper()
    print(converted + instring[1:])
    return converted + instring[1:]

# converts the first character of a string to lowercase
def to_lowercase(instring):
    converted = ''
    to_convert = instring[:1]
    if to_convert.isalpha():
        converted = to_convert.lower()
    print(converted + instring[1:])
    return converted + instring[1:]

# Reads a 'grid' text file into the program
def read_file(filename):
    file = open(filename, 'r')
    raw_next = file.readline()    # reads one line of the file
    colsize = len(raw_next) - 1   # determines the amount of columns minus \n
    next = raw_next[:-1]          # strips the newline character
    the_grid = []                 # what is exported
    while next != "":
        the_grid.append(next)
        raw_next = file.readline()
        next = raw_next[:colsize] # a 'columns' worth of characters

    file.close()            # close the file once finished
    return the_grid

# Write a grid of characters to a java file
def write_java_file(in_file_name, grid):
    filename = ""           # The name of the file e.g. Test.java
    # in_file_name          # The name cpitalized e.g. Test
    var_name = ""           # The name lowercase e.g. test
    run = False

    if "." in in_file_name:
        in_file_name = (in_file_name.split('.'))[0] # in case entered test.java

    in_file_name = to_uppercase(in_file_name)
    var_name = to_lowercase(in_file_name)
    # filename = in_file_name + ".java"
    if not os.path.exists('java_output/'):
        os.makedirs('java_output/')
    filename = os.path.join('java_output/', in_file_name+".java")
    write_file = open(filename, 'w')

    write_file.write(a)
    write_file.write(in_file_name)
    write_file.write(b)
    write_file.write(var_name)
    write_file.write(c)

    k = 0

    # loop through all the grid items
    for row in grid:
        j = 0

        write_file.write("\t\t{")
        for item in row:
            j = j + 1
            write_file.write("'" + item + "'")
            if j != len(row):
                write_file.write(", ")
                # print(item + "\t" + str(len(row)))
            else:
                write_file.write("}")

        if k != len(grid) - 1:
            write_file.write(",\n")
            # print("\t" + str(k) + "\t" + str(len(grid)))
            k = k + 1
        else:
            write_file.write("\n")

    write_file.write(d)

    write_file.close()

# Write to a python file
def write_python_file(in_file_name, grid):
    filename = ""
    # in_file_name
    var_name = ""

    if "." in in_file_name:
        in_file_name = (in_file_name.split('.'))[0] # in case entered test.java

    in_file_name = to_uppercase(in_file_name)
    var_name = to_lowercase(in_file_name)
    # filename = in_file_name + ".py"
    if not os.path.exists('python_output/'):
        os.makedirs('python_output/')
    filename = os.path.join('python_output/', in_file_name+".py")
    write_file = open(filename, 'w')

    write_file.write(a2)
    write_file.write(var_name)
    write_file.write(" = [ \\\n")

    k = 0

    # loop through all the grid items
    for row in grid:
        j = 0

        write_file.write("    [")
        for item in row:
            j = j + 1
            if j != len(row):
                write_file.write(item)
                write_file.write(", ")
            else:
                write_file.write("]")

        if k != len(grid) - 1:
            write_file.write(", \\\n")
            k = k + 1
        else:
            write_file.write(" ]")

    write_file.close()
