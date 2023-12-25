import collections
def count_elements(iterable):
        return collections.Counter(iterable)
text = "Hello, world!"
print("Words:", len(text.split()))