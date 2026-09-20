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
# Ask until the user enters exactly 12 numbers
while True:
    upc = input("Enter a 12-digit UPC: ")

    if len(upc) == 12 and upc.isdigit():
        break

    print("Error: Please enter exactly 12 digits.\n")


# Separate the UPC into the first 11 digits and check digit
first_eleven = upc[:11]
provided_check_digit = int(upc[11])

print()
print(f"The first 11 digits are '{first_eleven}'.")
print(f"The provided check digit is '{provided_check_digit}'.")

print()
print("Calculating...")

# Call the function
expected_check_digit = find_UPC(first_eleven)

print(f"The expected check digit is {expected_check_digit}.")
print()

# Compare the calculated digit with the user's 12th digit
if expected_check_digit == provided_check_digit:
    print("This is a VALID UPC.")
else:
    print("This is an INVALID UPC.")