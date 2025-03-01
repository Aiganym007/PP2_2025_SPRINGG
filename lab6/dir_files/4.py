import os
a = 0
with open(r'C:\Users\Gulistan\Desktop\PP2_2025_SPRING\lab6\dir_files\text.txt', 'r') as file:
    for line in file:
        a += 1
print(a)