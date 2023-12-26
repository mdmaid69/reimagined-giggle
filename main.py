for i in range(10): print(i)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())