Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
heights = [178,173,166,164,176]
heights.sort()
print('이 중에서 가장 작은 값은 :', heights[0])
이 중에서 가장 작은 값은 : 164
print('이 중에서 가장 큰 값은 :',heights[-1])
이 중에서 가장 큰 값은 : 178
a=[1,2,3]
b=a
b
[1, 2, 3]
b[0]=0
b
[0, 2, 3]
a
[0, 2, 3]
id(a), id(b)
(2454123793984, 2454123793984)
>>> c=list(a)
>>> c
[0, 2, 3]
>>> c[0]=1
>>> c
[1, 2, 3]
>>> a
[0, 2, 3]
>>> id(a), id(b), id(c)
(2454123793984, 2454123793984, 2454123802368)
>>> [x **2 for x in [1,2,3,4,5]]
[1, 4, 9, 16, 25]
>>> [x for x in range(10)]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> [x * x for x in rnage(10)]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    [x * x for x in rnage(10)]
NameError: name 'rnage' is not defined. Did you mean: 'range'?
>>> [x * x for x in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> st = ' Hello World'
>>> ['H', 'E', 'L', 'L', 'O', ' ', 'W' ,'O','R','L','D']
['H', 'E', 'L', 'L', 'O', ' ', 'W', 'O', 'R', 'L', 'D']
>>> a = ['welcome', 'to', 'the', 'python', 'world']
>>> frist_a = [s[0].upper() for s in a]
>>> print(frist_a)
['W', 'T', 'T', 'P', 'W']
>>> [x for x in range(10) if x % 2 == 0]
[0, 2, 4, 6, 8]
>>> [x**2 for x in range(10) if x % 2 ==0]
[0, 4, 16, 36, 64]
>>> s = ['Hello','12345','World', '67890']
>>> numbers = [x for x in s if x.isdigit()]
>>> print(numbers)
['12345', '67890']
>>> [int(x) for x in input('정수를 여러 개 입력하세요 : ').split()]
정수를 여러 개 입력하세요 : 100
[100]
>>> [int(x) for x in input('정수를 여러 개 입력하세요 : ').split() if x.isdigit]
정수를 여러 개 입력하세요 : 100 이백 300 400
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    [int(x) for x in input('정수를 여러 개 입력하세요 : ').split() if x.isdigit]
ValueError: invalid literal for int() with base 10: '이백'
100 200 300 400
SyntaxError: invalid syntax
[int(x) for x in input('정수를 여러 개 입력하세요 : ').split()]
정수를 여러 개 입력하세요 : 100 200 300
[100, 200, 300]
[int(x) for x in input('정수를 여러 개 입력하세요 : ').split() if x.isdigit()]
정수를 여러 개 입력하세요 : 100 이백 300 400
[100, 300, 400]
[(x, y) for x in [1,2,3] for y in [3,1,4]]
[(1, 3), (1, 1), (1, 4), (2, 3), (2, 1), (2, 4), (3, 3), (3, 1), (3, 4)]
[(x, y) for x in [1,2,3] for y in[3,1,4] if x!= y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
t1 = (1,2,3,4,5)
t1[0] = 100
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    t1[0] = 100
TypeError: 'tuple' object does not support item assignment
t1 = (1,2,3,4,5)
t1[0]
1
t1[1:4]
(2, 3, 4)
t2 = t1+ t1
t2
(1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
