VERY_LARGE_NUMBER = 10**7


def gen_1():
	return [i for i in range(0, VERY_LARGE_NUMBER + 1)]


def gen_2():
	result = []
	for i in range(0, VERY_LARGE_NUMBER + 1):
		result.append(i)
	return result


def find_1(arr):
	return arr.index(VERY_LARGE_NUMBER)


def find_2(arr):
	return [index for index, el in enumerate(arr) if el == VERY_LARGE_NUMBER][0]


def find_3(arr):
	for index, el in enumerate(arr):
		if el == VERY_LARGE_NUMBER:
			return index
	raise Exception("catch me if u can")
