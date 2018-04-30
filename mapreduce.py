#Range class with step

class range_iterator:
  def __init__(self, a, b, ss):
	self.a = a
	self.b = b
	self.ss = ss

  def __iter__(self):
	return self

  def __next__(self):
	if self.a > self.b:
	  raise StopIteration
	a = self.a
	self.a = self.a + self.ss
	return a

"""
b = range_iterator(2,5,1)
b_iter = iter(b)
assert hasattr(b, "__iter__")
assert hasattr(b, "__next__")
print(next(b_iter))
print(next(b_iter))
print(next(b_iter))
print(next(b_iter))
b = range_iterator(2,5,1)
print(list(b))
"""
from functools import reduce
def RMSE(actual, expected):
  c = map(lambda x, y: (y-x) ** 2, actual, expected)
  return (reduce(lambda x, y: x + y, c, 0)/len(actual)) ** (1/2)

print(RMSE([1,2], [3,4]))


def stddev(input):
  mean = reduce(lambda x, y: x + y, input, 0) / len(input)
  print(list(map(lambda x: (x - mean) ** 2, input)))
  return (reduce(lambda x, y: x + y, map(lambda x: (x - mean) ** 2, input), 0) / (len(input) - 1)) ** (1/2)

print(stddev([10,2,38,23,38,23,21]))
