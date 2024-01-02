def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
def find_unique_words(sentence):
        return set(sentence.split())