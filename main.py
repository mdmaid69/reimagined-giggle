  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2