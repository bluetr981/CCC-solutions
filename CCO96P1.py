n = int(input())
for i in range(n):
    c = int(input())
    a = list(map(int, input().split()))
    r = sorted(a)
    ans = 0
    while a != r:
        for t in range(len(a)-1):
            if a[t] > a[t+1]:
                a[t], a[t+1] = a[t+1], a[t]
                ans += 1
    print("Optimal train swapping takes " + str(ans) + " swaps.")
