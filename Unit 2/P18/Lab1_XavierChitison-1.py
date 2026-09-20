"""
Program Name: UPC Validator
Author: Xavier Chitison
Purpose: This program asks the user for a 12-digit UPC-A code.
         It calculates the expected check digit using a function
         and determines whether the UPC entered is valid or invalid.
Starter Code: No starter code was used.
Date: September 20, 2026
"""


def find_UPC(first_eleven):
    """Calculate and return the check digit for the first 11 UPC digits."""

    odd_sum = 0
    even_sum = 0

    # Add digits in the odd positions: 1, 3, 5, 7, 9, 11
    for i in range(0, 11, 2):
        odd_sum += int(first_eleven[i])

    # Multiply the odd-position sum by 3
    odd_sum = odd_sum * 3

    # Add digits in the even positions: 2, 4, 6, 8, 10
    for i in range(1, 11, 2):
        even_sum += int(first_eleven[i])

    # Add both totals together
    total = odd_sum + even_sum

    # Find the check digit
    check_digit = (10 - (total % 10)) % 10

    return check_digit
