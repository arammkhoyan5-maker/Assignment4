import json
import os
from typing import Dict, List, Optional

students: Dict[str, List[float]] = {
    "Max": [85, 92, 78],
    "Marina": [90, 88],
    "Ashley": [65, 74, 50],
    "Bonnie": [99, 87]
}


def display_menu() -> None:
    """
    Display the main menu options.
    """
    print("-" * 30)
    print(
        """1. Add student
2. Add grade
3. Show average for student
4. Show all students
5. Save to file
6. Load from file
7. Exit"""
    )
    print("-" * 30)


def add_student(students: Dict[str, List[float]], name: str) -> None:
    """
    Add a new student to the students dictionary.

    Parameters:
        students (dict): The dictionary of students.
        name (str): The name of the student to add.

    Returns:
        None
    """
    if name not in students:
        students[name] = []
    else:
        print(f"Student {name} already exists.")


def add_grade(students: Dict[str, List[float]], name: str, grade: float) -> None:
    """
    Add a grade to a student's list of grades.

    Parameters:
        students (dict): The dictionary of students.
        name (str): The name of the student.
        grade (float): The grade to add (0-100).

    Returns:
        None
    """
    if name in students:
        if 0 <= grade <= 100:
            students[name].append(grade)
        else:
            print("Grade must be between 0 and 100.")
    else:
        print(f"Student {name} does not exist.")


def average(students: Dict[str, List[float]], name: str) -> Optional[float]:
    """
    Calculate the average grade for a student.

    Parameters:
        students (dict): The dictionary of students.
        name (str): The name of the student.

    Returns:
        float or None: The average grade, or None if no grades exist.
    """
    if name in students and students[name]:
        return sum(students[name]) / len(students[name])
    else:
        print(f"{name} has no grades.")
        return None


def save_to_file(students: Dict[str, List[float]], filename: str) -> None:
    """
    Save the students dictionary to a file in JSON format.

    Parameters:
        students (dict): The dictionary of students.
        filename (str): The name of the file to save to.

    Returns:
        None
    """
    with open(filename, "w") as file:
        json.dump(students, file)


def load_from_file(filename: str) -> Dict[str, List[float]]:
    """
    Load the students dictionary from a file in JSON format.

    Parameters:
        filename (str): The name of the file to load from.

    Returns:
        dict: The dictionary of students loaded from the file, or an empty dictionary if the file does not exist.
    """
    if not os.path.exists(filename):
        print("File does not exist.")
        return {}

    with open(filename, "r") as file:
        return json.load(file)


def delete_student(students: Dict[str, List[float]], name: str) -> None:
    """
    Delete a student from the students dictionary.

    Parameters:
        students (dict): The dictionary of students.
        name (str): The name of the student to delete.

    Returns:
        None
    """
    if name in students:
        del students[name]
        print(f"Deleted student {name}.")
    else:
        print(f"Student {name} does not exist.")


def delete_grade(students: Dict[str, List[float]], name: str, grade: float) -> None:
    """
    Delete a grade from a student's list of grades.

    Parameters:
        students (dict): The dictionary of students.
        name (str): The name of the student.
        grade (float): The grade to delete.

    Returns:
        None
    """
    if name not in students:
        print(f"Student {name} does not exist.")
        return
    if grade not in students[name]:
        print(f"{name} does not have grade {grade}.")
        return
    students[name].remove(grade)
    print(f"Removed grade {grade} from {name}.")


if __name__ == "__main__":
    filename = "students.json"

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter student name: ")
            add_student(students, name)

        elif choice == "2":
            name = input("Enter student name: ")
            grade = float(input("Enter grade (0–100): "))
            add_grade(students, name, grade)

        elif choice == "3":
            name = input("Enter student name: ")
            result = average(students, name)
            if result is not None:
                print(f"Average grade for {name}: {round(result, 2)}")

        elif choice == "4":
            for name, grades in students.items():
                print(f"{name}: {grades}")

        elif choice == "5":
            save_to_file(students, filename)
            print("Saved.")

        elif choice == "6":
            students = load_from_file(filename)
            print("Loaded.")

        elif choice == "7":
            break

        else:
            print("Invalid option.")
