def calculate_average(numbers):
        return sum(numbers) / len(numbers)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())