a = '{:.10}'.format('Python Tutorial') # ตัดคำตั้งแต่ตัวอักษรตัวที่ 10 ออก
print(a)

a2 = '{:.{}}'.format('Python Tutorial', 10)
print(a2)

b = '{:10.10}'.format('Python0123456789')
print(b)

c = '{:d}'.format(30)
print(c)

d = '{:f}'.format(3.14689323899)
print(d)

e = '{:5d}'.format(39)
print(e)

f = '{:05.2f}'.format(6.12345678123)
print(f)