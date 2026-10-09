"""
while的循环用法，python中没有++/--的语法
"""

i = 0
while i < 3:
    print("喵",end=' ')
    i += 1

"""
for循环，可以用range函数进行计数，range(3)就表示计数三次
"""

for i in range(3):
    print("汪")
"""
可以写成 for _ in range(3),将i变量直接换成_,因为i变量除了能起一个计数的作用
就没有其他的作用了，所以可以直接用_替代，还可以减少空间浪费
"""

"""
python可以用*直接打印多次print语句中的内容
"""
print("汪"*3)
print("汪\n"*3)
print("汪\n"*3,end="")


"""
continue是继续当前的循环，break是退出最近的循环,
这里就是当n大于0就直接退出这个while true的循环
"""
while True:
    n = int(input("what's n? "))
    if n < 0:
        continue
    else:
        break
# 也可以直接写成 if n > 0:
#                   break

for _ in range(n):
    print("meow")
