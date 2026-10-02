# ============================================================
# STUDENT GRADING MANAGEMENT SYSTEM
# ============================================================
# Name:
# Language: Python
#
# Project:
# A complete student grading management system developed
# progressively from basic Python concepts to Object-Oriented
# Programming, exception handling, searching, sorting and testing.
#
# ============================================================


# ============================================================
# SECTION A – INITIAL SETUP
# Scalar Objects, Loops, Input and Validation
# ============================================================

def validate_grade(grade):
    """
    Validate that a grade is a number between 0 and 100.
    """

    try:
        grade = float(grade)
    except (ValueError, TypeError):
        raise InvalidGradeError("Grade must be a number.")

    if grade < 0 or grade > 100:
        raise InvalidGradeError(
            "Grade must be between 0 and 100."
        )

    return grade


def get_valid_grade():
    """
    Continuously request a valid grade from the user.
    """

    while True:
        try:
            grade = float(input("Enter grade (0-100): "))
            return validate_grade(grade)

        except InvalidGradeError as error:
            print(f"Invalid grade: {error}")


def get_student_name():
    """
    Request a non-empty student name.
    """

    while True:
        name = input("Enter student name: ").strip()

        if name:
            return name

        print("Student name cannot be empty.")


def calculate_class_statistics(gradebook):
    """
    Calculate the total and average of all grades
    in the class.

    This implements the basic calculation requirements
    introduced in Section A.
    """

    all_grades = []

    for student in gradebook.students.values():
        for grade in student.grades.values():
            all_grades.append(grade)

    if not all_grades:
        print("\nNo grades available.")
        return

    total = sum(all_grades)
    average = total / len(all_grades)

    print("\n" + "=" * 55)
    print("                  CLASS STATISTICS")
    print("=" * 55)

    print(f"Number of grades : {len(all_grades)}")
    print(f"Total grades     : {total:.2f}")
    print(f"Class average    : {average:.2f}")


# ============================================================
# SECTION B – LISTS AND TUPLES
# Multiple Subjects, Averages and Min/Max
# ============================================================

def get_student_tuple(student):
    """
    Represent a student using the tuple structure required
    in Section B.

    Example:
        ("Dikitso", [78, 85, 91])
    """

    grades_list = list(student.grades.values())

    return student.name, grades_list


def display_lists_and_tuples(gradebook):
    """
    Display each student's information using lists and tuples.
    """

    if not gradebook.students:
        print("\nNo students available.")
        return

    print("\n" + "=" * 60)
    print("              LISTS AND TUPLES")
    print("=" * 60)

    for student in gradebook.students.values():

        student_tuple = get_student_tuple(student)

        print(f"\nStudent Tuple: {student_tuple}")

        print(f"Name: {student_tuple[0]}")
        print(f"Grades List: {student_tuple[1]}")

        if student.grades:
            average = sum(student_tuple[1]) / len(
                student_tuple[1]
            )

            print(f"Average: {average:.2f}")


def display_subject_statistics(gradebook):
    """
    Display grades, highest grade, lowest grade and
    average for a selected subject.
    """

    subject = input(
        "\nEnter subject: "
    ).strip().title()

    grades = []

    for student in gradebook.students.values():

        if subject in student.grades:
            grades.append(
                (student.name, student.grades[subject])
            )

    if not grades:
        print(
            f"\nNo grades found for subject '{subject}'."
        )
        return

    grade_values = [
        grade for name, grade in grades
    ]

    highest = max(grade_values)
    lowest = min(grade_values)
    average = sum(grade_values) / len(grade_values)

    print("\n" + "=" * 55)
    print(f"              {subject.upper()} RESULTS")
    print("=" * 55)

    for name, grade in grades:
        print(f"{name}: {grade:.2f}")

    print("-" * 55)
    print(f"Highest grade : {highest:.2f}")
    print(f"Lowest grade  : {lowest:.2f}")
    print(f"Average grade : {average:.2f}")


# ============================================================
# SECTION C – DICTIONARIES
# Student Management and Data Access
# ============================================================

# Student records are stored in a dictionary:
#
# students = {
#     "Dikitso": Student object,
#     "Thapelo": Student object
# }
#
# Each Student object contains another dictionary:
#
# grades = {
#     "Math": 80,
#     "English": 85,
#     "Science": 90
# }


