import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()