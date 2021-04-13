from datetime import datetime, date, time, timedelta
import locale

# d1 = date(2020, 3, 12)
# print(d1)
# print(d1.year)
# print(d1.month)
# print(d1.day)

# t1 = time(23, 10, 59)
# print(t1)
# print(t1.hour)
# print(t1.minute)
# print(t1.second)

# print(date.max)
# print(date.min)

# print(time.max)
# print(time.min)

# dt = datetime(2020, 3, 12, 15, 17)
# print(dt)

# print(dt.date().year)

# print(dt.time().hour)


# print(datetime.max)
# print(datetime.min)

now  = datetime.now()
# print(now)
# print(now.year)
# print(now.month)

# new_dt = now.replace(year = 2019)
# print(new_dt)
# print(now)

# dt = datetime.strptime("30/08/2019", "%d/%m/%Y")
# print(dt)

# dt = datetime.strptime('29/03/2020 10:40', '%d/%m/%Y %H:%M')
# print(dt)

# dt = datetime.strptime('06-08-2018 09:20', '%m-%d-%Y %H:%M')
# print(dt)

# dt = datetime.strptime('2018-06-28', '%Y-%m-%d')
# print(dt)


# now = datetime.now()
# print(now.strftime('%Y-%m-%d (%a)'))
# print(now.strftime('%Y %B %d number day (%A)'))

delta1 = timedelta(days = 3, hours=2, minutes=10)
print(delta1)

delta2 = timedelta(days=2, hours=1, minutes=5)
print(delta2)

print(delta1 - delta2)
print(delta2 - delta1)

my_birthday = date(1995, 8, 4)

delta = date.today() - my_birthday
print(type(delta))

my_age = int(delta.days/365)
print(my_age)

wife_birthday = date(1996, 8, 4)
am_i_older = my_birthday < wife_birthday
print(am_i_older)

