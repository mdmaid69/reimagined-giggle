def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b