import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)