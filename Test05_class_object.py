class elem_fish:
    def __init__(self, name, hitpoint, attack, defend):
        self.name = name
        self.hitpoint = hitpoint
        self.attack = attack
        self.defend = defend

first_fish = elem_fish('earth', 1000, 100, 40)
print(first_fish.name)

second_fish = elem_fish('water', 700, 150, 25)
print(second_fish.name)

third_fish = elem_fish('wind', 500, 200, 20)
print(third_fish.name)

fourth_fish = elem_fish('fire', 400, 400, 10)
print(fourth_fish.name)

#แก้ไขข้อมูลในคลาส
third_fish.name = 'storm'
third_fish.attack += 25

#แสดงข้อมูล
fish3 = str(third_fish.name + ' ' +
            str(third_fish.hitpoint)+ ' '
            + str(third_fish.attack)+ ' '
            + str(third_fish.defend)+ ' '
            )
print(fish3)