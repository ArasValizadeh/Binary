hexa= input ('enter your number : ')
hexa = hexa [::-1]
print ('hexa is ',hexa)
sum = 0
arzesh_makani = 0
for i in hexa :
    if i == 'A' or i == 'a':
        sum += 10*16**arzesh_makani
    elif i == 'B' or i == 'b':
        sum += 11*16**arzesh_makani
    elif i == 'C' or i == 'c':
        sum += 12*16**arzesh_makani
    elif i == 'D' or i == 'd':
        sum += 13*16**arzesh_makani
    elif i == 'E' or i == 'e':
        sum += 14*16**arzesh_makani
    elif i == 'F' or i == 'f':
        sum += 15*16**arzesh_makani
    else :
        i = int(i)
        sum += i*16**arzesh_makani
    arzesh_makani += 1
print(sum)
