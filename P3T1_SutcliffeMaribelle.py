# CTI 110
# P3T1: Areas of Rectangles
# Name: Maribelle Sutcliffe

print ("This program will calculate the area of two rectangle.")
width1 = int(input("Enter the width of the first rectangle: "))
height1 = int(input("Enter the height of the first rectangle: "))
area1 = width1 * height1
print("The area of the first rectangle is:",area1)
width2 = int(input("Enter the width of the second rectangle: "))
height2 = int(input("Enter the height of the second rectangle: "))
area2 = width2 * height2
print("The area of the second rectangle is:",area2)
if area1 > area2:
    print("The area of the first rectangle is greater.")
elif area1 < area2:
    print("The area of the second rectangle is greater.")
elif area1 == area2:
    print("The area of both rectangles are equal")
    
