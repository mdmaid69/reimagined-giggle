import datetime
def get_today_date():
        return datetime.date.today()
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))