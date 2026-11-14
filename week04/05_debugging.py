

import csv
import json
from pathlib import Path
#Shan_72387_PFAI_Week04
base_folder = Path(__file__).resolve().parent
data_folder = base_folder / "data"
data_folder.mkdir(parents=True, exist_ok=True)

print("--- Running Part F: Debugging Exercises ---\n")

#Shan_72387_PFAI_Week04
class Student:
    """Corrected Student class with self parameter."""

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


s = Student("Ali", [80, 90])
print(f"F1 Fixed: Student created successfully -> Name: {s.name}, Marks: {s.marks}")

#Shan_72387_PFAI_Week04
csv_file_path = data_folder / "debug_students.csv"

with open(csv_file_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Ali", 85])

print("F2 Fixed: CSV row written successfully in 'w' mode.")
#Shan_72387_PFAI_Week04
class Model:
    """Simple model representation."""

    def __init__(self, model_name, accuracy):
        self.model_name = model_name
        self.accuracy = accuracy

    def to_dictionary(self):
        """Convert object attributes to a dictionary."""
        return {
            "model_name": self.model_name,
            "accuracy": self.accuracy,
        }

#Shan_72387_PFAI_Week04
model = Model("Decision Tree", 0.88)
json_file_path = data_folder / "debug_model.json"

with open(json_file_path, "w", encoding="utf-8") as file:
    json.dump(model.to_dictionary(), file, indent=4)

print("F3 Fixed: Model object converted to dictionary and dumped to JSON.")
print("\nAll debugging tasks in 04_debugging.py executed without errors!")