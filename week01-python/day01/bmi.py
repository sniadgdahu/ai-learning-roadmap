"""
day01的作业--BMI计算器

BMI=体重(kg)/身高的平方(m)

"""

weight =float(input("请输入您的体重(kg): ")) 
height = float(input("请输入您的身高(m): "))

# 平方可以直接写成height**2
BMI = weight/height**2
# 用于将float类型的值取两位小数，不然小数太多影响观感
BMI_2f =f"{BMI:.2f}"#f用于格式化显示，会严格的得到两位小数，可以展示00
#round管数值，对数字进行四舍五入之后，会显示最简结果，
# 得到的小数位不超过2位，可能只有一位小数
# 所以round管数值，f管显示，不管怎样都会严格按照要求进行显示
BMI_2 =round(BMI,2)

print(f"您的BMI是{BMI_2f}")
print(f"您的BMI是{BMI_2}")

