def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])