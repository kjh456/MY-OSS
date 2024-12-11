'''
여러줄로 주석을 달수 있어요

'''
"""
--------------------------
제작날짜 : 2024.09.13    | 
제작자 : 김종호          |
제목 : 파이썬 연습 ,실습 |
--------------------------
"""

반지름 = 7
면적 = 3.14 * 반지름 * 반지름 #면적을 구하는 변수는 면적이야
print(면적)
print("면적")

print(4*3*2*1)
print(1/2)
print(300-100)
print(423+12340)
print((1/100) * 1234)
print(3.141592 * 12.0 *12.0)


#신체 질량 지수 구하기

def calculate_bmi(weight, height):
    bmi = wight / (height ** 2)
    return bmi

weight = float(input("몸무게를 입력하세요 (kg): "))
height = float(input("키를 입력하세요 (m): "))

bmi = calculate_bmi(weight, height)
                    print(f"당신의 BMI는 {bmi:.2f}입니다.")
