"""
用于判断一个数字的奇偶性
"""

def main():
    x = int(input("what's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

"""
当True和False作为bool值用的时候，首字母必须要大写
"""
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

# 以上4行代码可以直接写成一行，return True if n % 2 == 0 else False
# 或者更简洁的版本return n % 2 ==0，因为这个式子本来就是就会得到一个bool值的答案
main()