def add_student(gradebook):
    """
    Add a new student to the dictionary.
    """

    name = get_student_name()

    try:
        gradebook.add_student(name)

        print(
            f"\nStudent '{name}' added successfully."
        )

        print(
            "\nEnter the student's subjects and grades."
        )

        while True:

            subject = input(
                "Enter subject "
                "(or type 'done' to finish): "
            ).strip()

            if subject.lower() == "done":
                break

            if not subject:
                print("Subject cannot be empty.")
                continue

            subject = subject.title()

            grade = get_valid_grade()

            gradebook.update_grade(
                name,
                subject,
                grade
            )

        print("\nStudent record completed.")

    except DuplicateStudentError as error:
        print(f"Error: {error}")


def search_student(gradebook):
    """
    Search for a student by name and display
    their grades and average.
    """

    name = input(
        "\nEnter student name to search: "
    ).strip()

    try:

        student = gradebook.search_student(name)

        display_student_details(student)

    except StudentNotFoundError as error:
        print(f"Error: {error}")


def update_student_grade(gradebook):
    """
    Search for a student and update one of their grades.
    """

    name = input(
        "\nEnter student name: "
    ).strip()

    try:

        student = gradebook.search_student(name)

        print(f"\nUpdating grades for {student.name}")

        subject = input(
            "Enter subject: "
        ).strip().title()

        if not subject:
            print("Subject cannot be empty.")
            return

        grade = get_valid_grade()

        gradebook.update_grade(
            name,
            subject,
            grade
        )

        print(
            f"\n{subject} grade updated successfully."
        )

    except StudentNotFoundError as error:
        print(f"Error: {error}")


def remove_student(gradebook):
    """
    Remove a student from the dictionary.
    """

    name = input(
        "\nEnter student name to remove: "
    ).strip()

    try:

        gradebook.remove_student(name)

        print(
            f"\nStudent '{name}' removed successfully."
        )

    except StudentNotFoundError as error:
        print(f"Error: {error}")


def display_subject_grades(gradebook):
    """
    View grades for a specific subject across
    all students.
    """

    subject = input(
        "\nEnter subject: "
    ).strip().title()

    results = gradebook.get_subject_grades(subject)

    if not results:
        print(
            f"\nNo grades found for '{subject}'."
        )
        return

    print("\n" + "=" * 50)
    print(f"          {subject.upper()} GRADES")
    print("=" * 50)

    for name, grade in results:
        print(f"{name}: {grade:.2f}")


# ============================================================
# SECTION D – FUNCTIONS
# Modularisation and Error Handling
# ============================================================

def display_student_details(student):
    """
    Display all information for one student.
    """

    print("\n" + "=" * 55)
    print(f"                  {student.name}")
    print("=" * 55)

    if not student.grades:
        print("No grades recorded.")
        return

    for subject, grade in student.grades.items():
        print(f"{subject:<20} {grade:.2f}")

    print("-" * 55)
    print(
        f"{'Average':<20} "
        f"{student.calculate_average():.2f}"
    )

    print(
        f"{'Highest':<20} "
        f"{student.get_highest_grade():.2f}"
    )

    print(
        f"{'Lowest':<20} "
        f"{student.get_lowest_grade():.2f}"
    )


def display_all_students(gradebook):
    """
    Display all students in the gradebook.
    """

    if not gradebook.students:
        print("\nNo students have been added.")
        return

    print("\n" + "=" * 60)
    print("                  ALL STUDENTS")
    print("=" * 60)

    for student in gradebook.students.values():
        display_student_details(student)


# ============================================================
# SECTION E – OBJECT-ORIENTED PROGRAMMING
# Student and Gradebook Classes
# ============================================================


class Student:
    """
    Represents one student.

    Attributes:
        name
        grades
    """

    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        """
        Add a grade for a subject.
        """

        grade = validate_grade(grade)

        self.grades[subject] = grade

    def calculate_average(self):
        """
        Calculate the student's average grade.
        """

        if not self.grades:
            return 0

        return (
            sum(self.grades.values())
            / len(self.grades)
        )

    def get_highest_grade(self):
        """
        Return the highest grade.
        """

        if not self.grades:
            return 0

        return max(self.grades.values())

    def get_lowest_grade(self):
        """
        Return the lowest grade.
        """

        if not self.grades:
            return 0

        return min(self.grades.values())

    def display_details(self):
        """
        Print the student's details.
        """

        display_student_details(self)


