import tank

first_tank = tank.Tank('t1', 3)
first_tank.fire_ammo()#ยิง!
print(first_tank.ammo)#เหลือ 2 นัด

first_tank.fire_ammo()#ยิง!
first_tank.fire_ammo()#ยิง!
print(first_tank.ammo)#เหลือ 0 นัด

first_tank.add_ammo(4)
print(first_tank.ammo)
