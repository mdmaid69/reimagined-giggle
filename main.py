n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))