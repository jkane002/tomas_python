import random
slist = []

#make random intergers not input

def inp():
    stock1 = input("please input your first number: ")
    slist.append(stock1)
    stock2 = input("please input your second number: ")
    slist.append(stock2)
    stock3 = input("please input your third number: ")
    slist.append(stock3)
    stock4 = input("please input your fourth number: ")
    slist.append(stock4)
    stock5 = input("please input your fifth number: ")
    slist.append(stock5)
    print("------------------------------------------")
    print(slist)
    conf = input("is this the correct list? y/n ")
    print("------------------------------------------")
    if conf == "y":
        print("Your list has been recorded")
    elif conf == "n":
        slist.clear()
        inp()
    else:
        print(slist)
        conf = input("is this the correct list? y/n ")

inp()
