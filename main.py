  def convert_to_binary(n):
        return bin(n)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())