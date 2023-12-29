sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()