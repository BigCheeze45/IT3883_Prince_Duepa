# Program Name: main.py
# Course: IT3883/Section W02
# Student Name: Prince Duepa
# Assignment Number: Lab/Assignment 5
# Due Date: 04/18/2025
# Purpose: a Python program to create and interact with a
#          database
# List Specific resources used to complete the assignment
# * https://docs.python.org/3/library/sqlite3.html
# * https://docs.python.org/3/library/argparse.html
# * https://www.sqlitetutorial.net/sqlite-avg/

import sqlite3
import argparse

from pathlib import Path


def read_input_file(path: Path):
    """Read input data file"""
    data = []
    with open(path) as f:
        # read file line by line
        for line in f.readlines():
            # ignore empty lines - typically end of file
            if line.strip() != "":
                # strip new line chars from each line
                line = line.strip().lower()
                # return a tuple for easy DB insertion
                data.append(tuple(line.split(" ")))
    return data


def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        prog="litexplorer",
        description="a Python program to create and interact with a database",
    )
    parser.add_argument("filename", type=Path)

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    # read CLI arguments
    args = parse_arguments()
    if not args.filename.exists():
        print(f"ERROR: {args.filename} not found. Please check file path and try again")
        exit(1)

    table_name = "temperature"
    con = sqlite3.connect("assignment5.db")
    cur = con.cursor()

    # create temperature DB
    cur.execute(
        f"CREATE TABLE IF NOT EXISTS {table_name}(ID INTEGER PRIMARY KEY, Day_Of_Week, Temperature_Value)"
    )

    # read input file with data
    # returns a list of tuple for each line
    # each tuple contains (Day of the week, Temperature)
    data = read_input_file(args.filename)

    # Delete all previous temps/ids before inserting new ones
    cur.execute(f"DELETE FROM {table_name}")
    cur.executemany(
        f"INSERT INTO {table_name} (Day_Of_Week, Temperature_Value) VALUES(?,?)", data
    )
    con.commit()

    # Find average for Sunday. Use lowercase since read_input_file does
    result = cur.execute(
        f"SELECT AVG(Temperature_Value) FROM {table_name} WHERE Day_Of_Week = 'sunday'"
    ).fetchone()
    print(f"Average temperature for Sunday: {round(result[0], 1)}")

    # Find average for Thursday
    result = cur.execute(
        f"SELECT AVG(Temperature_Value) FROM {table_name} WHERE Day_Of_Week = 'thursday'"
    ).fetchone()
    print(f"Average temperature for Thursday: {round(result[0], 1)}")
