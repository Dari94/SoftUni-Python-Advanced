from collections import deque

n = int(input())
pumps = deque ()
for _ in range(n):
    pump = [int(x) for x in input().split()]
    pumps.append(pump)

for i in range(n):
    current = pumps.popleft()