# 첫수를 입력하시오 1
# 끝수를 입력하시오 10
# 배수를 입력하시오 5
# 1에서 10까지 5의 배수의 합은 15입니다.

# a = int(input("첫 수를 입력하시오 "))
# b = int(input("끝 수를 입력하시오 "))
# c = int(input("배수를 입력하시오 "))
#
# sum = 0
# for i in range(a, b+1):
#     if i % c == 0:
#         sum += i
#
# print(a, "에서 ", b, "까지 ", c, "의 배수의 합은 ", sum, "입니다." )

a = input("첫 수를 입력하시오 ")
b = input("끝 수를 입력하시오 ")
c = input("배수를 입력하시오 ")

aa = int(a)
bb = int(b)
cc = int(c)

sum = 0
for i in range(aa, bb+1):
    if i%cc ==0:
        sum += i

print("{}에서 {}까지 {}의 배수의 합은 {}입니다.".format(a,b,c,sum))