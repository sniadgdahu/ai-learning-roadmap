"""
不建议有自己调用自己的情况存在，如果需要的话可以改成while true的形式
然后再用continue 和return来进行反复调用函数执行或者结束函数
"""




students = []
# 因为下面四个平均分只在calculate_average()函数中被需要，完全可以作为一个
# 局部变量在calculate_average()进行创建，所以就不需要这四个全局变量了
# chinese_average = 0
# math_average = 0
# english_average = 0
# total_average = 0 

def main():
    while True:
        m = int(input(
            "添加学生请按 1\n" \
            "删除学生请按 2\n" \
            "查询学生请按 3\n" \
            "修改成绩请按 4\n" \
            "计算平均分请按 5\n" \
            "获取排序结果请按 6\n"\
            "获取当前学生成绩统计表请按 7\n"\
            "退出请按 8\n"))
        match m:
            case 1:
                add_student()
                # main()
            case 2:
                delete_student()
                # main()
            case 3:
                search_student()
                # main()
            case 4:
                change_scores()
                # main()
            case 5:
                calculate_average()
                # main()
            case 6:
                gain_sort()
                # main()
            case 7:
                show_table()
                # main()
            case 8:
                return
            case _:
                print("请根据提示内容进行输入！")

def check_score(score,subject):
    while True:
        if score < 0 or score > 100:
            print("成绩范围是0-100，请重新输入成绩！")
            match subject:
                case "chinese":
                    score = int(input("请输入学生的语文成绩： "))
                case "math":
                    score = int(input("请输入学生的数学成绩： "))
                case "english":
                    score = int(input("请输入学生的英语成绩： "))
        else:
            return score
        
"""
已经写了check_score来简化以下三个函数，避免重复编码                
# def check_chinese(chinese_score):
    while True:
        if chinese_score < 0 or chinese_score > 100:
            print("成绩范围是0-100，请重新输入成绩！")
            chinese_score = int(input("请输入学生的语文成绩： "))
        else:
            return chinese_score
        
# def check_math(math_score):
    while True:
        if math_score < 0 or math_score > 100:
            print("成绩范围是0-100，请重新输入成绩！")
            math_score = int(input("请输入学生的数学成绩： "))
        else:
            return math_score
        
# def check_english(english_score):
    while True:
        if english_score < 0 or english_score > 100:
            print("成绩范围是0-100，请重新输入成绩！")
            english_score = int(input("请输入学生的英语成绩： "))
        else:
            return english_score
"""
            
def add_student():
    name = input("请输入学生的姓名： ")
    for i in range(len(students)):
        if students[i]["name"] == name:
            print("该学生已存在，添加无效！")
            return
    chinese_score = int(input("请输入学生的语文成绩： "))
    chinese_score = check_score(chinese_score,"chinese")
    math_score = int(input("请输入学生的数学成绩： "))
    math_score = check_score(math_score,"math")
    english_score = int(input("请输入学生的英语成绩： "))
    english_score = check_score(english_score,"english")
    total_score = chinese_score + math_score + english_score

    student = {
        "name" : name,
        "chinese_score" : chinese_score,
        "math_score" : math_score,
        "english_score" : english_score ,
        "total_score" : total_score
    }

    students.append(student)
    print("添加成功！")
    return


def delete_student():
    name = input("请输入需要删除的学生姓名： ")

    for i in range(len(students)):
        if students[i]["name"] == name:
            del students[i]
            print("删除成功！")
            return
    print("该学生不存在！")


def search_student():
    name  = input("请输入需要查找的学生姓名： ")

    for i in range(len(students)):
        if students[i]["name"] == name:
            print("姓名\t语文\t数学\t英语\t总分\t")
            print(f"{students[i]['name']}\t",
              f"{students[i]['chinese_score']}\t",
              f"{students[i]['math_score']}\t",
              f"{students[i]['english_score']}\t",
              f"{students[i]['total_score']}\t")
            print("查询成功！")
            return 
        
    print("没有找到该学生！")


def change_scores():
    name = input("请输入需要修改成绩的学生的姓名： ")

    for i in range(len(students)):
        if students[i]["name"] == name:
            students[i]["chinese_score"] = int(input("请输入该生的语文成绩：")) 
            students[i]["chinese_score"] = check_score(students[i]["chinese_score"],"chinese")
            students[i]["math_score"] = int(input("请输入该生的数学成绩：")) 
            students[i]["math_score"] = check_score(students[i]["math_score"],"math")
            students[i]["english_score"] = int(input("请输入该生的英语成绩：")) 
            students[i]["english_score"] = check_score(students[i]["english_score"],"english")
            students[i]["total_score"] =  students[i]["chinese_score"] + students[i]["math_score"] + students[i]["english_score"]
            print("修改成功！")
            print("姓名\t语文\t数学\t英语\t总分\t")
            print(f"{students[i]['name']}\t",
                f"{students[i]['chinese_score']}\t",
                f"{students[i]['math_score']}\t",
                f"{students[i]['english_score']}\t",
                f"{students[i]['total_score']}\t")
            return
    print("没有找到该学生！")


def calculate_average():
    
    if len(students) == 0:
        print("当前表格中没有学生，无法计算平均分！")
        return 
    else:
        chinese_score = 0
        math_score = 0
        english_score = 0
        total_score = 0
        for i in range(len(students)):
            chinese_score += students[i]["chinese_score"]
            math_score += students[i]["math_score"]
            english_score += students[i]["english_score"]
            total_score += students[i]["total_score"]
        chinese_average = chinese_score/len(students)
        math_average = math_score/len(students)
        english_average = english_score/len(students)
        total_average = total_score/len(students)

        print(f"语文平均分:{chinese_average:.2f}\n",
            f"数学平均分:{math_average:.2f}\n",
            f"英语平均分:{english_average:.2f}\n",
            f"总分平均分:{total_average:.2f}"
            )
        return

"""
之所以将show_table()
        return
移出match模块，是因为这样写重复编码了，
首先进入while部分，输入m，然后进行match比对，存在case值就进行相应的排序，
排序完了就直接退出match部分了，继续执行while中的show_table()，然后就直接
return退出while死循环了，
如果不符合match中case的值，那就执行continue，continue会直接结束当前本次循环，
continue后面的在while中的代码就不会执行，直接跳到while部分重新从while开始执行
新的一次循环，这样也不会执行到return，就不会退出循环，也达到了目的
"""
def gain_sort():

    while True:
        m = input("请输入需要按照什么进行排序(语文/数学/英语/总分)？ ")
        match m:
            case "语文":
                students.sort(key= lambda student:student["chinese_score"],reverse=True)
                # show_table()
                # return 
            case "数学":
                students.sort(key= lambda student:student["math_score"],reverse=True)
                # show_table()
                # return 
            case "英语":
                students.sort(key= lambda student:student["english_score"],reverse=True)
                # show_table()
                # return 
            case "总分":
                students.sort(key= lambda student:student["total_score"],reverse=True)
                # show_table()
                # return 
            case _:
                print("请根据要求的内容进行输入！") 
                # gain_sort()
                continue
        show_table()
        return 


def show_table():
    if len(students) == 0:
        print("当前表格中没有学生！")
    else:
        print("当前学生统计表格如下：\n")

        print("姓名\t语文\t数学\t英语\t总分\t")
        for i in range(len(students)):
            print(f"{students[i]['name']}\t",
                f"{students[i]['chinese_score']}\t",
                f"{students[i]['math_score']}\t",
                f"{students[i]['english_score']}\t",
                f"{students[i]['total_score']}\t")
        return



main()
