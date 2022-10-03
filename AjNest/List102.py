color_list = ["Red", "Blue", "Green", "Black"]
print(color_list[0])
print(color_list[1])
print(color_list[2])
print(color_list[3])

#Add an item to the list
color_list.append("White")
print(color_list)

#Insert an item at a given position
color_list.insert(2,"Grey") #แทรก "Grey" ไปที่ตำแหน่งที่ 2
print(color_list)

#Modify an element using the index of the he element
color_list[2] = "Pink"
print(color_list)

#Remove an item from the list
color_list.remove("Black")
print(color_list)

#Remove all items from the list
color_list.clear()
print(color_list)