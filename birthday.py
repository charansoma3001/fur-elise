import datetime
# from datetime import date, datetime

print("enter birthday: ")
y, m, d = input()
birth = datetime.date(y, m, d)
today = datetime.date.today()

if(today.month == birth.month and today.day>=birth.day or today.month>birth.month):
    nextYear = today.year + 1
else:
    nextYear = today.year

nextBirth = datetime.date(nextYear,today.month,today.day)
diff=nextBirth-today
print(diff.days)
