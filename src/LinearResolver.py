def resolve(k, b):
	if k == 0:
		raise Exception("k cannot be zero")
	return -b / k


class LinearResolver:
	__name = None

	def __init__(self, name):
		self.__name = name

	def resolve(self, k, b=0):
		try:
			return f"{self.__name} says root is {resolve(k, b)}"
		except:
			pass
