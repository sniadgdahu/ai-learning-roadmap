def main():
    number = get_number()
    meow(number)


def get_number():
#    想清楚逻辑，将input语句放入while才能进行无限循环输入，否则只能输入一次
# 但是也还在无限循环中
    while True:
        n = int(input("what's n? "))
        if n > 0:
            return n


def meow(n):
    for _ in range(n):
        print("meow")

main()