def count_words(sentence):
        return len(sentence.split())
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])