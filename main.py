def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import time
def get_time_since_epoch():
        return time.time()