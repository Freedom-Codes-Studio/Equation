import re

# 计算一个传入的字符串
def count_string(string):
	numbers = []
	search_numbers_regExp = r"\d+"
	
	while True:			# 把数字全拿出来
		numbers_object = re.search(search_numbers_regExp,string)
		if numbers_object:		# 匹配到了数字
			numbers_span = numbers_object.span()
			number_str = string[numbers_span[0]:numbers_span[1]]
			numbers.append(int(number_str))
			string = string.replace(number_str,"",1)
		else:
			break
	
	# 初始化返回值
	result = numbers[0]
	# 数字拿出来之后，剩下的全是符号
	chars = list(string)
	for i in range(len(chars)):
		if chars[i] == '+':
			result += numbers[i+1]
		elif chars[i] == '-':
			result -= numbers[i+1]
		elif chars[i] == '*':
			result *= numbers[i+1]
		else:
			result /= numbers[i+1]
	
	return result
