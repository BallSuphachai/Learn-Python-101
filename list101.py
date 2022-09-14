from operator import index


list_a = ["dog", "cat", "fish", "bear", "sneak"]
list_b = [1, 2, 3, 4, 5]

print(list_a)
pet_inp = input("input new pet: ")
new_pet = list_a.append(pet_inp)
print(list_a)
print("New pet is a",list_a[len(list_a)-1])
print("Pet number is",len(list_a),"\n")

rem = str(input("remove: "))
list_a.remove(rem)
print(list_a)
print("Pet number is",len(list_a),"\n")

popup = int(input("Buy some pet by number of pet:"))
print(list_a.pop(popup),"Pop up to sell!")
