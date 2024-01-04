  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity