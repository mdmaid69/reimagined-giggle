import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
text = "Hello, world!"
print("Uppercase:", text.upper())