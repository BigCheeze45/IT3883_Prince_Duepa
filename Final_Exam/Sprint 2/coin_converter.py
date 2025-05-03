# Program Name: coin_converter.py
# Course: IT3883/Section W02
# Student Name: Prince Duepa
# Assignment Number: Final Exam - Sprint 2
# Due Date: 05/03/2025
# Purpose: A program that interprets English statements describing
#          amounts of money in coins and converts them to dollar amounts
# List Specific resources used to complete the assignment
#   * https://docs.python.org/3/tutorial/inputoutput.html
#   * https://www.calculatorsoup.com/calculators/financial/money-calculator.php
#   * https://docs.python.org/3/library/unittest.html
#   * https://realpython.com/python-unittest/
#   * https://docs.python.org/3/tutorial/floatingpoint.html
#   * https://docs.python.org/3/library/decimal.html
#   * https://www.pythontutorial.net/advanced-python/python-decimal/

from decimal import Decimal

# Define coin values using Decimal for precision
COIN_VALUES = {
    "penny": Decimal('0.01'),
    "pennies": Decimal('0.01'),
    "nickel": Decimal('0.05'),
    "nickels": Decimal('0.05'),
    "dime": Decimal('0.10'),
    "dimes": Decimal('0.10'),
    "quarter": Decimal('0.25'),
    "quarters": Decimal('0.25')
}


def convert_coins_to_dollars(input_str):
    """
    Convert a string describing coins to a dollar amount.

    Args:
        input_str (str): A string describing coins (e.g., "1 penny and 2 nickels")

    Returns:
        Decimal: The dollar amount as a Decimal object to ensure precision

    Raises:
        ValueError: If the input contains an invalid coin denomination or format
    """

    # Input validation
    if not input_str or not isinstance(input_str, str):
        raise ValueError("Input must be a non-empty string")

    # Split the input string by "and"
    segments = [segment.strip() for segment in input_str.split("and")]

    total = Decimal('0.0')

    # Process each segment
    for segment in segments:
        # Skip empty segments
        if not segment:
            continue

        # Split the segment into words and filter out empty strings
        words = [word for word in segment.strip().split() if word]

        if len(words) < 2:
            raise ValueError(
                f"Invalid format in segment: '{segment}'. Expected 'quantity denomination'")

        # The first word should be the quantity
        try:
            quantity = int(words[0])
            if quantity < 0:
                raise ValueError(
                    f"Quantity must be a positive number: {quantity}")
        except ValueError:
            raise ValueError(
                f"Invalid quantity in segment: '{segment}'. Expected a number.")

        # The second word should be the denomination
        denomination = words[1].lower()

        # Check if the denomination is valid
        if denomination not in COIN_VALUES:
            raise ValueError(f"Invalid coin denomination: '{denomination}'. "
                             f"Supported denominations are: {', '.join(set(COIN_VALUES.keys()))}")

        # Add to the total
        total += quantity * COIN_VALUES[denomination]

    return total


def format_as_dollars(amount):
    """
    Format a Decimal or float as a dollar amount.

    Args:
        amount (Decimal or float): The amount to format

    Returns:
        str: The formatted dollar amount with 2 decimal places

    Examples:
        >>> format_as_dollars(Decimal('1.1'))
        '1.10'
        >>> format_as_dollars(Decimal('0.05'))
        '0.05'
    """
    # Convert to Decimal if not already
    if not isinstance(amount, Decimal):
        amount = Decimal(str(amount))

    # Format with 2 decimal places
    return f"{amount:.2f}"


def process_coin_statement(statement):
    """
    Process a statement about coins and return the dollar amount.

    This function serves as the main entry point for the program.
    It handles the conversion and formatting in one step.

    Args:
        statement (str): A string describing coins (e.g., "1 penny and 2 nickels")

    Returns:
        str: The dollar amount as a string with 2 decimal places

    Examples:
        >>> process_coin_statement("1 penny and 2 nickels")
        '0.11'
        >>> process_coin_statement("4 dimes and 7 quarters")
        '2.15'
    """
    try:
        # Clean up the input string
        clean_statement = statement.strip()

        # Handle the case of an empty string
        if not clean_statement:
            return "Error: Input cannot be empty"

        amount = convert_coins_to_dollars(clean_statement)
        return format_as_dollars(amount)
    except ValueError as e:
        return f"Error: {str(e)}"


def main():
    """
    Main function to run the coin converter program interactively.
    """
    # print("\nTest cases:")

    # # Test cases
    # test_cases = [
    #     "1 penny and 2 nickels",  # 0.11
    #     "4 dimes and 7 quarters",  # 2.15
    #     "1 quarter and 3 pennies",  # 0.28
    #     "21 pennies and 17 dimes and 52 quarters",  # 14.91
    #     "95 dimes and 73 quarters and 22 nickels and 36 pennies",  # 29.21
    #     "1 nickel and 17 quarters",  # 4.30
    #     "21 nickels and 15 pennies",  # 1.20
    #     "1 dime and 1 nickel and 1 penny and 1 quarter"  # 0.41
    # ]

    # # Run test cases
    # for test in test_cases:
    #     result = process_coin_statement(test)
    #     print(f"{test} -> {result}")
    print("Welcome to the Coin Converter!")
    print("Enter coin statements like '1 penny and 2 nickels' or type 'exit' to quit.")

    # Interactive mode
    while True:
        user_input = input("> ")
        if user_input.lower() == 'exit':
            print("Thank you for using the Coin Converter!")
            break

        result = process_coin_statement(user_input)
        print(f"${result}")


if __name__ == "__main__":
    main()
