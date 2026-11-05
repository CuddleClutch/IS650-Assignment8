# Grade Tracker

## Project Description
A command-line Python program that lets an instructor enter student names and scores, then view a formatted grade report with letter grades, class average, and top student.

## Initial Version
Features developed independently in the first push:
- **get_letter_grade function**: converts a numeric score (0-100) into a letter grade (A through F)
- **Input collection loop**: a for loop collects each student's name and score, with a nested while loop for input validation
- **Grades dictionary**: stores each student's name as the key and their score as the value
- **User input**: prompts for the number of students, then each name and score
- **Formatted output**: prints a grade report table, class average, and top student

## AI Tool Used
Claude (Anthropic)

## AI Assistance
I asked Claude to help me add an interactive menu system so the user can explore the grade data after entering it, instead of the program just printing the report and exiting. Specifically, I asked for the ability to sort students by score and to see a breakdown of how many students earned each letter grade.

## New or Modified Features
Added in the second push with AI assistance:
- **Interactive menu**: after the initial report displays, a menu loop lets the user choose between viewing the report again, sorting students, viewing grade distribution, or exiting
- **Sort by score**: displays all students ranked from highest to lowest score
- **Grade distribution**: a new `get_grade_distribution` function counts how many students earned each letter grade and displays the results with a simple bar chart
- **Refactored show_report**: moved the report display logic into its own function so it can be called from the menu

## Evaluation of AI Output
I accepted the AI's recommendations with minor adjustments. The menu structure, sorting, and grade distribution features were all reasonable and easy to understand. I kept the visual bar chart idea for the distribution because it makes the output more readable. The code was clean and matched the style of my original program, so I did not need to reject or heavily modify anything.

## How to Run the Program
1. Make sure Python 3 is installed
2. Open a terminal in the project folder
3. Run: `python main.py`
4. Enter the number of students, then each name and score when prompted
5. Use the menu to explore the grade data
