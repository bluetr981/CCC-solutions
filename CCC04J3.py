n = int(input())
m = int(input())
arr = []
g = []
for i in range(n):
    a = input()
    arr.append(a)
for i in range(m):
    b = input()
    g.append(b)
for e in range(len(arr)):
    for i in range(len(g)):
        print(arr[e], "as", g[i])
