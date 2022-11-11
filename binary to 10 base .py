num = input('enter your number : ')
num = num [::-1]
sum = 0
arzesh_makani = 0
for i in num :
    i = int(i)
    sum += i * 2**arzesh_makani
    arzesh_makani += 1

print ('your binary code in 10 base is : ', sum)
