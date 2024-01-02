import time
def get_current_time():
        return time.ctime()
def count_words(sentence):
        return len(sentence.split())