import re
s = input("Enter a string: ")
m = re.findall(r'a.*b$', s)
if m:
    print(m)
else:
    print("error")