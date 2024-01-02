def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
def greet(name):
        print(f"Hello, {name}!")