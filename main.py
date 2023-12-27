def find_unique_words(sentence):
        return set(sentence.split())
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())