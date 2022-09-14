#pseudo-code --> code
import random

#ตัวแปรที่ระบุสถานะของเกม
score = 0
lives = 3
words = ['ball', 'jisoo', 'yeji']
hint = {'ball':['นักพัฒนาเกม'],
        'jisoo':['สวย','ตลก'],
        'yeji':['ซุ่มซ่าม' ,'เพลิงนวล']
        }

def update_clue(guess, secret_word, clue):
    #guess ไล่ไปทีละตัวอักษรใน secret_word ดูว่ามีตัวไหนบ้างตรงกับที่ทาย
    for i in range(len(secret_word)): #Loop ตามจำนวนตัวอักษรในsecret_word
        #ถ้าทายตรงตัวไหน ก็อัพเดต clue ตรงตำแหน่งนั้น
        if guess == secret_word[i]:  #ถ้า guess ที่ป้อนเข้ามาตรงกับตำแหน่งที่ i
            clue[i] = guess #ใส่ guess เข้าใน clue ตำแหน่งที่ i
    win = ''.join(clue) == secret_word #joinตัวอักษรใน clue ให้เป็นคำแล้วเทียบกับ secret_word ว่าตรงกันไหม
    return win #ทายจนไม่เหลือ '?' แล้ว --> True, ยังเหลือ --> False

#ตราบใดที่ยังมีคำให้ทายอยู่ และ ชีวิตยังเหลือ --> เล่นต่อไป
while (len(words) > 0) and (lives > 0):
    #สุ่มคำจาก words แล้วดึงคำนั้นออกจาก list
    random.shuffle(words) #shuffle หรือสลับตำแหน่งคำใน words เหมือนสับไพ่
    secret_word = words.pop()
    key_hint = hint[secret_word] #คำใบ้ใน hint ที่ตรงกับ secret_word
    clue = list('?'*len(secret_word)) #จำนวน '?' เท่ากับตัวอักษรของ secret_word

    #ตราบใดที่ยังทายคำนี้ไม่เสร็จหรือชีวิตยังไม่หมด
    while True: # Infinite Loop จนกว่าจะมีการ break
        print(clue)
        print(key_hint)
        print('ชีวิตที่เหลือ: ' + str(lives))
        guess = input('ทายตัวอักษรมาซิ: ')

        #check ว่าตัวอักษรที่ทาย อยู่ใน secret_word หรือไม่
        if guess in secret_word:
           win = update_clue(guess, secret_word, clue)
           if win:
               print('ถูกต้อง! คำนั้นก็คือ: ' + secret_word)
               score = score + 1
               print('Score: ' + str(score))
               break
        else:
            print('ผิด! เลือดลด')
            lives = lives - 1
            if lives == 0:
                print('เจ้าแพ้แล้ว!')
                print('คำนั้นคือ: ' + secret_word)
                break  # ตาย!

print('Final score: ' + str(score))
print('Game end!')