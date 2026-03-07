"""
Kattis I/O Helper
Standard input/output patterns for Kattis problems
"""

import sys

# Pattern 1: Read until EOF
def read_until_eof():
    """Read all lines until EOF"""
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        # Process line
        process(line)

# Pattern 2: Read n test cases
def read_test_cases():
    """Read n test cases"""
    n = int(input())
    for _ in range(n):
        # Read test case
        data = input().split()
        process_test_case(data)

# Pattern 3: Read until specific sentinel
def read_until_sentinel(sentinel="0"):
    """Read until sentinel value"""
    while True:
        line = input().strip()
        if line == sentinel:
            break
        process(line)

# Pattern 4: Read multiple values per line
def read_multiple_values():
    """Read multiple values from single line"""
    n, m, k = map(int, input().split())
    # Process n, m, k

# Pattern 5: Read matrix/grid
def read_grid(rows, cols):
    """Read a grid of characters or numbers"""
    grid = []
    for _ in range(rows):
        row = list(input().strip())
        grid.append(row)
    return grid

# Pattern 6: Fast I/O for large inputs
def fast_io():
    """Use sys.stdin for faster I/O"""
    data = sys.stdin.read().split()
    # Process data
    i = 0
    while i < len(data):
        n = int(data[i])
        i += 1
        # Process n items
        items = [int(data[i+j]) for j in range(n)]
        i += n

# Pattern 7: Read with multiple lines per test case
def read_multiline_test_case():
    """Read test case spanning multiple lines"""
    n = int(input())
    lines = []
    for _ in range(n):
        lines.append(input().strip())
    # Process lines

# Pattern 8: Output formatting
def output_formatting():
    """Common output patterns"""
    # Single integer
    print(result)
    
    # Multiple values on one line
    print(a, b, c)
    
    # One value per line
    for item in results:
        print(item)
    
    # Formatted output
    print(f"Case {i}: {result}")
    print("Case {}: {}".format(i, result))

# Example: Complete problem template
def example_problem():
    """Template for typical Kattis problem"""
    # Read input
    n = int(input())
    arr = list(map(int, input().split()))
    
    # Solve
    result = solve(arr)
    
    # Output
    print(result)

def solve(arr):
    # Your solution
    return sum(arr)

if __name__ == "__main__":
    example_problem()

