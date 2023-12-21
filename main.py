i = 0
while i < 5:
        print(i)
        i += 1
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())