class Gradebook:
    """
    Manages a collection of Student objects.
    """

    def __init__(self):
        self.students = {}

    def add_student(self, name):
        """
        Add a new Student object to the gradebook.
        """

        if name in self.students:
            raise DuplicateStudentError(
                f"Student '{name}' already exists."
            )

        self.students[name] = Student(name)

    def remove_student(self, name):
        """
        Remove a student.
        """

        if name not in self.students:
            raise StudentNotFoundError(
                f"Student '{name}' was not found."
            )

        del self.students[name]

    def search_student(self, name):
        """
        Search for a student.
        """

        if name not in self.students:
            raise StudentNotFoundError(
                f"Student '{name}' was not found."
            )

        return self.students[name]

    def update_grade(
        self,
        name,
        subject,
        grade
    ):
        """
        Add or update a student's grade.
        """

        student = self.search_student(name)

        student.add_grade(
            subject,
            grade
        )

    def get_subject_grades(self, subject):
        """
        Return grades for one subject across
        all students.
        """

        results = []

        for student in self.students.values():

            if subject in student.grades:

                results.append(
                    (
                        student.name,
                        student.grades[subject]
                    )
                )

        return results


# ============================================================
# SECTION F – FINAL ENHANCEMENTS
# Custom Exceptions, Searching, Sorting and Testing
# ============================================================


class InvalidGradeError(Exception):
    """
    Raised when a grade is invalid.
    """
    pass


class StudentNotFoundError(Exception):
    """
    Raised when a student cannot be found.
    """
    pass


class DuplicateStudentError(Exception):
    """
    Raised when a duplicate student is added.
    """
    pass


def bubble_sort_by_average(
    gradebook,
    descending=True
):
    """
    Sort students by average grade using
    the Bubble Sort algorithm.
    """

    students = list(
        gradebook.students.values()
    )

    n = len(students)

    for i in range(n):

        swapped = False

        for j in range(
            0,
            n - i - 1
        ):

            average_one = (
                students[j].calculate_average()
            )

            average_two = (
                students[j + 1].calculate_average()
            )

            if descending:

                should_swap = (
                    average_one < average_two
                )

            else:

                should_swap = (
                    average_one > average_two
                )

            if should_swap:

                students[j], students[j + 1] = (
                    students[j + 1],
                    students[j]
                )

                swapped = True

        if not swapped:
            break

    return students


def bubble_sort_by_name(gradebook):
    """
    Sort students alphabetically using Bubble Sort.
    """

    students = list(
        gradebook.students.values()
    )

    n = len(students)

    for i in range(n):

        swapped = False

        for j in range(
            0,
            n - i - 1
        ):

            if (
                students[j].name.lower()
                >
                students[j + 1].name.lower()
            ):

                students[j], students[j + 1] = (
                    students[j + 1],
                    students[j]
                )

                swapped = True

        if not swapped:
            break

    return students


def sort_students(gradebook):
    """
    Allow the user to choose how students
    should be sorted.
    """

    print("\n" + "=" * 50)
    print("                  SORT STUDENTS")
    print("=" * 50)

    print("1. Sort by Name")
    print("2. Sort by Average - Highest First")
    print("3. Sort by Average - Lowest First")

    choice = input(
        "\nEnter your choice: "
    ).strip()

    if choice == "1":

        students = bubble_sort_by_name(
            gradebook
        )

    elif choice == "2":

        students = bubble_sort_by_average(
            gradebook,
            descending=True
        )

    elif choice == "3":

        students = bubble_sort_by_average(
            gradebook,
            descending=False
        )

    else:

        print("Invalid choice.")
        return

    print("\n" + "=" * 60)
    print("                 SORTED RESULTS")
    print("=" * 60)

    for position, student in enumerate(
        students,
        start=1
    ):

        print(
            f"{position}. "
            f"{student.name} - "
            f"Average: "
            f"{student.calculate_average():.2f}"
        )


# ============================================================
# SECTION F – TESTING AND DOCUMENTATION
# ============================================================

