import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)