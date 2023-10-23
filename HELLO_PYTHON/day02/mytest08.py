# 출력할 구구단을 입력하세요 7
# 7 * 1 = 7
# 7 * 9 = 63

dan = input("출력할 구구단을 입력하세요 ")
idan = int(dan)

for i in range(1, 9+1):
    print("{} * {} = {}".format(dan,i,i*idan))
    
# print("{} * {} = {}".format(dan,1,1*idan))
# print("{} * {} = {}".format(dan,2,2*idan))
# print("{} * {} = {}".format(dan,3,3*idan))
# print("{} * {} = {}".format(dan,4,4*idan))
# print("{} * {} = {}".format(dan,5,5*idan))
# print("{} * {} = {}".format(dan,6,6*idan))
# print("{} * {} = {}".format(dan,7,7*idan))
# print("{} * {} = {}".format(dan,8,8*idan))
# print("{} * {} = {}".format(dan,9,9*idan))
    