import sys

print("Script name:", sys.argv)
if len(sys.argv) > 1:
    print("Arguments:", sys.argv[1:])

import os
print(os.listdir())