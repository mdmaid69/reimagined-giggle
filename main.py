import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import time
def wait_for_seconds(seconds):
        time.sleep(seconds)