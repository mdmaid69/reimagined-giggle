  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()