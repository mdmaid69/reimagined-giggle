import sys
print(sys.version)
import glob
def find_files(pattern):
        return glob.glob(pattern)