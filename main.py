  def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
        return False
        return True
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)