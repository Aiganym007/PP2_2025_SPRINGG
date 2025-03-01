import os
path = input()
access = {
    'exist': os.path.exists(path),
    'read': os.access(path, os.R_OK),
    'write': os.access(path, os.W_OK),
    'exec': os.access(path, os.X_OK)
}
if access['exist'] and access['read'] and access['write'] and access['exec']:
    print("Full access")