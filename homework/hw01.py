import math



def distance(rate, time):
    distanceAns = rate*time
    print("Your distance is " , distanceAns)

def rate(distance, time):
    rateAns = distance/time
    print("Your rate is " , rateAns)


def time(distance, rate):
    timeAns = distance/rate
    print("Your time is " , timeAns)

want = input("what are you trying to calculate for? (r, t, or d) ")

try:
    if want == 'r':
        distanceIn = float(input("What is your distance? (Miles) "))
        timeIn = float(input("What is your time? (Hours) "))
        rate(distanceIn, timeIn)

    elif want == 't':
        distanceIn = float(input("What is your distance? (Miles) "))
        rateIn = float(input("What is your rate? (Mph) "))
        time(distanceIn, rateIn)
    elif want == 'd':
        timeIn = float(input("What is your time? (Hours) "))
        rateIn = float(input("What is your rate? (Mph) "))
        distance(rateIn, timeIn)
    else:
        print("Not a viable option, try r, t, or d ")

except:
    print("Bad input")
