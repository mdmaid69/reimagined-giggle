import datetime
print(datetime.datetime.now())
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())