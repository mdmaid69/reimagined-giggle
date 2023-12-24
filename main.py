import datetime
def get_today_date():
        return datetime.date.today()
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())