import os
print(os.getcwd())
import glob
def find_files(pattern):
        return glob.glob(pattern)