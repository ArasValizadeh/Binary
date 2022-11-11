import math
def reverse(num):
    return num[::-1]

number = int(input('enter your number : '))
kharej = number
hasel =''

while kharej >= 8 :
    hasel = hasel + str(kharej%8)
    kharej = math.floor(kharej/8)

hasel += str(kharej)
hasel = reverse(hasel)
print(hasel)
