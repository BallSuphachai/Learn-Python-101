color_list = ["Red", "Blue", "Green", "Black"]
print(color_list[0:2])
print(color_list[1:2])
print(color_list[1:-1])
print(color_list[:3])
print(color_list[:])

col = color_list.pop(2)
print(col)
print(color_list)

print(color_list.index("Red")) 

color_list = ["Red", "Blue", "Green", "Black"]
print(color_list)
color_list.append("Green")
print(color_list)
color_list.append("Green")
print(color_list)
print(color_list.count("Green"))