### 数据类型

#### 数字类型

```
整数类型，浮点数类型（float）、复数类型（complex）
>>> 156 / 31
5.032258064516129
>>> 155 // 31
5
>>> 156 % 31
1

```

### 数据类型转换

```
>>> float(int(560.1))
560.0
```

#### 获取变量类型

```
>>> a='ABC'
>>> type(a)
<class 'str'>
```

## 获得一个对象的所有属性和方法

```
dog1=Dog()
print(dir(dog1))
```

### Python关键字

```
>>> import keyword
>>> keyword.kwlist
```

### 算术运算符

```
>>> a=10
>>> b=5
>>> print(a + b)
15
>>> print(a - b)
5
>>> print(a * b)
50
>>> print(a / b)
2.0
>>> print(a ** b)
100000
>>> print(9 // 2)
4
>>> print(9.0 // 2.0)
4.0
```

### 比较运算符

```
>>> a=10
>>> b=20
>>> a == b
False
>>> a != b
True
>>> a > b
False
>>> a < b
True
>>> a >= b
False
>>> a <= b
True
>>> a + 10 >= b
True
>>> a + 10 > b
False
>>> a<=b-10
True
>>> a < b - 10
False
>>> a == b - 10
True
```

### 赋值运算符

```
>>> a=10
>>> b=20
>>> c=0
>>> c=a + b
>>> print(c)
30
>>> c += 10
>>> print(c)
40
>>> c -= a
>>> print(c)
30
>>> c *= a
>>> print(c)
300
>>> c /= a
>>> print(c)
30.0
>>> c %= a
>>> print(c)
0.0
>>> c=a ** 5
>>> print(c)
100000
>>> c //= b
>>> print(b)
20
>>> print(c)
5000
```

### 逻辑运算符

```
>>> a=10
>>> b=20
>>> a and b
20
>>> a or b
10
>>> not a
False
>>> not b
False
>>> not -1
False
>>> not False
True
>>> not True
False
```

### 成员运算符

```
>>> a=10
>>> b=5
>>> list=[1, 2, 3, 4, 5]
>>> print(a in list)
False
>>> print(a not in list)
True
>>> print(b in list)
True
```

### 身份运算符

```
>>> a=10
>>> b=10
>>> print(a is b)
True
>>> print(a is not b)
False
>>> b=20
>>> print(a is b)
False
```

## 字符串操作

```
>>> string1='hello'
>>> string2='world'
>>> print(string1 + string2)
helloworld
```

## 注释

```
>>> r=10    #半径，单位是米
```

## 通用序列操作

### 索引

```
>>> group_2='56789'
>>> group_2 [1]
'6'
>>> group_2[-1]
'9'
```

### 分片

```
group_3='123456789'
>>> group_3[0:5]
'12345'
>>> group_3[0:5:2]
'135'
>>> group_3[5:]
'6789'
>>> group_3[-5:]
'56789'
>>> group_3[:]
'123456789'
>>> group_3[::2]
'13579'
>>> group_3[::-1]
'987654321'
```

### 乘法

```
>>> word="abc"
>>> word*2
'abcabc'
```

### 序列相加

```
>>> [1, 2, 3] + [4, 5, 6]
[1, 2, 3, 4, 5, 6]
```

### 成员资格

```
>>> numbers=[1, 2, 3, 4, 5]
>>> 6 in numbers
False
```

### 长度、最小值和最大值

```
>>> numbers=[300,200,100,800,500]
>>> len(numbers)
5
>>> max(numbers)
800
>>> min(numbers)
100
```

## 列表

### 更新列表

#### 元素赋值

```
>>> group=[0,1,2,3,4]
>>> group[1]=9
>>> group
[0, 9, 2, 3, 4]
```

#### 增加元素

```
>>> group.append('test')
>>> group
[0, 9, 2, 3, 4, 'test']
```

#### 删除元素

```
>>> group
[0, 9, 2, 3, 4, 'test']
>>> del group[2]
>>> group
[0, 9, 3, 4, 'test']
```

#### 分片赋值

