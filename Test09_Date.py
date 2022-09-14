import datetime as dt
#ห้ามตั้งชื่อไฟล์เป็น datetime.py เพราะเป็นชื่อของ Module

date1 = dt.datetime(year=2022, month=2, day=14) #วันเวลาแบบกำหนดเอง
date2 = dt.datetime.now() #วันเวลาแบบปัจจุบัน

days = dt.timedelta(days=25) #ระยะเวลาแบบกำหนดเอง
date3 = date1 + days #คำนวนวันเวลา

days2 = date2 - date1
print(days2)
print()
print(date1.strftime('%A %d, %B %Y')) #https://www.w3schools.com/python/python_datetime.asp
