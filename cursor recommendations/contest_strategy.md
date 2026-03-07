# UAPC 2026 Division 2 - Contest Strategy Guide

## Pre-Contest Preparation

### 1. Know Your Tools
- **Language**: Python 3 (most common for Division 2)
- **Platform**: Kattis (familiarize yourself with submission format)
- **Time Limit**: 4 hours
- **Team Size**: 1-3 members

### 2. Template Preparation
- Have your I/O template ready
- Pre-write common algorithms (BFS, DFS, sorting, etc.)
- Know your math utilities (GCD, prime checking, etc.)

### 3. Practice Strategy
- Solve past UAPC Division 2 problems (2022-2025)
- Focus on problems you can solve in 30-60 minutes
- Practice reading problems quickly and identifying patterns

## Contest Day Strategy

### 1. Problem Reading (First 15 minutes)
- **Read ALL problems** before starting
- Rank problems by difficulty (easy → hard)
- Identify problem types:
  - Greedy
  - Graph traversal
  - Dynamic programming
  - Math/Number theory
  - String manipulation
  - Array problems

### 2. Problem Selection
- Start with easiest problems first
- Don't spend more than 30 minutes on a problem initially
- If stuck, move to next problem and come back later
- Division 2 problems are usually solvable with standard algorithms

### 3. Coding Strategy

#### Time Management
- **Easy problems**: 15-30 minutes
- **Medium problems**: 30-60 minutes
- **Hard problems**: 60+ minutes (if time permits)

#### Common Patterns to Recognize
1. **Shortest Path** → BFS (unweighted) or Dijkstra (weighted)
2. **Connected Components** → DFS or Union-Find
3. **Maximum/Minimum** → Greedy or DP
4. **Counting** → DP or Combinatorics
5. **Range Queries** → Prefix sums or Segment tree
6. **String Matching** → KMP or simple iteration

### 4. Debugging Tips
- Test with sample inputs first
- Check edge cases:
  - Empty input
  - Single element
  - Maximum values
  - Negative numbers (if applicable)
- Print intermediate values if stuck
- Use assert statements for debugging

### 5. Submission Strategy
- **Test thoroughly** before submitting
- Check output format (spaces, newlines, etc.)
- If WA (Wrong Answer):
  - Re-read problem statement
  - Check edge cases
  - Verify algorithm correctness
- If TLE (Time Limit Exceeded):
  - Optimize algorithm complexity
  - Check for infinite loops
  - Consider faster I/O

## Common Mistakes to Avoid

1. **Not reading problem carefully** - Misunderstand constraints or requirements
2. **Overcomplicating** - Division 2 problems usually have straightforward solutions
3. **Not testing edge cases** - Always test boundary conditions
4. **Wrong output format** - Match exact format required
5. **Off-by-one errors** - Double-check indices
6. **Integer overflow** - Use appropriate data types
7. **Not managing time** - Don't get stuck on one problem

## Problem Type Cheat Sheet

### Greedy Problems
- Look for "maximum" or "minimum" with constraints
- Usually involve sorting first
- Examples: Activity selection, interval scheduling

### Graph Problems
- Look for "path", "connected", "reachable"
- BFS for shortest path
- DFS for connectivity/cycles
- Union-Find for connected components

### Dynamic Programming
- Look for "count ways", "maximum/minimum with constraints"
- Usually involves subproblems
- Common: Knapsack, LIS, grid paths

### Math Problems
- Look for patterns, formulas
- Prime numbers, GCD/LCM, modular arithmetic
- Combinatorics (nCr, permutations)

### String Problems
- Pattern matching, anagrams, palindromes
- Usually straightforward iteration or hashing

## Final Tips

1. **Stay calm** - Don't panic if stuck
2. **Read problem statement twice** - Ensure understanding
3. **Start simple** - Get easy problems done first
4. **Use your team** - Discuss approaches if in team
5. **Manage time** - Keep track of remaining time
6. **Submit early** - Don't wait until last minute
7. **Double-check** - Verify solution before submitting

## Resources During Contest
- Your templates folder
- Past solved problems
- Standard library documentation (if allowed)
- Calculator for math problems

## Post-Contest
- Review solutions after contest
- Learn from problems you couldn't solve
- Practice similar problems
- Update your templates with new patterns

Good luck! 🚀

