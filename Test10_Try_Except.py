#ถ้า error จากข้อมูลใน try: จะถูกส่งไปยัง execept:
try:
    x = int(input('X = '))
    y = int(input('Y = '))
    if x == 0:
        raise Exception() #คืนค่าไปที่ except: ด้านล่าง
    z = x / y
    print(z)
except:
    print('กรอกข้อมูลไม่ถูกว้อยย!')

print('หล่อเท่!!')
