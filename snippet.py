#!/usr/bin/python3
import os

if not os.path.exists(raw_text):
    os.makedirs(raw_text)

if not os.path.exists(java_output):
    os.makedirs(java_output)





import os.path

save_path = 'C:/example/'

name_of_file = raw_input("What is the name of the file: ")

completeName = os.path.join(save_path, name_of_file+".txt")

file1 = open(completeName, "w")

toFile = raw_input("Write what you want into the field")

file1.write(toFile)

file1.close()
