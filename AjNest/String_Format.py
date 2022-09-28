names = "ball"
pet = "cat"

syn = "My name is {} and i have {}".format(names, pet)
print(syn)

syn2 = "The {1} are {0} pet".format(names,pet)
print(syn2)

syn3 = '{:>20}'.format('Python') #ข้อความชิดขวา 20 ช่อง (นับตัวมันเองด้วย)
print(syn3)

syn4 = '{:15}'.format('Pythonn')
print(syn4)

syn5 = '{:*>15}'.format('Python') #ข้อความชิดขวา 15 ช่อง (นับตัวมันเองด้วย) แล้วใส่ * ในช่องว่าง 
print(syn5)

syn5 = '{:*<15}'.format(names) #ข้อความชิดซ้าย 15 ช่อง (นับตัวมันเองด้วย) แล้วใส่ * ในช่องว่าง
print(syn5)

syn6 = '{:^16}'.format(names) #ข้อความอยู่กลาง ของความกว้าง 16
print(syn6)