import sys
def exit_program():
        sys.exit()
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)