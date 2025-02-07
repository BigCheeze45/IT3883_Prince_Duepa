# Program Name: grade_average_calculator.py
# Course: IT3883/Section W02
# Student Name: Prince Duepa
# Assignment Number: Lab/Assignment 2
# Due Date: 02/07/2025
# Purpose: Given a file containing grade scores, calculate the average
#          then present them in descending order
# List Specific resources used to complete the assignment
#   * https://fstring.help/cheat/
#   * https://docs.python.org/3.11/library/argparse.html
#   * https://realpython.com/command-line-interfaces-python-argparse/
#   * https://docs.python.org/3.11/library/typing.html
#   * https://www.pythontutorial.net/python-basics/python-type-hints/


import argparse
from pathlib import Path
from typing import List, Dict


def parse_arguments() -> argparse.Namespace:
    """Set up command-line argument parsing."""
    parser = argparse.ArgumentParser(
        description='Calculate and sort student averages from an input file.'
    )
    parser.add_argument(
        'input_file',
        help='Path to the input file containing student grades'
    )
    return parser.parse_args()


def read_student_data(filename: str) -> Dict[str, List[float]]:
    """
    Read student data from the input file.

    Args:
        filename: Path to the input file

    Returns:
        List of tuples containing (student_name, list_of_scores)
    """
    students = {}
    with open(filename) as file:
        for i, line in enumerate(file):
            # Split the line into fields
            fields = line.strip().split()

            # Assume first field is the name, rest are scores
            name = fields[0]
            try:
                scores = [float(score) for score in fields[1:]]
                students[name] = scores
            except ValueError as e:
                print(
                    f"Skipping line {i+1} ({name}) due to invalid score: {line.strip()}")
                continue

    return students


def calculate_average(scores: List[float]) -> float:
    """Calculate the average of a list of scores."""
    return sum(scores) / len(scores)


def main():
    # Parse command-line arguments
    args = parse_arguments()

    input_file = Path(args.input_file)
    if not input_file.exists():
        print(f"Error: Could not find file '{input_file}'")
        exit(1)

    # Read and process the student data
    students = read_student_data(input_file)

    # Calculate averages and sort in descending order
    student_averages = [
        (name, calculate_average(scores))
        for name, scores in students.items()
    ]
    student_averages.sort(key=lambda row: row[1], reverse=True)
    # Print results
    # print("\nStudent Averages (Sorted by Grade):")
    # print("-" * 40)
    # print(f"{'Name':<30} {'Average':>8}")
    # print("-" * 40)
    print()
    for name, average in student_averages:
        print(f"{name:<10} {average:>8.2f}")


if __name__ == "__main__":
    main()
