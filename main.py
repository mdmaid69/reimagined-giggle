def count_words(sentence):
        return len(sentence.split())
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())