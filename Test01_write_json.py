print("อ่ะจ๊ะเอ๋ตัวเอง! ท่านผู้เจริญซึ่งมากไปด้วยปัญญา!")
import json
prog_dict = {
    "name" : "Python",
    "author" : "Guido Van Rossum",
    "year" : 1990,
    "frameworks" : ["Flask","Django"],
    "libraries" : ["Pandas","Numpy","Matplotlib","Requests"]
}
with open('data22.json','w') as json_file:
    json.dump(prog_dict, json_file,indent=4)

print(type(prog_dict))
