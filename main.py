  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
def calculate_energy(mass, c=3*10**8):
        return mass * c**2