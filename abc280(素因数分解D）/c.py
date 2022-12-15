s = input() + "W"
t = input()

for i in range(len(t)):
    if s[i] == t[i]:
        continue
    print(i+1)
    exit