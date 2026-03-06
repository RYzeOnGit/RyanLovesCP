n, p = map(int, input().split())
trophies = [list(map(int, input().split())) for _ in range(n)]

uniq = set()  # set of permutations (as tuples of original row indices)

for j in range(p):
    # Collect (value, original_row_index) for column j
    col = [(trophies[i][j], i) for i in range(n)]
    # If any duplicates in values, this column can never be strictly increasing
    if len({v for v, _ in col}) != n:
        continue
    # The unique permutation that makes column j strictly increasing
    col.sort()  # sort by value
    order = tuple(idx for _, idx in col)
    uniq.add(order)

print(len(uniq))