import sympy
import re

while True:
    try:
        
        # 先将输入的正常方程式转换为sympy能够处理的式子(移项后的式子)。
        # 如x+1=2转换为x-1(省略"=0")。
        string = input("请输入一元方程式(相乘请勿省略乘号):").replace(" ","")
        get_unknown = re.search('([a-z])', string)
        unknown = sympy.symbols(get_unknown.group())
        m = re.search("=([^\s].*)", string)
        m = m.group()
        formula = string.replace(m, "") + "-" + m.replace("=", "")
        
        result = sympy.solve([formula],[unknown]) # 解方程交给sympy，就没了
        
        print("解得:", result)
    except:
        print("<无效的输入>")
