def remove_duplicates(lst):
        return list(set(lst))
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))