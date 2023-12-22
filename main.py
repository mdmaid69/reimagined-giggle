import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)