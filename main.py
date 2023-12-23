def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
n = 10
print("Powers of 2:", [2**x for x in range(n)])