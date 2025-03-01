import os
a = ["A", "B", "C", "D", "E", "F", "G", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "W", "X", "Y", "Z"]
for i in a:
    f = i + ".txt"
    with open(f, 'w') as file:
        file.write("hello")
