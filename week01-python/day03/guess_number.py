import random

n = random.randint(1,100)

check = True
m =5

while(m):
    x = int(input("请输入一个数字（1-100）"))
    m = m-1
    if x > n:
        print("大了，猜小一点")
    elif x < n:
        print("小了，猜大一点")
    else:
        print("恭喜你，猜中啦！")
        check = False
        break

if check:
    print("还差一点就猜中了，再接再厉哦！")

