"""
Greedy Algorithm Example
Problem: Activity Selection (or similar scheduling problem)
Given n activities with start and end times, find maximum number of activities
that can be performed by a single person.
"""

def solve_activity_selection():
    """
    Greedy approach: Always pick the activity that ends earliest
    Time: O(n log n) due to sorting
    """
    n = int(input())
    activities = []
    
    for _ in range(n):
        start, end = map(int, input().split())
        activities.append((start, end))
    
    # Sort by end time
    activities.sort(key=lambda x: x[1])
    
    count = 0
    last_end = -1
    
    for start, end in activities:
        if start >= last_end:
            count += 1
            last_end = end
    
    print(count)

if __name__ == "__main__":
    solve_activity_selection()

