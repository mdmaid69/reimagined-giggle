import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h