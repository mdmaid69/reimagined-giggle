import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)