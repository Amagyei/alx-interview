"""
0-main.py
Test the pascal_triangle function from 0-pascal_triangle.py
"""

# Import the pascal_triangle function from 0-pascal_triangle.py
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle in a formatted way
    """
    for row in triangle:
        print(f"[{', '.join(map(str, row))}]")  # Using f-string for formatting

if __name__ == "__main__":
    n = 5  # You can change this or add input handling for user-defined rows
    print(f"Pascal's Triangle with {n} rows:")
    print_triangle(pascal_triangle(n))

