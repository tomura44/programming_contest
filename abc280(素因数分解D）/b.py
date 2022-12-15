n = int(input())
s = [0] + list(map(int, input().split()))
a = []


for i in range(n):
    a.append(s[i+1] - s[i])
    
print(*a)
    
