#CTI 110
#P3HW1 - Age Classifier
#Maribelle Sutcliffe
#February 23, 2018

age = int(input("Please enter your age: "))
if age <= 1:
    print("You are an infant")
elif age < 13:
    print("You are a child")
elif age < 20:
    print("You are a teenager")
elif age >= 20:
    print("You are an adult")
