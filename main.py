import datetime
def get_current_date():
        return datetime.date.today()
def count_words(sentence):
        return len(sentence.split())