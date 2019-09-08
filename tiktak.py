from tkinter import *
import tkinter.messagebox
root=Tk()
root.title('tiktak')
root.config(bg='black')
img=PhotoImage(file='c.png')
img1=PhotoImage(file='d.png')
winset=[{1,2,3},{4,5,6},{7,8,9},{1,4,7},{2,5,8},{3,6,9},{1,5,9},{3,5,7}]
def Result():
    for s in winset:
        if s.issubset(pl1):
            tkinter.messagebox.showinfo('result',"player 1 win")
            intial()
            lb1.destroy()
            lb2.destroy()
            return True
        if s.issubset(pl2):
            tkinter.messagebox.showinfo('result',"player 2 win")
            intial()
            lb1.destroy()
            lb2.destroy()
            return True
    return False
            
def change(x):
    global l
    global flag
    global pl1
    global pl2
    global count
    global lb1
    global lb2
    ind=x[0]*3+x[1]
    if flag:
        pl1.add(ind+1)
        l[ind]['image']=img
        flag=False
        lb1.destroy()
        lb2=Label(root,text='Player 2')
        lb2.grid(column=3,row=3,padx=7,pady=7,sticky='news')
    else:
        pl2.add(ind+1)
        l[ind]['image']=img1
        flag=True
        lb2.destroy()
        lb1=Label(root,text='Player 1')
        lb1.grid(column=0,row=3,padx=7,pady=7,sticky='news')
    count=count+1
    if count>=5:
        f=Result()
    if count==9 and f==False:
        tkinter.messagebox.showinfo('result',"match draw")
        intial()
        lb1.destroy()
        lb2.destroy()
def start():
    global lb1
    start["state"]='disable'
    for b in l:
        b['state']='active'
    lb1=Label(root,text='Player 1')
    lb1.grid(column=0,row=3,padx=7,pady=7,sticky='news')
def intial():
    
    global l
    global pl1
    global pl2
    global flag
    global count
    global start
    l=[]
    pl1=set()
    pl2=set()
    flag=True
    count=0
    for i in range(3):
        for j in range(3):
            l.append(Button(root,state='disable',bg='white',bd=10,command=lambda x=(i,j):change(x)))
            l[-1].grid(padx=7,pady=7,sticky='news',row=i,column=j)
    start=Button(root,text='START',bg='white',bd=10,fg='green',font='arial 30 bold',command=start)
    start.grid(row=3,column=1,padx=7,pady=7,sticky='news')
    for i in range(3):
        root.grid_rowconfigure(i,weight=1)
    for i in range(3):
        root.grid_columnconfigure(i,weight=1)
intial()
root.mainloop()
