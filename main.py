def is_even(n):
        return n % 2 == 0
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())