n = 10
print("Cube numbers:", [x**3 for x in range(n)])
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())