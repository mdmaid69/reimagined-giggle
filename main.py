import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
def find_unique_words(sentence):
        return set(sentence.split())