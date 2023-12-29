def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))