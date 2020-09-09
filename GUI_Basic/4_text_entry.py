from tkinter import *

root = Tk()
root.title('Nado GUI') # 상단바에 이름
root.geometry('640x480')

txt = Text(root, width = 30,  height = 5) # 텍스트 창 생성 - 여러줄 
txt.pack()

txt.insert(END, '글자를 입력하세요.') # 기본값 미리 제공 ( 끝까지 )

e = Entry(root, width = 30) # 한줄로 입력 받음(로그인 - id, pw 등...)
e.pack()
e.insert(0, '한줄만 입력해요') # insert 할 때, 처음부터 넣어야 하기 때문에 0을 넣어줌

def btncmd():
    # 내용 출력
    print(txt.get('1.0', END))  # 1 : 첫번쨰 라인, 0 : 0번째 column 위치 // 처음부터 끝까지 가져옴
    print(e.get()) # entry 는 이게 끝

    # 내용 삭제
    txt.delete('1.0', END)
    e.delete(0, END)


btn = Button(root, text = '클릭' , command =  btncmd)
btn.pack()


root.mainloop() # 창이 닫치지 않도록 해줌.


