import math
def reverse(num):
    return num[::-1]

number = int(input('enter your number : '))
kharej = number
hasel =''

numbers={15:'F',14:'E',13:'D',12:'C',11:'B',10:'A',9:'9',8:'8',7:'7',
6:'6',5:'5',4:'4',3:'3',2:'2',1:'1'}

while kharej >=16 :
    baghi = kharej%16
    hasel += numbers[baghi]
    kharej = math.floor(kharej/16)

hasel += numbers[kharej]
hasel = reverse(hasel)
print(hasel)
