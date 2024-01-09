def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
n = 10
print("Square numbers:", [x**2 for x in range(n)])