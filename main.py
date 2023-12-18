  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
  def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
        return False
        return True