```
>>> group
[0, 9, 3, 4, 'test']
>>> group[0:2]="listing"
>>> group
['l', 'i', 's', 't', 'i', 'n', 'g', 3, 4, 'test']
```

```
>>> group
['1', '2', '3', '4', '5', '6', '7', '8']
>>> group[1:1]="和"
>>> group
['1', '和', '2', '3', '4', '5', '6', '7', '8']
```

### 嵌套列表

```
>>> group1=list("12")
>>> group2=list("45678")
>>> group[0]=group1
>>> group[1]=group2
>>> group
[['1', '2'], ['4', '5', '6', '7', '8']]
```

### 列表方法

#### extend()

```
>>> a=['hello','world']
>>> b=['python','is','funny']
>>> a.extend(b)
>>> a
['hello', 'world', 'python', 'is', 'funny']
```

#### index()

```
>>> field=['hello', 'world', 'python', 'is', 'funny']
>>> field.index('hello')
0
>>> field.index('abc')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 'abc' is not in list

```

#### insert()

```
>>> num=[1,2,3]
>>> num.insert(0,"和")
>>> num
['和', 1, 2, 3]
```

#### sort()

```
>>> num=[5,8,1,3,6]
>>> num.sort()
>>> num
[1, 3, 5, 6, 8]
>>> num1=[5,8,1,3,6]
>>> num2=sorted(num)
>>> num1
[5, 8, 1, 3, 6]
>>> num2
[1, 3, 5, 6, 8]
```

#### 高级排序

```
>>> field=['study', 'python', 'is', 'happy']
>>> field.sort(key=len)
>>> field
['is', 'study', 'happy', 'python']
>>> field.sort(key=len, reverse=True)
>>> field
['python', 'study', 'happy', 'is']

```

#### copy()

```
>>> field=['study','python','is','happy']
>>> copyfield=field.copy()
>>> copyfield
['study', 'python', 'is', 'happy']
```

#### remove()

```
>>> good=['女排','精神','中国','精神','学习','精神']
>>> good.remove('精神')
>>> good
['女排', '中国', '精神', '学习', '精神']
```

#### pop()

```
>>> field=['hello', 'world', 'python', 'is', 'funny']
>>> field.pop(0)
'hello'
>>> field.pop()
'funny'
```

#### reverse()

```
>>> num=[1,2,3]
>>> num.reverse()
>>> num
[3, 2, 1]
```

#### clear()

```
>>> field=['study','python','is','happy']
>>> field.clear()
>>> field
[]
```

#### count()

```
>>> good=['女排','精神','中国','精神','学习','精神']
>>> good.count(12)
0
>>> good.count("精神")
3
```

## 元组

```
>>> tuple(['hello', 'world'])
('hello', 'world')
>>> tuple('hello')
('h', 'e', 'l', 'l', 'o')
>>> tuple(('hello', 'world'))
('hello', 'world')
```

```
>>> tuple(['hi','python'])      #列表转元组
('hi', 'python')
>>> list(('hi', 'python'))     #元组转列表
['hi', 'python']
```

### 元组的基本操作

#### 访问元组

```
>>> strnum=('hi','python',2017,2018)
>>> strnum
('hi', 'python', 2017, 2018)
>>> strnum[1]
'python'
```

#### 删除元组

```
>>> greeting=('hi','python')
>>> greeting
('hi', 'python')
>>> del greeting
```

#### 元组的索引和截取

```
>>> field=('hello','world','welcome')
>>> field[2]
'welcome'
>>> field[1:]
('world', 'welcome')
```

### 元组内置函数

```
>>> number=(39,28,99,88,56)
>>> max(number)
99
>>> len(number)
5
>>> min(number)
28
```

## 列表与元组的区别

```
>>> t
('a', 'b', ['A', 'B'])
>>> t[2][0]='X'
>>> t
('a', 'b', ['X', 'B'])
```

## 字符串的简单操作

```
>>> print('读\"万卷书，\n行\t万里\'路。')
读"万卷书，
行      万里'路。
```



