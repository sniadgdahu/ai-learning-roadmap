
# 这是int类型讲解
# x = int(input("请输入数字x： "))
# y = int(input("请输入数字y： "))
# print("x+y=",x+y)


# 这是float类型讲解

def main():
    x = float(input("what's x? "))
    y = float(input("waht's y? "))

    """
    round()函数用于对数字进行四舍五入，输入必须为一个数字，默认对该数字进行
    整数的四舍五入。但若需要保留几位小数，只需要在‘，’后面加上要求保留的小数位数字
    即，round（n，1）就是表示对数字n保留一位小数进行四舍五入
    """

    print("x+y=",round(x+y))
    print("保留一位小数：x+y=",round(x+y,1))

    """
    用f-string格式化字符串对输出进行规范的要求（按照美国一样，三位数字之间加一个','）
    """
    z =round(x+y)
    print(f"用格式化字符串进行输出，数字之间用','进行分隔{z:,}")

    print(f"用f字符串进行两位小数的显示{z:.2f}")
    print("multi函数调用结果：",multi(z))


def multi(n):
    return n**2

main()
