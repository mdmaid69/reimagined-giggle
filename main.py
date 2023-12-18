import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)