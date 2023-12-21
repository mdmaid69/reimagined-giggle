import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))