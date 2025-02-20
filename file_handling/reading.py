# Topic: File Handling | File Reading
import json
import csv

txt_file = "C:/Users/eserkai/OneDrive - Ericsson/Documents/Programming/Python/Training/mini-projects/file_handling/output.txt"
json_file = "C:/Users/eserkai/OneDrive - Ericsson/Documents/Programming/Python/Training/mini-projects/file_handling/output.json"
csv_file = "C:/Users/eserkai/OneDrive - Ericsson/Documents/Programming/Python/Training/mini-projects/file_handling/output.csv"

with open(txt_file, "r") as file:
    content = file.read()
    print(f"Printing '{txt_file}' contents:")
    print(content)

with open(json_file, "r") as file:
    content = json.load(file)
    print(f"Printing '{json_file}' contents:")
    print(content)

with open(csv_file, "r") as file:
    content = csv.reader(file)
    print(f"Printing '{csv_file}' contents:")

    for line in content:
        print(line)
