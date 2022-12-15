h,w = map(int, input().split())
ans = 0

for i in range(h):
    s = input()
    for j in s:
        if j == "#":
            ans += 1
            
print(ans)
    
