def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
def calculate_energy(mass, c=3*10**8):
        return mass * c**2