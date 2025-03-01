import os
a = list(map(int, input().split()))
with open(r'C:\Users\Gulistan\Desktop\PP2_2025_SPRING\lab6\dir_files\text.txt', 'w') as file:
    for i in a:
        file.write(str(i)+"\n")