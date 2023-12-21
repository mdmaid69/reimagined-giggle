def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
def find_unique_words(sentence):
        return set(sentence.split())