import sys
def add_to_python_path(path):
        sys.path.append(path)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())