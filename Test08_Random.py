import random

damage = random.randint(50, 60) #Random จำนวนเต็ม random.randint(ค่าน้อยที่สุด, ค่ามากที่สุด)
percent = random.uniform(0, 100) #Random จำนวนทศนิยม random.uniform(ค่าน้อยที่สุด, ค่ามากที่สุด)

if percent <= 25: #โอกาศติดคริ 25 %
    damage *= 2 #ติดคริ หมายถึง damage คูณสอง
print('ทำดาเมจ:', damage)
print()

moneys = [0, 20, 100, 1000]
money = random.choice(moneys) #Random แบบสมาชิกจาก List [0, 20, 100, 1000]
print('สุ่มได้เงินรางวัล:', money)

print()
random.shuffle(moneys) #Random สลับลำดับตำแหน่งสมาชิกจาก List
print(moneys)
moneys = [0, 20, 100, 1000] #set ตำแหน่งใหม่ให้เป็นเหมือนเดิม
print(moneys)

