def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import datetime
def get_current_datetime():
        return datetime.datetime.now()