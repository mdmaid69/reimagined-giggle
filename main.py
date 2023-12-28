def greet(name):
        print(f"Hello, {name}!")
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())