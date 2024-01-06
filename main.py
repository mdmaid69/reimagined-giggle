def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
def is_odd(n):
        return n % 2 != 0