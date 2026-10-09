"""
该程序用于提示用户输入一个名字，然后输出这个名字在哈利波特的世界中属于
哪一个学院
"""

"""
match相当于switch的用法，最后的case _:就相当于else，对其他没有列举到的情况
进行阐述,记得最后的case和_之间有一个空格
"""

name = input("what's your name? ")
"""
match name:
    case "哈利":
        print("格兰分多")
    case "赫敏":
        print("格兰芬多")
    case "罗恩":
        print("格兰芬多")
    case "德拉科":
        print("斯莱特林")
    case _:
        print("who?")

"""
# 可以用或者符号更简洁的书写
match name:
    case "哈利" | "赫敏" | "罗恩":
        print("格兰分多")
    case "德拉科":
        print("斯莱特林")
    case _:
        print("who?")
