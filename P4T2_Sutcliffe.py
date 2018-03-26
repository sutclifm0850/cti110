#P4T2
#Bug Collector
#Sutcliffe
#March 25, 2018

total = 0

for day in range (1, 8):
    print('Enter the bugs collected on day', day)
    bugs = int(input())
    total = total + bugs

print('You collected a total of', total, 'bugs.')    
