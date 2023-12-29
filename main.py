def find_unique_words(sentence):
        return set(sentence.split())
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b