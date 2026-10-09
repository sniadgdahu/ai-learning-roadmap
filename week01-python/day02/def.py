"""
def用于定义函数，括号后面直接加：就行，不用{}，并且括号里面传参数可以设默认值
"""

def hello(name):
    print("hello,",name)

# 不传参的话就使用默认值world
def hello2(name="world"):
    print("hello,",name)

def main():
    name = input("what's your name? ")
    hello(name)
    hello2()

main()