# 좋아하는 수를 입력하시오 4
# 또 좋아하는 수를 입력하시오 5
# 4와 5의 합은 9입니다.

# a = int(input("좋아하는 수를 입력하시오 "))
# b = int(input("또 좋아하는 수를 입력하시오 "))
#
# sum = a+b
#
# print(a, "와", b, "의 합은 ", sum, "입니다.")


a = input("좋아하는 수를 입력하시오 ")
b = input("또 좋아하는 수를 입력하시오 ")

aa = int(a)
bb = int(b)
sum = aa+bb

print(a +"와 " + b +"의 합은 " + str(sum) +"입니다.")
print("{}와 {}의 합은 {}입니다.".format(a,b,sum))
