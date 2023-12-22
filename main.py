import datetime
def get_current_datetime():
        return datetime.datetime.now()
def find_unique_words(sentence):
        return set(sentence.split())