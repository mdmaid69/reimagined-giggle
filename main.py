def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)