# TODO: объяснить, что это и зачем; сделать выводы
# Пример на базе list'ов, однако могут быть и иные контейнеры

from src.decorators import measure_time, print_some_noise
from src.benchmark import *


@print_some_noise
def main():
	gens = [gen_1, gen_2]
	finds = [find_1, find_2, find_3]

	for gen in gens:
		for find in finds:
			print(f"{measure_time(lambda: find(gen()))()[-1]}ms {gen.__name__}::{find.__name__}")


if __name__ == "__main__":
	main()
