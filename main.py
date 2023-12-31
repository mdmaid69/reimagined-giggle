def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])