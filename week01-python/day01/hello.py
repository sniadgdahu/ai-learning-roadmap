#视频跟练
print("hello,world!")
print(1+2)
print("i'm learning for make more money hhhh...")

#直接用变量接收input函数
# age=input("how old are you? my hon ")

"""
这是多行注释的演示
"""
#打印接收到的年纪
# print("i'm "+ age +" years old!")

"""
print(argu1,argu2,argu3...)，print()函数可以接收多个参数，在输出的时候，
每个参数之间都会自带空格，这样就不需要我们手动敲空格，来个例子
"""
#这里其实在？后面有一个空格，这样在输入的时候就不会连在一起显示，比较美观
name = input("what's your name? ")
# print("hello my name is",name,"and i'm",age,"years old!")

"""
print(sep=' ',end='\n'),print()函数默认结束会有换行符,当有多个参数的时候,
分隔符默认为空格，但是我们也可以自己设置分隔符(sep)和换行符(end),例如：
"""
#执行完这俩print，输出在同一行，并由**连接，名字由？？连接
print("my name is ",name,sep='??',end='**')
print("test end changed")

"""
以上有两种参数，一种是位置参数，就像name，age之类的，是按照位置顺序传递的，
还有一种是命名参数，就像sep，end之类的，可以通过它们的名字来直接使用它们
"""

"""
如果想要在字符串中输出含有引号的内容，那么就需要'""'这样，在单引号中间输入需要
进行输出的双引号，这样可以保证双引号被输出，也可以全用双引号，但是加上\来表示
这个""是转义字符，需要进行输出，ok，test
"""

print("i just making a \"test\"")
print('this is another "test"')#输出语句均有“”

"""
字符串的特殊用法，在print()语句中字符串前面加上f，可以直接在字符串中用{name}
的形式输入变量，可以直接输出变量的值，而不是name这个字符串,
f 是作用于字符串前面的，并且只作用于它紧挨着的那个字符串，后面的字符串它不起作用
"""

print(f"hello my name is {name}")
print(name,f"{name} is my name")
print(f"my name is {name}","{name} is not been output")
