import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()