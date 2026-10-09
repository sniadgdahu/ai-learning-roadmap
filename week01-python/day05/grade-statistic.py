while True:
    n = int(input("有多少个学生？ "))
    if n > 0:
        break

students = []

math = 0
chinese = 0
english = 0
total = 0
a = 0
b= 0
c = 0
"""
列表需要用append（）函数，才能向列表里面加元素
"""

for i in range(n):
    # 需要每次都创建一个新的字典，然后将字典进行赋值
    dict1 = {"name":"","语文":"","数学":"","英语":"","总分":"","等级":""}
    dict1["name"] = input("请输入学生的姓名：")
    dict1["语文"]= int(input("请输入该生的语文成绩："))
    dict1["数学"]= int(input("请输入该生的数学成绩："))
    dict1["英语"]= int(input("请输入该生的英语成绩："))
    dict1["总分"] = dict1["数学"]+dict1["英语"]+dict1["语文"]
    if dict1["总分"] >= 270:
        dict1["等级"] = "A"
    elif dict1["总分"] >= 240:
        dict1["等级"] = "B"
    elif dict1["总分"] >= 180:
        dict1["等级"] = "C"
    else:
        dict1["等级"] = "D"

# """
# 这里智能用三个if，因为用elif的话，如果前面if语句执行了，就不会在执行elif语句
# 显然这里是需要分别判断三个地方的不及格人数
# """


    if dict1["语文"] < 60:
        a +=1
    if dict1["数学"] < 60:
        b +=1
    if dict1["英语"] < 60:
        c +=1
    students.append(dict1)


# """
# 这行代码用于对students列表进行排序，reverse=True是用来设置排序按照从高到低
# sort()是list的排序方法，默认从小到大进行排序，改了true就是从大到小
# key来设置按照什么内容进行排序
# lambda函数中前面的 student 是接收列表中的一个元素作为参数；
# 冒号后面的 student["总分"] 是取出这个学生的总分，
# 并把这个总分作为函数的返回值。
# """

students.sort(key = lambda student:student["总分"], reverse=True)


print("================ 成绩表 ================")
print(f"姓名\t语文\t数学\t英语\t总分\t等级")

for i in students:
#     print("name:",i["name"],"yuwen:",i["语文"],
#           "shuxue:",i["数学"],"yingyu:",i["英语"],"zongfen:",i["总分"])

    math +=i["数学"]
    chinese += i["语文"]
    english += i["英语"]
    total += i["总分"]

# 注意以下写法中的引号冲突，""里面不能在含有""，可以用'',或者在前面加转义字符\

    print(f"{i['name']}\t",
          f"{i['语文']}\t",
          f"{i['数学']}\t",
          f"{i['英语']}\t",
          f"{i['总分']}\t",
          f"{i['等级']}")

print(f"不及格人数\t{a}\t{b}\t{c}")
print(f"平均分\t{chinese/n:.2f}\t{math/n:.2f}\t{english/n:.2f}\t{total/n:.2f}")

print("=====================================")

print(f"总分最高分为：{students[0]['总分']}"
      f"\n总分最低分为：{students[len(students)-1]['总分']}")
