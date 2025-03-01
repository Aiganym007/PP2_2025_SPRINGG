import os
path = input()
if os.path.exists(path):
    print(os.path.basename(path), os.path.dirname(path))
    