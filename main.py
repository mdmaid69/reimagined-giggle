def reverse_string(s):
        return s[::-1]
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())