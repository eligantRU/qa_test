from time import time


def measure_time(func):
	def wrapper(*arg, **kw):
		t1 = time()
		result = func(*arg, **kw)
		t2 = time()
		return result, 1000 * (t2 - t1)
	return wrapper


def print_some_noise(func):
	def wrapper(*arg, **kw):
		print(10**10**2)
		result = func(*arg, **kw)
		print(42)
		return result
	return wrapper
