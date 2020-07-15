def resolve(k, b):
	if k == 0:
		raise Exception("k cannot be zero")
	return -b / k


class SuperLinearResolver:
	__args = None

	def __init__(self, args):
		self.__args = args
