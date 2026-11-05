#Grant Brooks
#Assigment 8: Git Development with AI

#function: get_letter_grade converts a score into a letter grade
def get_letter_grade(score):
    """Return a letter grade for a numeric score."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    return "F"


def main():
    print("=== Grade Tracker ===")
#dict: grades dict stores a student's name and score

    grades = {}

    while True:
        try:
            count = int(input("How many students do you want to enter? "))
            if count > 0:
                break
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Please enter a valid whole number.")
#input: asks for number of students and grades

#loop: a for loop collects all student info. another while loop is used to govern the user input
    for i in range(count):
        name = input(f"\nStudent {i + 1} name: ").strip()
        while True:
            try:
                score = float(input(f"Score for {name} (0-100): "))
                if 0 <= score <= 100:
                    break
                print("Score must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")
        grades[name] = score

    print("\n=== Grade Report ===")
    for name, score in grades.items():
        print(f"{name:<15} {score:>6.1f}  Grade: {get_letter_grade(score)}")

    average = sum(grades.values()) / len(grades)
    top_student = max(grades, key=grades.get)


#output: a formatted report with each student's grade and name, along with score (up to one decimal)
    print("\n--- Summary ---")
    print(f"Class average: {average:.1f}")
    print(f"Top student:   {top_student} ({grades[top_student]:.1f})")


if __name__ == "__main__":
    main()
