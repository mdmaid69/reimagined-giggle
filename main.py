import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()