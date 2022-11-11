import math
def my_function(x):
  return x[::-1]

num = int(input('enter your number : '))
kharej = num
hasel = ''

while kharej >= 2 :
    hasel = hasel + str(kharej%2)
    kharej=math.floor(kharej/2)

hasel = hasel + str (kharej)
binary=my_function(hasel)
print(binary)
