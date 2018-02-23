#CTI 110
# P3LAB - Calculate Students Grade
# Sutcliffe
#February 23, 2018


A_score = 90
B_score = 80
C_score = 70

 
score = int(input('Enter grade: '))
if score >= A_score:
    print('Your grade is: A')
elif score >= B_score:
    print('Your grade is: B')
elif score >= C_score:
    print('Your grade is: C')
else:
    print('Your grade is: F')

