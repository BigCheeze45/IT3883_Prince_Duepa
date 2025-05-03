# Program Name: coin_converter.py
# Course: IT3883/Section W02
# Student Name: Prince Duepa
# Assignment Number: Final Exam - Sprint 1
# Due Date: 05/03/2025
# Purpose: A program that interprets English statements describing
#          amounts of money in coins and converts them to dollar amounts
# List Specific resources used to complete the assignment
#   * https://docs.python.org/3/tutorial/inputoutput.html
#   * https://www.calculatorsoup.com/calculators/financial/money-calculator.php
#   * https://docs.python.org/3/library/unittest.html
#   * https://realpython.com/python-unittest/
#   * https://docs.python.org/3/tutorial/floatingpoint.html

def convert_coins_to_dollars(input_str):
    """
    Convert a string describing coins to a dollar amount.

    Args:
        input_str (str): A string describing coins (e.g., "1 penny and 2 nickels")

    Returns:
        float: The dollar amount

    Raises:
        ValueError: If the input contains an invalid coin denomination
    """
    # Define coin values
    coin_values = {
        "penny": 0.01,
        "pennies": 0.01,
        "nickel": 0.05,
        "nickels": 0.05,
        "dime": 0.10,
        "dimes": 0.10,
        "quarter": 0.25,
        "quarters": 0.25
    }

    # Split the input string by "and"
    segments = [segment.strip() for segment in input_str.split("and")]

    total = 0.0

    # Process each segment
    for segment in segments:
        # Skip empty segments
        if not segment:
            continue

        # Split the segment into words
        words = segment.strip().split()

        # The first word should be the quantity
        try:
            quantity = int(words[0])
        except (ValueError, IndexError):
            raise ValueError(f"Invalid quantity in segment: {segment}")

        # The second word should be the denomination
        try:
            denomination = words[1].lower()
        except IndexError:
            raise ValueError(f"Missing denomination in segment: {segment}")

        # Check if the denomination is valid
        if denomination not in coin_values:
            raise ValueError(f"Invalid coin denomination: {denomination}")

        # Add to the total
        total += quantity * coin_values[denomination]

    return total


def format_as_dollars(amount):
    """
    Format a float as a dollar amount.

    Args:
        amount (float): The amount to format

    Returns:
        str: The formatted dollar amount
    """
    return f"{amount:.2f}"


def process_coin_statement(statement):
    """
    Process a statement about coins and return the dollar amount.

    Args:
        statement (str): A string describing coins

    Returns:
        str: The dollar amount as a string
    """
    try:
        amount = convert_coins_to_dollars(statement)
        return format_as_dollars(amount)
    except ValueError as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    # Test cases
    # print("\nTest cases:")
    # test_cases = [
    #     "1 penny and 2 nickels",
    #     "4 dimes and 7 quarters",
    #     "1 quarter and 3 pennies",
    #     "21 pennies and 17 dimes and 52 quarters",
    #     "95 dimes and 73 quarters and 22 nickels and 36 pennies",
    #     "1 nickel and 17 quarters",
    #     "21 nickels and 15 pennies",
    #     "1 dime and 1 nickel and 1 penny and 1 quarter"
    # ]

    # Run test cases
    # for test in test_cases:
    #     result = process_coin_statement(test)
    #     print(f"{test} -> {result}")

    # Interactive mode
    print("Welcome to the Coin Converter!")
    print("Enter coin statements like '1 penny and 2 nickels' or type 'exit' to quit.")
    while True:
        user_input = input("> ")
        if user_input.lower() == 'exit':
            print("Thank you for using the Coin Converter!")
            break

        result = process_coin_statement(user_input)
        print(f"{result}")
