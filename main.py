def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import time
def get_current_time():
        return time.ctime()