"""
Unit tests for the Coin Converter program.

This module contains comprehensive tests for all functions in the coin_converter module.
"""

import unittest
from decimal import Decimal
from coin_converter import convert_coins_to_dollars, format_as_dollars, process_coin_statement


class TestCoinConverter(unittest.TestCase):
    """Test suite for the Coin Converter program."""

    def test_convert_coins_to_dollars_basic(self):
        """Test basic single denomination cases."""
        # Test single coins
        self.assertEqual(convert_coins_to_dollars("1 penny"), Decimal('0.01'))
        self.assertEqual(convert_coins_to_dollars("1 nickel"), Decimal('0.05'))
        self.assertEqual(convert_coins_to_dollars("1 dime"), Decimal('0.10'))
        self.assertEqual(convert_coins_to_dollars(
            "1 quarter"), Decimal('0.25'))

        # Test multiple of the same coin
        self.assertEqual(convert_coins_to_dollars(
            "5 pennies"), Decimal('0.05'))
        self.assertEqual(convert_coins_to_dollars(
            "10 nickels"), Decimal('0.50'))
        self.assertEqual(convert_coins_to_dollars("20 dimes"), Decimal('2.00'))
        self.assertEqual(convert_coins_to_dollars(
            "4 quarters"), Decimal('1.00'))

    def test_convert_coins_to_dollars_plural_forms(self):
        """Test singular and plural forms of denominations."""
        self.assertEqual(convert_coins_to_dollars("1 penny"), Decimal('0.01'))
        self.assertEqual(convert_coins_to_dollars(
            "2 pennies"), Decimal('0.02'))
        self.assertEqual(convert_coins_to_dollars("1 nickel"), Decimal('0.05'))
        self.assertEqual(convert_coins_to_dollars(
            "2 nickels"), Decimal('0.10'))
        self.assertEqual(convert_coins_to_dollars("1 dime"), Decimal('0.10'))
        self.assertEqual(convert_coins_to_dollars("2 dimes"), Decimal('0.20'))
        self.assertEqual(convert_coins_to_dollars(
            "1 quarter"), Decimal('0.25'))
        self.assertEqual(convert_coins_to_dollars(
            "2 quarters"), Decimal('0.50'))

    def test_convert_coins_to_dollars_combinations(self):
        """Test combinations of different coin denominations."""
        # Test from provided test cases
        self.assertEqual(convert_coins_to_dollars(
            "1 penny and 2 nickels"), Decimal('0.11'))
        self.assertEqual(convert_coins_to_dollars(
            "4 dimes and 7 quarters"), Decimal('2.15'))
        self.assertEqual(convert_coins_to_dollars(
            "1 quarter and 3 pennies"), Decimal('0.28'))
        self.assertEqual(convert_coins_to_dollars(
            "21 pennies and 17 dimes and 52 quarters"), Decimal('14.91'))
        self.assertEqual(convert_coins_to_dollars(
            "95 dimes and 73 quarters and 22 nickels and 36 pennies"), Decimal('29.21'))
        self.assertEqual(convert_coins_to_dollars(
            "1 nickel and 17 quarters"), Decimal('4.30'))
        self.assertEqual(convert_coins_to_dollars(
            "21 nickels and 15 pennies"), Decimal('1.20'))
        self.assertEqual(convert_coins_to_dollars(
            "1 dime and 1 nickel and 1 penny and 1 quarter"), Decimal('0.41'))

        # Test additional combinations
        self.assertEqual(convert_coins_to_dollars(
            "100 pennies"), Decimal('1.00'))
        self.assertEqual(convert_coins_to_dollars(
            "10 nickels and 10 pennies"), Decimal('0.60'))
        self.assertEqual(convert_coins_to_dollars(
            "3 quarters and 2 dimes and 1 nickel"), Decimal('1.00'))

    def test_convert_coins_to_dollars_whitespace_handling(self):
        """Test handling of extra whitespace."""
        self.assertEqual(convert_coins_to_dollars(
            "  1 penny  "), Decimal('0.01'))
        self.assertEqual(convert_coins_to_dollars(
            "1 penny   and   2 nickels"), Decimal('0.11'))
        self.assertEqual(convert_coins_to_dollars(
            "  4  dimes  and  7  quarters  "), Decimal('2.15'))
        self.assertEqual(convert_coins_to_dollars(
            "1 penny and    2 nickels"), Decimal('0.11'))

    def test_invalid_inputs(self):
        """Test handling of various invalid inputs."""
        # Test empty input
        with self.assertRaises(ValueError):
            convert_coins_to_dollars("")

        # Test None input
        with self.assertRaises(ValueError):
            convert_coins_to_dollars(None)

        # Test invalid denomination
        with self.assertRaises(ValueError):
            convert_coins_to_dollars("1 dollar")

        # Test invalid quantity (non-numeric)
        with self.assertRaises(ValueError):
            convert_coins_to_dollars("one penny")

        # Test negative quantity
        with self.assertRaises(ValueError):
            convert_coins_to_dollars("-1 penny")

        # Test invalid format (missing quantity)
        with self.assertRaises(ValueError):
            convert_coins_to_dollars("penny")

        # Test invalid format (missing denomination)
        with self.assertRaises(ValueError):
            convert_coins_to_dollars("1")

        # Test invalid format (too many words)
        with self.assertRaises(ValueError):
            convert_coins_to_dollars("1 shiny penny")

    def test_format_as_dollars(self):
        """Test the format_as_dollars function."""
        # Test various decimal values
        self.assertEqual(format_as_dollars(Decimal('0')), "0.00")
        self.assertEqual(format_as_dollars(Decimal('0.1')), "0.10")
        self.assertEqual(format_as_dollars(Decimal('0.01')), "0.01")
        self.assertEqual(format_as_dollars(Decimal('1.0')), "1.00")
        self.assertEqual(format_as_dollars(Decimal('1.5')), "1.50")
        self.assertEqual(format_as_dollars(Decimal('1.23')), "1.23")
        self.assertEqual(format_as_dollars(Decimal('10.005')),
                         "10.00")  # Tests rounding
        self.assertEqual(format_as_dollars(Decimal('99.999')),
                         "100.00")  # Tests rounding

        # Test handling float inputs (should convert to Decimal internally)
        self.assertEqual(format_as_dollars(0.1), "0.10")
        self.assertEqual(format_as_dollars(1.0), "1.00")

    def test_process_coin_statement(self):
        """Test the process_coin_statement function."""
        # Test valid cases
        self.assertEqual(process_coin_statement(
            "1 penny and 2 nickels"), "0.11")
        self.assertEqual(process_coin_statement(
            "4 dimes and 7 quarters"), "2.15")
        self.assertEqual(process_coin_statement(
            "  1 penny  and  2 nickels  "), "0.11")
        self.assertEqual(process_coin_statement(
            "1 dime and 1 nickel and 1 penny and 1 quarter"), "0.41")

        # Test error handling
        self.assertEqual(process_coin_statement(
            ""), "Error: Input cannot be empty")
        self.assertTrue(process_coin_statement("1 dollar").startswith("Error"))
        self.assertTrue(process_coin_statement(
            "one penny").startswith("Error"))


if __name__ == "__main__":
    unittest.main()
