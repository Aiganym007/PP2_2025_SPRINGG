import os
with open(r"C:\Users\Gulistan\Desktop\PP2_2025_SPRING\A.txt", 'r') as src, open(r'C:\Users\Gulistan\Desktop\PP2_2025_SPRING\lab6\dir_files\text.txt', 'w') as dest:
    dest.write(src.read())
    