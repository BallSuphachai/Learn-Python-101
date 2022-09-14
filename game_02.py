#pseudo-code --> code
from tkinter import * # import ทุกสิ่งอย่างใน tkinter มาใช้
import random
import time

window = Tk()
window.title('Game Tai Si Ja')
window.geometry('700x840')

#ตัวแปรที่ระบุสถานะของเกม
game_finished = False #เริ่มต้นเกมยังไม่จบ
score = 0
lives = 3

#แสดง score และ live บน window
status_str = StringVar() #มาจาก Tkinter
status_str.set('Score: ' + str(score) + ' | ' + 'Lives: ' + '❤️'*lives)
show_status = Label(window, textvariable=status_str)
show_status.pack(pady=20)

word_dict = {
    'ball':
        {'category': 'นักพัฒนาเกม',
         'hints': ['ชอบ k-pop', 'เมนจีซู', 'ชอบเยจี']
        },
    'jisoo':
        {'category': 'k-pop',
         'hints' : ['blackpink', 'ตลก', 'นักแสดง']
        },
    'yeji':
        {'category': 'k-pop',
         'hints' : ['itzy', 'ซุ่มซ่าม', 'เพลิงนวล']
        },
    }
words = list(word_dict.keys())

#ฟังก์ชั่นสุ่มคำและสร้าง clue ['','',....,'']
def get_new_secret_word():
    random.shuffle(words)  # shuffle หรือสลับตำแหน่งคำใน words เหมือนสับไพ่
    secret_word = words.pop()
    clue = list('?' * len(secret_word))
    return secret_word, clue

secrets_word, clue = get_new_secret_word()

#แสดง category และ clue บน window
category_str = StringVar()
category_str.set(word_dict[secrets_word]['category'])
show_category = Label(window, textvariable=category_str, font=('Arial', 50))
show_category.pack(pady=10)

clue_str = StringVar()
clue_str.set(' | '.join(clue))
show_clue = Label(window, textvariable=clue_str, font=('Arial', 50))
show_clue.pack(padx=10, pady=30)
#แสดง hints
hints = word_dict[secrets_word]['hints']
hint_text = StringVar()
hint_text.set('Hints')
hint_str = StringVar()
hint_str.set('\n'.join(hints))

show_hint_text = Label(window, textvariable=hint_text, font=('Arial Bold', 28))
show_hint_text.pack()
show_hints = Label(window, textvariable=hint_str, font=('Arial', 28))
show_hints.pack(pady=10)

#กล่องให้กรอก guess
textentry = Entry(window, width=5, borderwidth=1, font=('Arial', 50), justify='center')
textentry.pack()

#ปุ่มกด submit พร้อมฟังก์ชันที่อัพเดต clue และสถานะของเกม

def update_clue(guess, secret_word, clue):
    #guess ไล่ไปทีละตัวอักษรใน secret_word ดูว่ามีตัวไหนบ้างตรงกับที่ทาย
    for i in range(len(secret_word)): #Loop ตามจำนวนตัวอักษรในsecret_word
        #ถ้าทายตรงตัวไหน ก็อัพเดต clue ตรงตำแหน่งนั้น
        if guess == secret_word[i]:  #ถ้า guess ที่ป้อนเข้ามาตรงกับตำแหน่งที่ i
            clue[i] = guess #ใส่ guess เข้าใน clue ตำแหน่งที่ i

    clue_str.set(' | '.join(clue))
    win = ''.join(clue) == secret_word #joinตัวอักษรใน clue ให้เป็นคำแล้วเทียบกับ secret_word ว่าตรงกันไหม
    return win #ทายจนไม่เหลือ '?' แล้ว --> True, ยังเหลือ --> False

def update_screen():
    #ประกาศตัวแปลพวกนี้ให้เป็น global เพื่อให้ฟังก์ชันนี้เข้าถึงตัวแปลนอก command ได้
    global game_finished, score, lives, secrets_word, clue, hints

    guess = textentry.get().strip() #Strip to remove whitespaces
    guess = guess.lower() #lowercase

    if guess in secrets_word:
        win = update_clue(guess, secrets_word, clue)
        if win:
            print('เย่! คำนั้นคือ: ' + secrets_word)
            score = score + 1
            print('score: ' + str(score))
            clue_str.set('Yay! Answer: ' + secrets_word)
            window.update()
            time.sleep(2) #ทำให้โปรแกรมค้างไว้ 2 วินาที

            if len(words) == 0:
                game_finished = True
                clue_str.set('Congrats!')
            else:
                secrets_word, clue = get_new_secret_word()
                category_str.set(word_dict[secrets_word]['category'])
                clue_str.set(' | '.join(clue))
                hints = word_dict[secrets_word]['hints']
                hint_str.set('\n'.join(hints))

    else:
        print('ผิด! เลือดลด')
        lives = lives - 1
        if lives < 1:
            clue_str.set('Game Over!')
            game_finished = True

    status_str.set('Score: ' + str(score) + ' | ' + 'Lives: ' + '❤️'*lives)
    textentry.delete(0, 'end')

submit_btn = Button(window, text='Submit', command=update_screen)
submit_btn.pack()

#โปรแกรมหลักที่ check ว่าเกมจบแล้วหรือยัง

def main():
    if not  game_finished:
        window.after(1000, main)
    else:
        submit_btn['state'] = 'disable'
        print('Quitting...')
        window.quit()

window.after(1000, main)
window.mainloop()

#จบเกม
print('End Game')