import random

slist = [7,1,5,3,6,4]
minimumprice = slist[0]
price = slist[0]
difs = []

for i in slist:
    if i < minimumprice:
         minimumprice = i
    price = i
    dif = price-minimumprice
    difs.append(dif)
    #print(dif)
print("Your maximum profit is" , max(difs))
    #[3,99,1,2]
