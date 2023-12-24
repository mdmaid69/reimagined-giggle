def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))