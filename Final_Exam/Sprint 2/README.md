# Coin Converter - Sprint 2

## Design Improvements

After reviewing the test cases and initial implementation, I identified additional requirements:

* Handle extra spaces in the input
* Handle variations in formatting
* Validate input thoroughly and provide meaningful error messages

### Correctly handling decimal arithmetic
A problem testing revealed in Sprint 1 is that many decimal numbers do not have
exact representations in binary floating-point. As such, you can get unexpected
results during arithmetic operations. For example,
"1 dime and 1 nickel and 1 penny and 1 quarter" (`0.10 + 0.05 + 0.01 + 0.25`)
does not equal `0.41` exactly. This is because Python represents decimal
numbers exactly, which carries over into arithmetic operations.

To fix this, I use the decimal module which provides more intuitive
arithmetics.

## Test Cases

| Test                                                   | Pass/Fail | Note |
|--------------------------------------------------------|-----------|------|
| 1 penny                                                | Pass      |      |
| 1 nickel                                               | Pass      |      |
| 1 dime                                                 | Pass      |      |
| 1 quarter                                              | Pass      |      |
| 5 pennies                                              | Pass      |      |
| 10 nickels                                             | Pass      |      |
| 20 dimes                                               | Pass      |      |
| 4 quarters                                             | Pass      |      |
| 2 pennies                                              | Pass      |      |
| 2 nickels                                              | Pass      |      |
| 2 dimes                                                | Pass      |      |
| 2 quarters                                             | Pass      |      |
| 1 penny and 2 nickels                                  | Pass      |      |
| 4 dimes and 7 quarters                                 | Pass      |      |
| 1 quarter and 3 pennies                                | Pass      |      |
| 21 pennies and 17 dimes and 52 quarters                | Pass      |      |
| 95 dimes and 73 quarters and 22 nickels and 36 pennies | Pass      |      |
| 1 nickel and 17 quarters                               | Pass      |      |
| 21 nickels and 15 pennies                              | Pass      |      |
| 1 dime and 1 nickel and 1 penny and 1 quarter          | Pass      |      |
| 100 pennies                                            | Pass      |      |
| 10 nickels and 10 pennies                              | Pass      |      |
| 3 quarters and 2 dimes and 1 nickel                    | Pass      |      |
| 1 penny                                                | Pass      |      |
| 1 penny   and   2 nickels                              | Pass      |      |
| 4  dimes  and  7  quarters                             | Pass      |      |
| 1 penny and    2 nickels                               | Pass      |      |

*Generated using [Tables Generator](https://www.tablesgenerator.com/markdown_tables)*
