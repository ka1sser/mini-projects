# TOPIC: Writing Files | .txt, .json, and .csv
import json
import csv

employees_txt = ["Eugene", "Squidward", "Spongebob", "Patrick"]

employee_json = {
    "employee1": {"name": "Spongebob", "age": 30, "job": "Cook"},
    "employee2": {"name": "Patrick", "age": 31, "job": "Sanitation"},
}

employees_csv = [
    ["Name", "Age", "Job"],
    ["Spongebob", 30, "Cook"],
    ["Patrick", 31, "Sanitation"],
    ["Sandy", 27, "Scientist"],
]

file_path_txt = "output.txt"
file_path_json = "output.json"
file_path_csv = "output.csv"

with open(file_path_txt, "w") as file:

    for employee in employees_txt:
        file.write("\n" + employee)

    print(f"txt file '{file_path_txt}' was created.")

with open(file_path_json, "w") as file:
    json.dump(employee_json, file, indent=4)

    print(f"json file '{file_path_json}' was created.")

with open(file_path_csv, "w", newline="") as file:
    writer = csv.writer(file)
    for row in employees_csv:
        writer.writerow(row)
    print(f"csv file '{file_path_csv}' was created.")
