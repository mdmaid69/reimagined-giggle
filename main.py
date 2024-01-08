import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)