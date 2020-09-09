from tkinter import *

root = Tk()
root.title('Nado GUI') # 상단바에 이름
root.geometry('640x480')

lable1 = Label(root, text='안녕하세요')
lable1.pack()

photo = PhotoImage(file = 'img.png')
lable2 = Label(root, image= photo)
lable2.pack()

def change():
    lable1.config(text ='또 만나요')

    global photo2 # 전역 변수로 선언해줘야 함.
    photo2 = PhotoImage(file = 'x.png')
    lable2.config(image = photo2)

btn = Button(root, text='클릭' , command= change)
btn.pack()

root.mainloop() # 창이 닫치지 않도록 해줌.


