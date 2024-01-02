import time
def wait_for_seconds(seconds):
        time.sleep(seconds)
import glob
def find_files(pattern):
        return glob.glob(pattern)