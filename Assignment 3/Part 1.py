#Jason Guan
#U9893-2926
#Program intended to predict the approximate population size of organisms

StartNum = int(input('Starting number of organisms:'))

while StartNum < 1:
    StartNum = int(input('Starting number of organisms:'))

DailyIncrease = int(input('Average daily increase (as a %):'))


while DailyIncrease < 1:
    DailyIncrease = int(input('Average daily increase (as a %):'))

NumDays = int(input('Number of days to multiple:'))

while NumDays < 1:
    NumDays = int(input('Number of days to multiple:'))

PercentageIncrease = DailyIncrease / 100
OutputDay = 1

print("Day \t\t Population")
print('---------------------------')
for day in range(1, NumDays + 1):
    print(f'{day} \t\t {StartNum:.6f}')
    StartNum = StartNum + (PercentageIncrease * StartNum)

    
    
    
