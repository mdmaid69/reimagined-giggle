n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())