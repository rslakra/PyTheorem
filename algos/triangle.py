#
# Author: Rohtash Lakra
#

def print_triangle(max_row):
    """Prints a triangle of numbers
    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5
    """
    for i in range(max_row):
        for j in range(i + 1):
            print(j + 1, end=" ")
        print()


def print_perfect_triangle(max_row):
    """Prints a perfect triangle of numbers
    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5
    """
    current = 1
    row = 1
    
    while True:
        row_sum = sum(range(current, current + row))
        if current + row - 1 > max_row:
            break
        
        for i in range(row):
            print(current, end=" ")
            current += 1
        
        print()
        row += 1


def print_line(label: str, length: int = 80):
    print(f"<{label}>".center(length, "-"))


def print_number_triangle(max_number):
    """
    Prints a triangular arrangement of numbers up to the largest triangular number
    less than or equal to max_number.
    """
    current_number = 1
    row_length = 1
    
    while True:
        # Calculate the sum of numbers in the current row
        sum_in_row = sum(range(current_number, current_number + row_length))
        
        # Check if adding the next row would exceed max_number
        if current_number + row_length - 1 > max_number:
            break
        
        # Print the numbers in the current row
        for i in range(row_length):
            print(current_number, end=" ")
            current_number += 1
        print()  # Move to the next line for the next row
        row_length += 1


def print_centered_number_triangle(max_rows):
    """
    Prints a triangular pattern of numbers centered with '1' at the base.
    """
    current_number = 1
    # Calculate the maximum width of the triangle (for the last row)
    # The last row will contain numbers up to max_rows, roughly, so its length will be max_rows * 2 - 1
    max_width = 2 * max_rows - 1
    
    for row_num in range(1, max_rows + 1):
        # Calculate the number of leading spaces needed for centering
        leading_spaces = max_rows - row_num
        
        # Print leading spaces
        end_space = "  " if row_num < 5 else " "
        print(" " * leading_spaces, end=end_space)
        
        # Print the numbers for the current row
        for i in range(1, row_num + 1):
            print(current_number, end=end_space)
            current_number += 1
        print()  # Move to the next line for the next row


print_line("print_triangle")
print_triangle(5)
print()
print_line("print_perfect_triangle")
print_perfect_triangle(5)
print_line("print_number_triangle")
print_number_triangle(100)
print_line("print_centered_number_triangle")
print_centered_number_triangle(10)
