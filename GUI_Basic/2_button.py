from tkinter import *

root = Tk()
root.title('Nado GUI') # 상단바에 이름
root.geometry('640x480')
btn1 = Button(root, text= '버튼1') # 버튼 만들기
btn1.pack() # 버튼 포함 시키기

btn2 = Button(root, padx = 5, pady = 10 , text = '버튼2222222222222') # 글자가 많아지면 크기가 널어진다.
btn2.pack()

btn3 = Button(root, padx = 10, pady = 5 , text = '버튼3')
btn3.pack()

btn4 = Button(root, width = 10, height = 3, text = '버튼44444444444') # 틀자체가 고정
btn4.pack()

btn5 = Button(root, fg ='red', bg = 'yellow', text= '버튼5') # fg : 글자색, bg : 배경색
btn5.pack()

photo = PhotoImage(file ='img.png')
btn6 = Button(root, image=photo)
btn6.pack( )

def btncmd():
    print('버튼이 클릭되었어요.')

bnt7 = Button(root, text= '동작하는 버튼 ', command= btncmd)
bnt7.pack()

# padx = , pady = : 여백 , width = , height = : 크기


root.mainloop() # 창이 닫치지 않도록 해줌.


