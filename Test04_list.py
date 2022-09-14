quests = ['ทักทายเพื่อน','ยืมเบ็ดตกปลา','เก็บหนอน']
for i in range(len(quests)):
    print(str(i + 1) + '. ' + quests[i])

# รับค่าจากการทำเควส และแสดงผล
quests_do_it = ''
while quests_do_it != ('ทักทายเพื่อน') :
    quests_do_it = str(input())
    if quests_do_it == ('ทักทายเพื่อน'):
        print('สวัสดีเพื่อนรัก!\nวันนี้อากาศดีมาก ไปตกปลากันเถอะ')
        break
    else:
        print('ไม่มีอะไรเกิดขึ้น')
