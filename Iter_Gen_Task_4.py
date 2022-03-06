nested_list = [
	['a', 'b', 'c', [1, 2, [33, 44, 55, ['r', 4, 'zz']]]],
	['d', 'e', [121, 232, 343, 'ttt', [999, 1010, None, [False]]], 'f', 'h', False],
	[1, 2, None, [111, 444, 'sss']],
]

def print_elements(list_input):
	for items in list_input:
		yield items

def print_all(list_2):
	for element in print_elements(list_2):
		if isinstance(element, list):
			print_all(element)
		else:
			print(element)

if __name__ == '__main__':
	print(print_all(nested_list))
