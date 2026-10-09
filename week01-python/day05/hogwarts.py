"""
list数据类型
"""
# students = ["赫敏","哈利","罗恩"]

"""
for循环可以直接遍历list列表,不需要知道列表长度，直接用变量名就可以遍历
len()函数可以用来得到列表的长度
"""

# for student in students:
#     print(student)

# for i in range(len(students)):
#     print(students[i])


"""
dict字典数据类型，拥有键和值两部分，键：值的形式，并且用{}来定义
可以直接用字典的键来当索引，查看字典的值，eg：students["赫敏"]，
这就是查看students字典中，赫敏这个键所对应的值是多少

"""

# students = {
#     "赫敏":"格兰芬多",
#     "哈利":"格兰芬多",
#     "罗恩":"格兰芬多",
#     "德拉科":"斯莱特林"
#     }

# print(students["赫敏"])
"""
用for循环遍历字典的时候，默认遍历的是键，然后可以用键作为索引来遍历值
"""

# for student in students:
#     print(student)
#     print (student , students[student],sep=",")

"""
用字典作为列表的元素，可以描述一个表，比如学生表，
列表的一个元素就是一个学生的所有信息，学生的各种信息用字典来存储，
通过列表元素的遍历，可以直接用字典的键值来查看正割列表的对应的值为多少
"""

students = [
    {"name":"赫敏", "house":"格兰芬多", "patrobus":"水濑"},
    {"name":"哈利", "house":"格兰芬多", "patronus":"麋鹿"},
    {"name":"罗恩","house":"格兰芬多","patronus":"狗"},
    {"name":"德拉科","house":"斯莱特林","patronus":None}
]

for student in students:
    print(student["name"])
