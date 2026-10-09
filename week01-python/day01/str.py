"""
字符串的内置函数strip()用法，用于去除接收的字符串前后的空格
例如接收一个名字，但是用户输入不规范，前后有许多空格，程序会直接输出用户前后都输入
的空格，但是这样超级不美观，所以用strip()函数对字符串前后空格进行处理
"""

name = input("what's your name? ")
print(f"my name is {name}")

#strip()函数去除字符串前后空格(但是不能去除中间的空格),在输出格式规范的字符串
name = name.strip()

print(f"my name is {name}")

"""
capitalize()这个函数只会大写第一个字母，但是用title()，这个函数可以
对输入的每个单词的首字母均进行大写
"""
#输入 serena deng进行测试，答案Serena deng，不是Serena Deng
name = name.capitalize()
print(f"my name is {name}")

name = name.title()
print(f"my name is {name}")

"""
函数可以链式调用
name = input("what's your name").strip().title()
可以用以上方式对代码进行简化 
"""


"""
split("")函数可以用于对字符串进行分割，只需要在""中输入用于分隔的符号即可，
可以直接在前面按顺序对变量进行赋值，那么经过split分隔的值也会按顺序存入变量
split(" ")表示一个空格作为分隔符，遇到几个空格就会切分一次，不会把连续的所有
空格合成一个切分，因为""里面明确说了分隔符为一个空格，但使用split()
就会默认只要是空格就是一个切分，也不管空格的长度，因为没有设置分隔符的内容
"""

# first , last = name.split(" ")
print(name.split())
print(name.split(" "))
# print(f"my first name is {first}",f"and my last name is {last}")

