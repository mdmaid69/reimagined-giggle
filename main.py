import sys
def exit_program():
        sys.exit()
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)