```
>>> print('圆周率PI的值为：%f' % 3.14)
圆周率PI的值为：3.140000
>>> print('一年有%d个月' % 12)
一年有12个月
>>> print('hi,%s' % 'python')
hi,python
>>> print('今天的空气质量比昨天提升了：%.2f%%' % 1.23)
今天的空气质量比昨天提升了：1.23%
>>> print('字符串%s，整数 %d，小数%.2f' %("abc",10,3.14))
字符串abc，整数 10，小数3.14

```

## 字符串方法

### split()方法

```
>>> say
'stay hungry stay foolish'
>>> say.split()
['stay', 'hungry', 'stay', 'foolish']
>>> say.split('s')
['', 'tay hungry ', 'tay fooli', 'h']
>>> say.split('s',2)
['', 'tay hungry ', 'tay foolish']
```

### strip()方法

```
>>> say=' stay hungry stay foolish '
>>> say.strip()
'stay hungry stay foolish'
>>> say
' stay hungry stay foolish '
```

### join()方法

```
>>> say=('stay hungry','stay foolish')
>>> new_say=','.join(say)
>>> new_say
'stay hungry,stay foolish'
>>> num=['1','2','3','4','a','b']
>>> plus_num='+'.join(num)
>>> plus_num
'1+2+3+4+a+b'

```

### find()方法

```
>>> say='stay hungry,stay foolish'
>>> say.find('stay')
0
>>> say.find('hun')
5
>>> say.find('python')
-1
```

### lower()方法

```
>>> greeting='Hello,World'
>>> greeting.lower()
'hello,world'
```

### upper()方法

```
>>> field='do it now'
>>> field.upper()
'DO IT NOW'
```

### replace()方法

```
>>> field='do it now,do right now'
>>> field.replace('do','123')
'123 it now,123 right now'
>>> field.replace('do','123',1)
'123 it now,do right now'
```

### swapcase()方法

```
>>> field='Just do it,NOW'
>>> field.swapcase()
'jUST DO IT,now'
```

### translate()方法

```
>>> intab='adefs'
>>> outtab='12345'
>>> trantab=str.maketrans(intab,outtab)
>>> st='just do it'
>>> st.translate(trantab)
'ju5t 2o it'
```

## 创建和使用字典

```
>>> dict_define={'小萌': '000', '小智': '001', '小强': '002'}
>>> dict_define
{'小萌': '000', '小智': '001', '小强': '002'}
>>> student=[('name','小智'),('number','001')]
>>> student_info=dict(student)
>>> student_info
{'name': '小智', 'number': '001'}
>>> student_info1=dict(name='小智',number='001')
>>> student_info1
{'name': '小智', 'number': '001'}
```

#### 修改字典

```
>>> student={'小萌':'000','小智':'001','小强':'002'}
>>> student['小强']
'002'
>>> student['小强']='005'
>>> student['小强']
'005'
>>> student['小张']='003'  #添加一个学生
>>> student['小张']
'003'

```

#### 删除字典元素

```
>>> del student['小张']
>>> student
{'小萌': '000', '小智': '001', '小强': '005'}
```

## 字典方法

### get()方法

```
>>> student
{'小萌': '000', '小智': '001', '小强': '005'}
>>> student.get('name','未指定')
'未指定'
>>> student.get('name')
>>> student.get('小强')
'005'
```

### keys()方法

```
>>> student
{'小萌': '000', '小智': '001', '小强': '005'}
>>> student.keys()
dict_keys(['小萌', '小智', '小强'])
>>> list(student.keys())
['小萌', '小智', '小强']

```

### values()方法

```
>>> student
{'小萌': '000', '小智': '001', '小强': '005'}
>>> student.values()
dict_values(['000', '001', '005'])
>>> list(student.values())
['000', '001', '005']
```

### key in dict方法

```
>>> student
{'小萌': '000', '小智': '001', '小强': '005'}
>>> '小萌' in student
True
>>> '小明' in student
False
```

### update()方法

```
>>> student={'小萌': '000', '小智': '001'}
>>> student2={'小李':'003'}
>>> student3={'小李':'005'}
>>> student.update(student2)
>>> student
{'小萌': '000', '小智': '001', '小李': '003'}
>>> student.update(student3)
>>> student
{'小萌': '000', '小智': '001', '小李': '005'}
```

