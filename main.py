import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])