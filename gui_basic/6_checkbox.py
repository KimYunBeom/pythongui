from msilib.schema import ListBox
from tkinter import *

root = Tk()
root.title('Nado GUI')
root.geometry('640x480+800+200')

chkvar = IntVar() # chkvar에 int형으로 값을 저장한다
chkbox = Checkbutton(root, text='오늘 하루 보지 않기', variable=chkvar)
# chkbox.select() # 기본 선택 처리
# chkbox.deselect() # 기본 선택해제 처리
chkbox.pack()


chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text='일주일 동안 보지 않기', variable=chkvar2)
chkbox2.pack()

def btncmd():
  print(chkvar.get()) # 0 : 체크해제, 1 : 체크
  print(chkvar2.get())

btn = Button(root, text='클릭', command=btncmd)
btn.pack()

root.mainloop()
