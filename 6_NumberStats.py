class NumberStats:
  def __init__(self):
    self.num_list = []

  def add_number(self, num):
    self.num_list.append(num)

  def count_numbers(self):
    return len(self.num_list)

stats = NumberStats()
stats.add_number(3)
stats.add_number(5)
stats.add_number(1)
stats.add_number(2)
print("Numbers added:", stats.count_numbers())