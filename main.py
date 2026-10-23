from grade_processor import (
    InvalidScoreError,
    Student,
    calculate_average,
    get_highest_lowest,
    get_pass_fail_status,
)


def print_report(students: list[Student]) -> None:
    """Executing the entire value-processing pipeline"""
    print("=== Student Graduation Results Report ===")

    student_statuses = get_pass_fail_status(students, passing_score=60.0)

    print(f"\n{'Name':<15} | {'Score':>6} | {'Status':<6}")
    print("-" * 34)
    for s in student_statuses:
        print(f"{s['name']:<15} | {s['score']:>6.1f} | {s['status']:<6}")

    average_score = calculate_average(students)
    highest_student, lowest_student = get_highest_lowest(students)

    print("\n--- Statistical Summary ---")
    print(f"Average Class : {average_score:.2f}")
    print(
        f"Highest Score : {highest_student['name']} ({highest_student['score']:.1f})"
    )
    print(
        f"Lowest Score  : {lowest_student['name']} ({lowest_student['score']:.1f})"
    )


def main():
    valid_students: list[Student] = [
        {"name": "Budi", "score": 85.0},
        {"name": "Siti", "score": 92.5},
        {"name": "Andi", "score": 45.0},
        {"name": "Rina", "score": 60.0},
    ]

    print("Test 1: Normal Data")
    try:
        print_report(valid_students)
    except InvalidScoreError as e:
        print(f"Value Error: {e}")
    except ValueError as e:
        print(f"System Errpr: {e}")

    print("\n" + "=" * 40 + "\n")

    invalid_students: list[Student] = [
        {"name": "Eko", "score": 75.0},
        {"name": "Doni", "score": 150.0},
    ]

    print("Test 2: Data Values ​​Outside of Limits")
    try:
        print_report(invalid_students)
    except InvalidScoreError as e:
        print(f"Value Error: {e}")
    except ValueError as e:
        print(f"System Error: {e}")


if __name__ == "__main__":
    main()