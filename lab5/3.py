import re
s = input("Enter a string: ")
m = re.findall(r'[a-z]+_[a-z]+', s)
if m:
    print(m)
else:
    print("error")