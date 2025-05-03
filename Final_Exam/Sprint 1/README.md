# Coin Converter - Sprint 1

Please see the [exam scope](../IT%203883%20Final%20Exam.pdf) for problem
description and other details.

# Design

With the [user stories below](#user-stories), core components of this application
are:

* Input parser that converts sentences to structured data
* Denomination recognizer that maps coin names to their numerical value. This
will be implemented using a dictionary.

    ```json
    {
        "penny": 0.01,
        "pennies": 0.01,
        "nickel": 0.05,
        "nickels": 0.05,
        "dime": 0.10,
        "dimes": 0.10,
        "quarter": 0.25,
        "quarters": 0.25
    }
    ```

* Calculator to keep tracking of running total
* A formatter to present results in the desired format.

# Deliverables

For Sprint 1, I choose the following deliverables:

* Source code with comments (required)
* A set of [user stories](#user-stories) that include details about user input and output.
* A [flow chart](#flow-chart) showing each of the steps followed by the program
* A list of the [test cases](#test-cases) you ran and if they passed or failed

## User Stories

1. As a user, I want to input a sentence describing coins (e.g., "1 penny and 2
nickels") so that the system can understand my coin collection.

2. As a user, I want the system to recognize different coin denominations (pennies,
nickels, dimes, quarters) so that I can describe various combinations of coins.

3. As a user, I want the system to handle both singular and plural forms of coin
names (e.g., "penny" vs "pennies") so that I can use natural language.

4. As a user, I want the system to calculate the total dollar value of my coins
so that I know how much money I have.

5. As a user, I want the output formatted in dollars (e.g., $0.41) so that it's
easy to understand.

6. As a user, I want the system to handle any order of coin denominations in my
input (e.g., "1 quarter and 3 pennies" or "3 pennies and 1 quarter") so that I
don't have to remember a specific format.

## Flow chart

[![](https://mermaid.ink/img/pako:eNptkE1zmzAQhv-KRpdciAcM-INDO4mxGydxp5P00oIPqrXBmoJExSqNy_i_R8iQOp3qpN193nc_WrpTHGhCn0r1e7dnGsnXNJfEvqvsEW28JZeXH8h19oXpBoiQtUHSoBay2J64awcssse6FEOJ_DiQCyb5Rc8sHJNmK6UJsN2eNFBUINEj8IKa7ZD8MkyiwAOxKsJBqkpIhkLJ3iF1Dst23byrkmdWCv7xeIKWFiLfoHHsKlso-Qx2o3cCVJ3GwPZM8lk5xafsAdBoSUBrO2gFTcOKAVw55CbbmBJFXR7-Tmx3_XekN_sbp1pnV5x3nbWRsjsPKmRlj6wdcttulIbhLs2w0e35RulZrh_5rjtpxfDkSJi9jipLpgmrlJHYt7hz7P2w3v-Qe4dssqXkNkM9WmjBaYLagEcrsD26kLYdnVPcQwU5TeyXM_0zp7k8Wk3N5HelqkGmlSn2NHliZWMjU3OGkApWaFa9ZTVIDnrRTUKTYBaFzoUmLX2hySwMR_58Es0n8Wzsh8HYoweazP1RMI79OIz8eDoJpuOjR_-4tv5oNo3m3QuieBJOo-j4Cqpo5ZU?type=png)](https://mermaid.live/edit#pako:eNptkE1zmzAQhv-KRpdciAcM-INDO4mxGydxp5P00oIPqrXBmoJExSqNy_i_R8iQOp3qpN193nc_WrpTHGhCn0r1e7dnGsnXNJfEvqvsEW28JZeXH8h19oXpBoiQtUHSoBay2J64awcssse6FEOJ_DiQCyb5Rc8sHJNmK6UJsN2eNFBUINEj8IKa7ZD8MkyiwAOxKsJBqkpIhkLJ3iF1Dst23byrkmdWCv7xeIKWFiLfoHHsKlso-Qx2o3cCVJ3GwPZM8lk5xafsAdBoSUBrO2gFTcOKAVw55CbbmBJFXR7-Tmx3_XekN_sbp1pnV5x3nbWRsjsPKmRlj6wdcttulIbhLs2w0e35RulZrh_5rjtpxfDkSJi9jipLpgmrlJHYt7hz7P2w3v-Qe4dssqXkNkM9WmjBaYLagEcrsD26kLYdnVPcQwU5TeyXM_0zp7k8Wk3N5HelqkGmlSn2NHliZWMjU3OGkApWaFa9ZTVIDnrRTUKTYBaFzoUmLX2hySwMR_58Es0n8Wzsh8HYoweazP1RMI79OIz8eDoJpuOjR_-4tv5oNo3m3QuieBJOo-j4Cqpo5ZU)

*This chart was generated using [mermaid](https://mermaid.js.org/). An image
version is available [here](./S1_D2_Flowchart.png)*.

## Test Cases

| Test                                                   | Pass/Fail | Note                                                                                                                       |
|--------------------------------------------------------|-----------|----------------------------------------------------------------------------------------------------------------------------|
| 1 penny                                                | Pass      |                                                                                                                            |
| 1 nickel                                               | Pass      |                                                                                                                            |
| 1 dime                                                 | Pass      |                                                                                                                            |
| 1 quarter                                              | Pass      |                                                                                                                            |
| 2 pennies                                              | Pass      |                                                                                                                            |
| 2 nickels                                              | Pass      |                                                                                                                            |
| 2 dimes                                                | Pass      |                                                                                                                            |
| 2 quarters                                             | Pass      |                                                                                                                            |
| 1 penny and 2 nickels                                  | Pass      |                                                                                                                            |
| 4 dimes and 7 quarters                                 | Pass      |                                                                                                                            |
| 1 quarter and 3 pennies                                | Pass      |                                                                                                                            |
| 21 pennies and 17 dimes and 52 quarters                | Pass      |                                                                                                                            |
| 95 dimes and 73 quarters and 22 nickels and 36 pennies | Pass      |                                                                                                                            |
| 1 nickel and 17 quarters                               | Pass      |                                                                                                                            |
| 21 nickels and 15 pennies                              | Pass      |                                                                                                                            |
| 1 dime and 1 nickel and 1 penny and 1 quarter          | **Fail**  | `AssertionError: 0.41000000000000003 != 0.41`<br>because Python represents decimal numbers exactly which impact arithmetic |

*Generated using [Tables Generator](https://www.tablesgenerator.com/markdown_tables)*