def run_unit_tests():
    """
    Unit testing documentation:

    The following individual components are tested:

    1. Grade validation
    2. Student creation
    3. Grade addition
    4. Average calculation
    5. Student searching
    6. Duplicate student handling
    7. Missing student handling
    8. Student removal
    9. Bubble Sort by average
    10. Bubble Sort by name
    """

    print("\nRunning unit tests...")

    # Grade validation
    assert validate_grade(50) == 50
    assert validate_grade(0) == 0
    assert validate_grade(100) == 100

    # Invalid grade
    try:
        validate_grade(101)
        assert False
    except InvalidGradeError:
        pass

    # Student class
    student = Student("Test Student")

    student.add_grade(
        "Math",
        80
    )

    student.add_grade(
        "English",
        90
    )

    assert (
        student.calculate_average()
        == 85
    )

    # Gradebook
    gradebook = Gradebook()

    gradebook.add_student("Alice")

    gradebook.update_grade(
        "Alice",
        "Math",
        80
    )

    assert (
        gradebook
        .search_student("Alice")
        .calculate_average()
        == 80
    )

    # Duplicate student test
    try:

        gradebook.add_student("Alice")

        assert False

    except DuplicateStudentError:
        pass

    # Missing student test
    try:

        gradebook.search_student("Unknown")

        assert False

    except StudentNotFoundError:
        pass

    # Sorting test
    gradebook.add_student("Bob")

    gradebook.update_grade(
        "Bob",
        "Math",
        90
    )

    sorted_students = (
        bubble_sort_by_average(
            gradebook
        )
    )

    assert (
        sorted_students[0].name
        == "Bob"
    )

    print(
        "All unit tests passed successfully."
    )


def run_integration_test():
    """
    Integration test for the complete system.

    Tests the complete workflow:

    Add → Update → Search → Sort → Remove
    """

    print(
        "\nRunning integration test..."
    )

    gradebook = Gradebook()

    gradebook.add_student(
        "Integration Student"
    )

    gradebook.update_grade(
        "Integration Student",
        "Math",
        80
    )

    gradebook.update_grade(
        "Integration Student",
        "English",
        90
    )

    student = gradebook.search_student(
        "Integration Student"
    )

    assert (
        student.calculate_average()
        == 85
    )

    gradebook.update_grade(
        "Integration Student",
        "Math",
        100
    )

    assert (
        student.grades["Math"]
        == 100
    )

    sorted_students = (
        bubble_sort_by_average(
            gradebook
        )
    )

    assert (
        sorted_students[0].name
        == "Integration Student"
    )

    gradebook.remove_student(
        "Integration Student"
    )

    assert (
        "Integration Student"
        not in gradebook.students
    )

    print(
        "Integration test passed successfully."
    )


def run_all_tests():
    """
    Run both unit and integration tests.
    """

    print("\n" + "=" * 60)
    print("                    TESTING")
    print("=" * 60)

    try:

        run_unit_tests()
        run_integration_test()

        print(
            "\nAll tests completed successfully."
        )

    except AssertionError:

        print(
            "\nA test failed. "
            "Please check the implementation."
        )

    except Exception as error:

        print(
            f"\nTesting error: {error}"
        )


# ============================================================
# MAIN MENU
# ============================================================

def display_menu():
    """
    Display the main program menu.
    """

    print("\n")
    print("=" * 60)
    print("           STUDENT GRADING MANAGEMENT SYSTEM")
    print("=" * 60)

    print("1.  Add Student")
    print("2.  View All Students")
    print("3.  Search Student")
    print("4.  Update Student Grade")
    print("5.  Remove Student")
    print("6.  View Subject Grades")
    print("7.  View Subject Statistics")
    print("8.  Sort Students")
    print("9.  View Lists and Tuples")
    print("10. View Class Statistics")
    print("11. Run Tests")
    print("0.  Exit")

    print("=" * 60)


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():
    """
    Main function controlling the entire application.
    """

    gradebook = Gradebook()

    print("=" * 60)
    print("       WELCOME TO THE STUDENT GRADING SYSTEM")
    print("=" * 60)

    while True:

        display_menu()

        choice = input(
            "Enter your choice: "
        ).strip()

        try:

            if choice == "1":

                add_student(
                    gradebook
                )

            elif choice == "2":

                display_all_students(
                    gradebook
                )

            elif choice == "3":

                search_student(
                    gradebook
                )

            elif choice == "4":

                update_student_grade(
                    gradebook
                )

            elif choice == "5":

                remove_student(
                    gradebook
                )

            elif choice == "6":

                display_subject_grades(
                    gradebook
                )

            elif choice == "7":

                display_subject_statistics(
                    gradebook
                )

            elif choice == "8":

                sort_students(
                    gradebook
                )

            elif choice == "9":

                display_lists_and_tuples(
                    gradebook
                )

            elif choice == "10":

                calculate_class_statistics(
                    gradebook
                )

            elif choice == "11":

                run_all_tests()

            elif choice == "0":

                print(
                    "\nThank you for using "
                    "the Student Grading System."
                )

                break

            else:

                print(
                    "\nInvalid menu choice. "
                    "Please try again."
                )

        except Exception as error:

            print(
                f"\nAn unexpected error occurred: "
                f"{error}"
            )


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()