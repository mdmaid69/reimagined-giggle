import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))