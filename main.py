import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))