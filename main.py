def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())