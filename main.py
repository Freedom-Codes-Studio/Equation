import functions as fun

# 让用户输入一个方程
temp_main = input("输入一个方程:")
temp_x = input("输入方程中的未知数:")

# 将方程分成两半
temp_main = temp_main.split('=')



# 合并同类项
# 左边部分
temp_left_number_str = temp_main[0].replace(temp_x,'')
temp_left_number = fun.count_string(temp_left_number_str)
temp_left = f"{temp_left_number}" + temp_x
# 右边部分
temp_right = str(fun.count_string(temp_main[1]))
# 放进方程
temp_main[0] = temp_left
temp_main[1] = temp_right

# 系数化为1
temp_x_number = temp_main[0].replace(temp_x,'')
temp_x_number = int(temp_x_number)
temp_right = int(temp_main[1])
result = temp_right/temp_x_number
print(f"解得 x = {result}")
