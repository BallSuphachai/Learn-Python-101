a = '{:.10}'.format('Python Tutorial') # ตัดตัวอักษรให้ถึงตำแหน่งที่ 10
print(a+"|<----")

a2 = '{:.{}}'.format('Python Tutorial', 10) # ตัดตัวอักษรให้ถึงตำแหน่งที่ {Argument}
print(a2)

b = '{:12.10}'.format('Python Tutorial999') # ความกว้าง 12 และ ตัดตัวอักษรให้ถึงตำแหน่งที่ 10
print(b+"|<----")

# https://www.w3schools.com/python/ref_string_format.asp
c = '{:d}'.format(0b101) # {:d} หมายถึง Decimal format 
print(c)

d = '{:f}'.format(3.14689323899) # Fix point number format (float)
print(d)

e = '{:5d}'.format(39) # เลื่อนไป 5 ตำแหน่ง
print(e)

f = '{:9.2f}'.format(6.12345678123) # ต้องการทศนิยม 2 ตำแหน่ง ในรูปแบบความกว้าง 9 ตัว
print(f) 

#Signed Numbers
i = '{:+d}'.format(39)
print(i)
j = '{: d}'.format((-30))
print(j)
k = '{: d}'.format(39)
print(k)

#Named Placeholders การแทนที่
data = {'first': 'Ball', 'last': 'Suphachai'}
l = '{first}_{last}'.format(**data)
print(l)
m = '{first}{last}'.format(first='Aj.',last='NesT')
print(m)

# Date Time
from datetime import datetime
dt = '{:%Y-%m-%d %H:%M}'.format(datetime(2020, 8, 26, 10, 38))
print(dt)

