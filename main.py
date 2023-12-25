import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
text = "Hello, world!"
print("Uppercase:", text.upper())