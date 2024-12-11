'''
person_dic = {'Name','홍길동','Age': '27','Class':'초급'}

print(person_dic['Name'])
print(person_dic['Age'])



phone_book={"홍길동":"010-1234-56789", "강감찬":"010-1234-5679","이순신":"010-1234-5680"}

print(phone_book["강감찬"])
      
print(phone_book.keys())
      
print(phone_book.values())

print(phone_book.items())

for name, phone_num in phone_book.items():
      print(name,':',phone_num)     
'''

'''
stores = {"커피음료":7,"펜":3,"종이컵":2,"우유":8,"콜라":4,"책":5}
print("재고 : ",stores[input("물건의 이름을 입력하시오: ")])
'''
'''
numbers={2,1,3}      
if 1 in numbers:
      print("집합 안에 1이 있습니다.")
else:
    print("집합 안에 1이 없습니다.")
'''
'''
numbers = {2,1,3}
for x in numbers:
    print(x,end="")
'''
'''
A=  set("ajxignwfwozler")
for x in sorted(A):
    print(x, end="")
'''
'''
a_list = ['hello','world','welcome','to','python']
'python' in a_list
True
'''
