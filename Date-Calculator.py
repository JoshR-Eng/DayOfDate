# Import Packages
import random 

# Set variables
month31 = [1, 3, 5, 7, 8, 10, 12]
monthValues = [4, 0, 0, 3, 5, 1, 3, 6, 2, 4, 0, 2]
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']


"""
FUNCTIONS
"""
    # Func. to calculate day of the date
def calculate(date, month, year):
    date,month,year = int(date),int(month),int(year)

    if month < 3:
        month += 12
        year -= 1

    day = date
    decade = year % 100
    century = year // 100

    formula = (
        (day + ((13 * (month+1)) // 5) + decade + (decade // 4) 
        + (century // 4) - (2 * century)) % 7 
        )
    
    return days[formula]

    # Func. to determine if it's a leap year
def leapYear(year):
    year = int(year)
    return (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0)



"""
Loop
"""

i = 0       # Set loop counter to 0
score = 0   # Set Score to 0

# Calculate 10 dates 
while i <= 10:
    # Generate random date
    year = random.randint(1600,2100)
    month = random.randint(1,12)
    if month == 2 and leapYear(year):
        date = random.randint(1,29)
    elif month == 2:
        date = random.randint(1,28)
    elif month in month31:
        date = random.randint(1,31)
    else:
        date = random.randint(1,30)

    print(f"\n{date:02}.{month:02}.{year}")
    calcAns = calculate(date, month, year)

    userAns = input("\tDay of the week: ").strip()
    
    if userAns.title() == calcAns:
        print('Correct!')
        score +=1
    else:
        print('Wrong! - ' + calcAns)

    i += 1

print(f'You got {score} out of 10')



