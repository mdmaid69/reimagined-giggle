  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))