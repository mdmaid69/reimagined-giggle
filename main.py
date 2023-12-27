n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()