def main():
    print("您的成绩等级为：",grade())



def grade():
    n = int(input("请输入您的成绩分数（满分100）："))
    if(n>=90):
        return'A'
    elif(n>=80 and n<=89):
        return 'B'
    elif(n>=70 and n<=79):
        return 'C'
    elif(n>=60 and n<=69):
        return 'D'
    else:
        return 'E'
    
    
main()