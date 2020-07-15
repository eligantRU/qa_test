def process_exception():
	from src.benchmark import find_3

	try:
		find_3([])
	except Exception as ex:
		print(f"gotcha: {ex}")
		return 42
	finally:
		print("finally block")


def main():
	print(process_exception())


if __name__ == "__main__":
	main()
