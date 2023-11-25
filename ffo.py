def calculate_cgpa_and_total_units():
    grade_points = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'F': 0}

    num_courses = int(input("Enter the number of courses: "))
    
    course_codes = []
    course_units = []
    grades = []

    for i in range(num_courses):
        course_code = input(f"Enter the course code for course {i + 1}: ")
        course_unit_hours = int(input(f"Enter the course units for course {i + 1}: "))
        course_grade = input(f"Enter the grade for course {i + 1} (e.g., A, B, C, D, E, F): ").upper()

        if course_grade in grade_points:
            course_codes.append(course_code)
            course_units.append(course_unit_hours)
            grades.append(course_grade)
        else:
            print(f"Invalid grade '{course_grade}'. Please enter a valid grade.")

    print("\nCourse Information:")
    total_units_course = 0
    for code, credit, grade in zip(course_codes, course_units, grades):
        print(f"Course Code: {code}, Course Units: {credit}, Grade: {grade}")
        total_units_course += credit

    total_credit_points = sum(grade_points[grade] * credit for grade, credit in zip(grades, course_units))
    total_unit_course = sum(course_units)

    if total_unit_course == 0:
        cgpa = 0.0
    else:
        cgpa = total_credit_points / total_unit_course

    return cgpa, total_unit_course

# Example usage
cgpa, total_units = calculate_cgpa_and_total_units()
print(f'\nCGPA: {cgpa:.2f}')
print(f'Total Units Course: {total_units}')
