# Python Student Grading Management System

## Project Overview

This project is a Python-based Student Grading Management System designed to manage student information and grades through a menu-driven program.

The system was developed progressively through Sections A–F of the assignment, with all functionality integrated into one final Python program.

## Objectives

The system demonstrates how Python can be used to:

* Store and manage student grades
* Calculate student and class averages
* Search, update and remove student records
* Organise data using lists, tuples and dictionaries
* Apply functions and modular programming
* Implement Object-Oriented Programming (OOP)
* Handle invalid input and exceptions
* Sort student records
* Perform unit and integration testing

## Technologies Used

* Python
* Object-Oriented Programming (OOP)
* Lists and Tuples
* Dictionaries
* Functions
* Exception Handling
* Sorting Algorithms
* Unit Testing

## Project Features

### Section A – Initial Setup

* Student name and grade entry
* Grade validation between 0 and 100
* Student average calculation
* Class statistics

### Section B – Lists and Tuples

* Lists for storing grades
* Tuples for storing student information
* Subject-level statistics
* Highest and lowest grades
* Student averages

### Section C – Dictionaries

Student records are managed using dictionaries.

The system supports:

* Adding students
* Updating grades
* Removing students
* Searching for students
* Retrieving subject-specific grades
* Calculating student averages

### Section D – Functions

The program uses modular functions for:

* Student searches
* Grade updates
* Student details
* Data validation
* Displaying records
* Error handling

### Section E – Object-Oriented Programming

The system implements two main classes:

* `Student` – represents an individual student and manages their grades.
* `Gradebook` – manages student records and operations such as adding, removing, searching and updating students.

The project also includes sorting functionality based on student names and averages.

### Section F – Exception Handling and Testing

The final version includes custom exceptions:

* `InvalidGradeError`
* `StudentNotFoundError`
* `DuplicateStudentError`

It also includes:

* Input validation
* Exception handling
* Bubble sort algorithms
* Unit testing
* Integration testing
* Code comments and documentation

## Testing

The program includes automated tests for important functionality, including:

* Grade validation
* Student creation
* Grade calculations
* Student searching
* Duplicate student handling
* Missing student handling
* Sorting
* Adding, updating and removing students

Both unit tests and integration tests are included.

## How to Run

1. Make sure Python is installed.
2. Download or clone this repository.
3. Open a terminal or command prompt in the project folder.
4. Run the program using:

```bash
python Dikitso_Motona_Grading_System.py
```

5. Follow the menu displayed by the program.

## Main Menu

The system provides options to:

1. Add Student
2. View All Students
3. Search Student
4. Update Student Grade
5. Remove Student
6. View Subject Grades
7. View Subject Statistics
8. Sort Students
9. View Lists and Tuples
10. View Class Statistics
11. Run Tests
12. Exit

## Expected Input and Output

The program accepts student names, subjects and numerical grades.

Grades must be between **0 and 100**.

The system displays information such as:

* Student details
* Grades
* Student averages
* Subject statistics
* Class statistics
* Sorted student records
* Error messages for invalid operations

## Assumptions and Limitations

* Student records are stored in memory while the program is running.
* Data is not stored permanently in a database or external file.
* The program is designed as a command-line application.
* Each student is identified by their name.
* Grades are restricted to values between 0 and 100.

## Project Outcome

This project demonstrates the practical application of Python programming concepts in developing a complete Student Grading Management System.

It combines Python data structures, functions, Object-Oriented Programming, exception handling, sorting algorithms and software testing into one integrated application.
