setA = {1, 2, 3, 4, 5, 6,}
setB = {2, 3, 4, 5, 6, 7, 8}
print(setA|setB)
print(setA&setB)

def triangle():
    base = input("Please enter your Base value ")
    height = input("Please enter your height value ")
    area = float(base)*float(height)*float(0.5)
    print("The area of your triangle is" , area)
triangle()

print("The time complexity is 0(n) and the space complexity is O(n)")
