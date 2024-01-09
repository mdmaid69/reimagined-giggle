n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())