import glob
def find_files(pattern):
        return glob.glob(pattern)
import time
def wait_for_seconds(seconds):
        time.sleep(seconds)