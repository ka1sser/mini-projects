# Topic: File Detection

import os

file_path = "C:/Users/eserkai/OneDrive - Ericsson/Documents/Programming/Python/Training/mini-projects/file_handling/test.txt"

if os.path.exists(file_path):
    print(f"I found the location of '{file_path}' exists!")

    if os.path.isfile(file_path):
        print("That is a file!")
else:
    print("File is missing!")
