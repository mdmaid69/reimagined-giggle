import sys
def exit_program():
        sys.exit()
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)