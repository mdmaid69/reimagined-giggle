sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)