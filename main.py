import datetime
def get_current_datetime():
        return datetime.datetime.now()
def count_words(sentence):
        return len(sentence.split())