### clear()方法

```
>>> student
{'小萌': '000', '小智': '001', '小李': '005'}
>>> student.clear()
>>> student
{}
```

### copy()方法

```
>>> student={'小萌': '000', '小智': '001'}
>>> st=student.copy()
>>> st
{'小萌': '000', '小智': '001'}
```

### fromkeys()方法

```
>>> seq=('name', 'age', 'sex')
>>> dict.fromkeys(seq)
{'name': None, 'age': None, 'sex': None}
>>> dict.fromkeys(seq, 10)
{'name': 10, 'age': 10, 'sex': 10}
```

### items()方法

```
>>> student={'小萌': '000', '小智': '001'}
>>> student.items()
dict_items([('小萌', '000'), ('小智', '001')])
```

### setdefault()方法

```
>>> student={'小萌': '000', '小智': '001'}
>>> student.setdefault('小张','006')
'006'
>>> student.setdefault('小智','006')
'001'
>>> student
{'小萌': '000', '小智': '001', '小张': '006'}
```

## 集合

```
>>> numbers={1,2,3,4,5,3,2,1,6}
>>> numbers
{1, 2, 3, 4, 5, 6}
```

### 创建集合

```
>>> name=set('abc')
>>> name
{'c', 'b', 'a'}
>>> students=set(['小萌','小智'])
>>> students
{'小萌', '小智'}
```

### 集合方法

#### add()方法

```
>>> students
{'小萌', '小智'}
>>> students.add(1)
>>> students
{'小萌', '小智', 1}
```

#### remove()方法

```
>>> students
{'小萌', '小智', 1}
>>> students.remove('小智')
>>> students
{'小萌', 1}
```

#### in和not in

```
>>> students
{'小萌', 1}
>>> 1 in students
True
>>> 2 not in students
True
```

## import的使用

```
import math
print(math.pi)
```

```
from math import pi
print(pi)
```

```
from math import *
print(pi)
```

```
import math as m
print(m.pi)
```

### if语句

```
num = 80
if num > 10:
    print('num的值大于10')
elif 0 <= num <= 10:
    print('num的值介于0和10之间')
else:
    print('num的值小于0')
```

```
num=10
if num <= 10 and num>=5:
    print('num的值介于5和10之间')
else:
    print('num的值不介于5和10之间')
```

### is 和 ==的区别

```
z=[1,2,3]
x=z.copy()
print(x==z)
print(x is z)
使用==运算符判定两个对象是否相等，使用is判定两个对象是否等同（是否为同一对象）
```

### 断言

```
>>> x=3
>>> assert x > 0, "x is not zero or negative"
>>> x=-3
>>> assert x > 0, "x is not zero or negative"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError: x is not zero or negative
```

## 循环

### while循环

```
n=1
while n<=5:
    print(n)
    n += 1
```

### for循环

```
fields=['a','b','c']
for f in fields:
    print(f)
```

```
tups={'name':'小智','number':100}
for tup in tups:   #for循环字典
    print(tup)
    print(tups[tup])
```

### 迭代工具

#### 并行迭代

```
student=['xiaomeng','xiaozhi','xiaoqiang']
number=[1001,1002,1003]
for name,num in zip(student,number):
    print(name)
    print(num)
```

### 跳出循环

#### break

```
for letter in 'hello':
   if letter == 'l':
      break
   print (letter)
```

#### continue

```
for letter in 'hello':
   if letter == 'l':
      continue
   print (letter)
```

#### 在while循环中使用else语句

```
num=0
while num < 3:
   print (f"{num} 小于 3")
   num += 1
else:
   print (f"{num} 大于或等于 3")
print("结束循环!")
```

#### 在for循环中使用else语句

```
for letter in 'hello':
   # if letter == 'l':
   #    break
   print (letter)
else:
   print("结束")
```

## pass语句

```
fields=['a','b','c']
for f in fields:
    pass
```

## 函数

```
def fun1():
   print("函数1")
fun1()
```

```
def fun2(name,age):
   print(name)
   print(age)
fun2("tom",18)
fun2(age=18,name="tom")
```

