import datetime
def get_today_date():
        return datetime.date.today()
def count_words(sentence):
        return len(sentence.split())