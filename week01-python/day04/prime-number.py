import math

"""
算术平方根，向上取整，向下取整都需要引用math库，
math.sqrt(n)是求算术平方根
math.isqrt(n)是求算术平方根的下整数
math.ceil(n)是求>=n的最小整数，也就是向上取整
math.ceil(math.sqrt(n))是求算术平方根的上整数
"""
# n=10
# print(math.sqrt(n))
# print(math.isqrt(n))
# print(math.ceil(math.sqrt(n)))


while True:
    n = int(input("what's n? "))
    if n >= 2:
        break

"""
现在是找到有因数，就输出不是，继续找完剩下的所有的因数来检查，最后检查完了
才能说是质数
"""
# if n == 2 or n == 3:
#     print(f"{n} is prime number")
# else:
#     for i in range(2,math.isqrt(n)+1):
#         if n % i == 0:
#             print(f"{n} isn't prime number")
#             break
#         elif i == math.isqrt(n):
#             print(f"{n} is prime number")

"""
Python 有一种特殊语法：
for ... else
你可以把它理解成：else 可以直接跟在 for 后面，它属于 for，而不是 if。

简洁思路：先假设它就是质数，然后找到因数就把它改成不是质数，如下：
"""

for i in range(2, math.isqrt(n) + 1):
    if n % i == 0:
        print(f"{n} 不是质数")
        break
else:
    print(f"{n} 是质数")