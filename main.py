import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()