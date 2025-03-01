import os
dir=[]
file = []
path = input()
for i in os.listdir(path):
    if os.path.isdir(os.path.join(path, i)):
        dir.append(i)
for i in os.listdir(path):
    if os.path.isfile(os.path.join(path,i)):
        file.append(i)
print(dir)
print(file)
