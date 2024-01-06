def convert_to_octal(n):
        return oct(n)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())