from datetime import datetime
current = datetime.now()
bornyear = input("When were you born (in year)?: ")
print(f'You are', current.year - int(bornyear), 'years old')