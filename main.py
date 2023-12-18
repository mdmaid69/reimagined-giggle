def find_unique_words(sentence):
        return set(sentence.split())
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))