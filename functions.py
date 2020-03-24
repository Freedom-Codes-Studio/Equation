import re,time

def delete_split(string,begin,end):
	# 用于删除给定字符串的一部分
	string = string[:begin] + string[end:]
	return string

def find_element(string):
	# 初始化一个列表，用于保存所有常量的索引
	const_list = []
	# 初始化一个列表，用于保存所有未知数的索引
	x_list = []

	# 常数的正则表达式
	RegExp_const = r"(\+|-|\*|/)*\d+(\+|-|\*|/)*([^A-z0-9]|$)"
	# 未知数的正则表达式
	RegExp_x = r"(\+|-|\*|/)*\d*[A-z](\+|-|\*|/)*([^A-z0-9]|$)"

	for const_string in re.finditer(RegExp_const,string):
		const_span = list(const_string.span())
		for i in [const_span[0],const_span[1]-1]:
			if string[i]=='+' or string[i]=='-' or string[i]=='*' or string[i]=='/':
				if i == const_span[0]:
					const_span[0] += 1
				else:
					const_span[1] -= 1
		const_list.append(const_span)

	for x_string in re.finditer(RegExp_x,string):
		x_span = list(x_string.span())
		for i in [x_span[0],x_span[1]-1]:
			if string[i]=='+' or string[i]=='-' or string[i]=='*' or string[i]=='/':
				if i == x_span[0]:
					x_span[0] += 1
				else:
					x_span[1] -= 1
		x_list.append(x_span)

	return {"const_list":const_list,"x_list":x_list}

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
