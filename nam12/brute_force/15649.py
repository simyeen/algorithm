from itertools import permutations

n, m = map(int, input().split())
arr = []
for i in range(1, n+1):
    arr.append(i)

for c in permutations(arr, m):
    print(" ".join(map(str, c)))
