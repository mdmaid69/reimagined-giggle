import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)