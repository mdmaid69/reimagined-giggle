def find_common_elements(list1, list2):
        return set(list1) & set(list2)
  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)