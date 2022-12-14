s = input()

if len(s) != 8 or s[0].isdigit() or s[7].isdigit() or not s[1:7].isdecimal() or s[1] == '0':
    print("No")
else:
    print("Yes")
