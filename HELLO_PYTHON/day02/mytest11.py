# 첫 수를 입력하세요 7
# 끝 수를 입력하세요 9
# 7은 9보다 2만큼 작다
# 9은 7보다 2만큼 크다
# 같은 숫자입니다

# num1 = int(input("첫 수를 입력하세요 "))
# num2 = int(input("끝 수를 입력하세요 "))
#
# if num1 < num2:
#     differ = num2 - num1
#     print("{}은 {}보다 {}만큼 크다".format(num2, num1, differ))
# elif num1 > num2:
#     differ = num1 - num2
#     print("{}은 {}보다 {}만큼 작다".format(num2, num1, differ))
# else:
#     print("같은 숫자 입니다.")

a = input("첫 수를 입력하세요 ")
b = input("끝 수를 입력하세요 ")

aa = int(a)
bb = int(b)

if aa>bb:
    min = aa - bb
    print("{}은 {}보다 {}만큼 크다".format(a,b,min))
elif aa<bb:
    min = bb - aa
    print("{}은 {}보다 {}만큼 작다".format(a,b,min))
else:
    print("같은 숫자입니다.")
