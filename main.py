  def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())