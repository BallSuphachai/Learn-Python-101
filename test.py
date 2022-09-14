status = False
while status == False:
    username = input("Username: ")
    password = input("Password: ")
    if (username == "admin") and (password == "1234"):
        status = True
        print("รหัสผ่านถูกต้อง")
        break
    print("รหัสผ่านไม่ถูกต้อง\n")
print("ยินดีต้อนรับ ><")