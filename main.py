numbers = [1, 2, 3, 4, 5]
print("Max:", max(numbers))
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()