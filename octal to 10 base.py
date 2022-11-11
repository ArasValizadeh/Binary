octal = input ('enter your number : ')
octal = octal [::-1]
sum = 0
arzesh_makani = 0
for i in  octal :
    i  = int(i)
    sum += i*8**arzesh_makani
    arzesh_makani += 1
print ('your 10 base number is : ', sum)
