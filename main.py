def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import time
def wait_for_seconds(seconds):
        time.sleep(seconds)