"""
Unit tests for the Coin Converter program.
"""

import unittest
from coin_converter import convert_coins_to_dollars, format_as_dollars, process_coin_statement


class TestCoinConverter(unittest.TestCase):

    def test_convert_coins_to_dollars(self):
        """Test the convert_coins_to_dollars function with various inputs."""
        # Test basic cases
        self.assertEqual(convert_coins_to_dollars("1 penny"), 0.01)
        self.assertEqual(convert_coins_to_dollars("1 nickel"), 0.05)
        self.assertEqual(convert_coins_to_dollars("1 dime"), 0.10)
        self.assertEqual(convert_coins_to_dollars("1 quarter"), 0.25)

        # Test plural forms
        self.assertEqual(convert_coins_to_dollars("2 pennies"), 0.02)
        self.assertEqual(convert_coins_to_dollars("2 nickels"), 0.10)
        self.assertEqual(convert_coins_to_dollars("2 dimes"), 0.20)
        self.assertEqual(convert_coins_to_dollars("2 quarters"), 0.50)

        # Test combinations
        self.assertEqual(convert_coins_to_dollars(
            "1 penny and 2 nickels"), 0.11)
        self.assertEqual(convert_coins_to_dollars(
            "4 dimes and 7 quarters"), 2.15)
        self.assertEqual(convert_coins_to_dollars(
            "1 quarter and 3 pennies"), 0.28)
        self.assertEqual(convert_coins_to_dollars(
            "21 pennies and 17 dimes and 52 quarters"), 14.91)
        self.assertEqual(convert_coins_to_dollars(
            "95 dimes and 73 quarters and 22 nickels and 36 pennies"), 29.21)
        self.assertEqual(convert_coins_to_dollars(
            "1 nickel and 17 quarters"), 4.30)
        self.assertEqual(convert_coins_to_dollars(
            "21 nickels and 15 pennies"), 1.20)
        # Expected to fail
        self.assertEqual(convert_coins_to_dollars(
            "1 dime and 1 nickel and 1 penny and 1 quarter"), 0.41)

    def test_invalid_inputs(self):
        """Test handling of invalid inputs."""
        # Test invalid denomination
        with self.assertRaises(ValueError):
            convert_coins_to_dollars("1 dollar")

        # Test invalid quantity
        with self.assertRaises(ValueError):
            convert_coins_to_dollars("one penny")

    def test_format_as_dollars(self):
        """Test the format_as_dollars function."""
        self.assertEqual(format_as_dollars(0.1), "0.10")
        self.assertEqual(format_as_dollars(1.0), "1.00")
        self.assertEqual(format_as_dollars(1.5), "1.50")
        self.assertEqual(format_as_dollars(1.23), "1.23")

    def test_process_coin_statement(self):
        """Test the process_coin_statement function."""
        self.assertEqual(process_coin_statement(
            "1 penny and 2 nickels"), "0.11")
        self.assertEqual(process_coin_statement(
            "4 dimes and 7 quarters"), "2.15")

        # Test error handling
        self.assertTrue(process_coin_statement("1 dollar").startswith("Error"))


if __name__ == "__main__":
    unittest.main()
