def convert_to_hex(n):
        return hex(n)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())