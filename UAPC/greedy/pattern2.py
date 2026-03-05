import heapq
arr.sort()  # by start
heap = []
for s, e in arr:
    if heap and heap[0] <= s:
        heapq.heapreplace(heap, e)
    else:
        heapq.heappush(heap, e)
# “Minimum number of ‘things’ to cover all intervals?”