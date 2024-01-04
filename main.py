def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])