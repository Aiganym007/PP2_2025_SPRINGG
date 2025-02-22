import re
s = "ab abb abbb a ac abc"
m = re.findall(r'ab{2,3}', s)
if m:
    print(m)
else:
    print("error")