def count_words(sentence):
        return len(sentence.split())
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))