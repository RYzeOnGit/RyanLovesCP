from bisect import bisect_left, insort
# bisect_left(sorted_list, x) finds where x would be inserted to keep the list sorted.
# insort(sorted_list, x) inserts x into the list while keeping it sorted.
n, k = map(int, input().split())
activities = []
for _ in range(n):
    s, e = map(int, input().split())
    activities.append((e, s))      # store (end, start)

activities.sort()                  # greedy: earliest end first

ends = []                          # sorted end times of rooms currently used
ans = 0

for e, s in activities:
    # find first end >= s, so ends[idx-1] is the largest end < s
    idx = bisect_left(ends, s)

    if idx > 0:
        # reuse the room that ends latest but still < s
        ends.pop(idx - 1)
        insort(ends, e)
        ans += 1
    else:
        # no room ends < s, so we can only schedule if we have unused rooms
        if len(ends) < k:
            insort(ends, e)
            ans += 1

print(ans)