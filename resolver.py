# TODO: объяснить расход памяти и время работы; предложить оптимизации


import src.LinearResolver as Resolver


def main():
	args = [(k, 1) for k in range(0, 1000, 2)]

	resolver = Resolver.LinearResolver("R2D2")
	for k, b in args:
		print(resolver.resolve(k, b))


if __name__ == "__main__":
	main()
