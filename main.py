import sys
def exit_program():
        sys.exit()
import glob
def find_files(pattern):
        return glob.glob(pattern)