#P4HW1
#Distance Travveled
#Sutcliffe
#March 25, 2018

speed = float(input('What is the speed of the vehicle in mph?'))
time = int(input('How many hours has it traveled?'))

print('Hour','\tDistance Traveled')
for Hour in range(1, time + 1 ):
    distance = speed * Hour
    print(Hour,'\t',distance)
