def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
def count_characters(sentence):
        return len(sentence)