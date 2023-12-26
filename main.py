import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
import time
def wait_for_seconds(seconds):
        time.sleep(seconds)