### 默认参数

```
def fun3(name, age=23):
   print(name)
   print(age)
fun3(age=18,name="tom")
fun3("tom")
```

### 可变参数

```
def fun4(name, *vartuple):
   print(name)
   for i in vartuple:
      print(i)
fun4("tom",1,2,3)
args=(1, 2, 3, 4)
fun4("tom",*args)
```

```
def fun5(name, **kw):
    print(name)
    print(kw)
fun5("hhj", 城市="深圳", 爱好="编程")
other={'城市': '北京', '爱好': '编程'}
fun5("hhj", **other)
注意kw获得的字典是other复制的，对kw的改动不会影响函数外的other
```

## 变量的作用域

```
a = [1, 2, 3]
def fun1(a):
    a[1] = 9
print(a)   # [1, 2, 3]
fun1(a)
print(a)   # [1, 9, 3]
```

```
a = 8
def fun1(a):
    a=10
print(a)   # 8
fun1(a)
print(a)   # 8
```

```
a = 8
def fun1():
    global a
    a=10
print(a)   # 8
fun1()
print(a)   # 10
```

## 返回函数

```
def sum_late(*args):
    def calc_sum():
        ax=0
        for n in args:
            ax=ax + n
        return ax
    return calc_sum
calc_sum=sum_late(1, 2, 3, 4)
print(calc_sum())
```

## 递归函数

```
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
print(fact(4))
```

## 匿名函数

```
def is_odd(n):
    return n % 2 == 1
newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(list(newlist))

c = lambda x, y, z: x * y * z
print(c(1, 2, 3))
a = [item for item in filter(lambda x: x > 3, [1, 2, 3, 4, 5])]
```

## 偏函数





```
class Student(object):
    def __fun1(self):
        print("这是私有方法")
    def __init__(self, name, score):
        self.name=name
        self.__score=score
    def info(self):
        print(f'学生：{self.name}；分数: {self.__score}')
        self.__fun1()
    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0<=score<=100:
            self.__score=score
        else:
            print('请输入0到100的数字。')

stu=Student('xiaomeng',95)
print(stu.name)
print(stu.get_score())
stu.info()
stu.set_score(-10)
```

## 继承

```
class Animal(object):
    def run(self):
        print('Animal is running...')
class Dog(Animal):
    def eat(self):
        print('Eating ...')
    def run(self):
        print('Dog is running...')
Animal().run()
dog1=Dog()
dog1.run()
dog1.eat()
print(isinstance(dog1, Animal))
```

## 类的专有方法

#### __str__

```
class Animal(object):
    def run(self):
        print('Animal is running...')
    def __str__(self):
        return "这是str方法"
dog1=Animal()
print(dog1)
```

#### __iter__

```

```

#### __getitem__

#### __getattr__

#### __call__

```
class Animal(object):
    def run(self):
        print('Animal is running...')
    def __str__(self):
        return "这是str方法"
    def __call__(self):
        print("call")
dog1=Animal()
dog1()
```

## 异常

```
def mult_exception(x,y):
    try:
        a=x/y
        b=name
    except ZeroDivisionError:
        print('this is ZeroDivisionError')
    except Exception:
        print('this is NameError')
mult_exception(2,1)
```

```
def mult_exception(x,y):
    try:
        a=x/y
        b=name
    except (ZeroDivisionError,NameError):
        print('this is ZeroDivisionError')
    except Exception as e:
        print('this is NameError')
        print(e)
mult_exception(2,1)
```

## 异常中的else

```
def mult_exception(x,y):
    try:
        a=x/y
    except Exception as e:
        print(e)
    else:
        print("else")
    finally:
        print("finally")
mult_exception(2,0)
# 如果在try子句执行时没有发生异常，就会执行else语句后的语句
# 无论try子句中是否发生异常，finally都会被执行
```

## 日期和时间

```
import time
start_time=time.time()
time.sleep(3)
end_time=time.time()
print((end_time-start_time))
```

## datetime模块

```
import datetime
print(datetime.datetime.now())
# 2021-09-18 16:48:54.418067
```

