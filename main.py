def find_unique_words(sentence):
        return set(sentence.split())
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b