print([x**2 for x in range(10)])
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())