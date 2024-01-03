n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())