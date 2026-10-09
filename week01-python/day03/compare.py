x = int(input("what's x? "))
y = int(input("what's y? "))


"""
python 的if语句没有（），直接在if后面写条件就可以，也没有{}，写完条件加一个：
就可以写主体部分了，并且&&符号直接写成and ，||符号直接写成or
"""
if x > y:
    print("x > y")
elif x < y:
    print("x < y")
else:
    print("x = y")

if x > y or x < y:  #可以直接问x!=y
    print("x is not equal to y")
else:
    print("x equals y")


"""
pyhton 中可以直接写10<=x<=20，不需要拆成两个不等式
"""

score = int(input("what's your score? "))

if 90 <= score <= 100:
    print("Grade : A")
elif 80 <= score < 90:
    print("Grade : B")
elif 70 <= score < 80:
    print("Grade : C")
elif 60 <= score < 70:
    print("Grade : D")
else:
    print("Grade : F")