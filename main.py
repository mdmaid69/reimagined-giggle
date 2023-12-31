import datetime
def get_today_date():
        return datetime.date.today()
def find_unique_words(sentence):
        return set(sentence.split())