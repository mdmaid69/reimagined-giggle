  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2