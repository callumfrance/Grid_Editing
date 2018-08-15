#!/usr/bin/python3
import os
from grid import *

toExit = False

while not toExit:
    # Clears the screen before printing again
    os.system('cls' if os.name == 'nt' else 'clear')
    write_filename = ''

    print("Enter name of file to be converted gridded into a java / python file:")
    read_filename = input("> ")

    if read_filename != "exit":
        in_grid = read_file(read_filename)
        print("File has been read")
        print(in_grid)


        print("Enter name of java file:")
        write_filename = input("> ")

    if write_filename != "exit":
        write_java_file(write_filename, in_grid)
        write_python_file(write_filename, in_grid)
        print("File has been written")

    if write_filename == "exit" or read_filename == "exit":
        toExit = True
    else:
        print("Invalid command")
