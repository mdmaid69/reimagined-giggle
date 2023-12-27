sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
import time
def get_time_since_epoch():
        return time.time()