sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)