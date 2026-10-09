"""
range(i,j)函数的取值是[i,j)
"""

# for i in range(1,10):
#     for j in range(1,10):
#         if j == i:
#             print(f"{j}*{i}=", j * i)
#             break
#         else:
#             print(f"{j}*{i}=", j * i, end=" ")



"""
外层的i就是行，内层的j是列，
一行中，行的数字是不变，列的数字累加到等于行，所以可以优化j，
直接写成range(1,i+1)
"""

for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={j*i}",end=" ")
    print()