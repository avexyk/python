import datetime
# from datetime import date
# from datetime import datetime

# print(datetime.date(2019, 01, 01))

# print(datetime.datetime(2019, 1, 1))

# print(datetime.date(2019, 2, 29))
# print(datetime.datetime(2019, 1, 1, 09, 10, 12))
# print(datetime.datetime(2019, 1, 1, 24, 10, 35))

# print(datetime.datetime(2019, 1, 1, 12, 10, 35))

# print(date(2019, 12, 31).isoformat())


# date_time = datetime.datetime(2019, 2, 27, 11, 15, 30)
# print(date_time.strftime('%d/%m/%y %H:%M'))

# date_time = '2019-01-30 15:30:45'
# print(date_time)

# fecha = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')
# print(type(fecha))

# datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S.%f')
# date_time.strftime('%Y-%m-%d %H:%M:%S')
# date_time.strptime('%Y-%m-%d %H:%M:%S')

# ayer1 = datetime.datetime.today() - datetime.timedelta(days=1)
# print(ayer1)

# ayer2 = datetime.date.today() - datetime.timedelta(seconds=86390)
# print(ayer2)

# ayer3 = datetime.datetime.now() - datetime.timedelta(days=1)
# print(ayer3)

# ayer4 = datetime.date.today() - datetime.timedelta(seconds=86900)
# print(ayer4)

# ayer5 = datetime.date.today() - datetime.timedelta(days=1)
# print(ayer5)

# Final

date_time = datetime.datetime(2010, 8, 25, 10, 35, 15)

uno = date_time.strftime('%Y/%m/%d %H:%M:%S')
# dos = date_time.strptime('%Y/%m/%d %H:%M:%S')
# tres = date_time.strftime('%y/%m/%d %H:%M:%S')
# cuatro = date_time.strftime('%Y/%m/%d %H:%M:%s')

print(uno)
# print(dos)
# print(tres)
# print(cuatro)