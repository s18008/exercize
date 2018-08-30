import tkinter,random
quiz = [('1+1=','1','2','3','4',2),('2+2=','4','6','8','10',1)]
Q = random.sample(quiz,len(quiz))
Next = 0

root = tkinter.Tk()
root.title(u"Software Title")
root.geometry("400x300")

def nest(number):
    def Decision():
        global Next,Static
        if number == Q[Next][5]:
           ## Static = tkinter.Label(text='正解')
            Static.config(text="正解")
            ##Static.pack()
        else:
            ##Static = tkinter.Label(text='不正解')
            ##Static.pack()
            Static.config(text="不正解")
        sel = tkinter.Button(text="次の問題へ",width=50,command=lambda: sel.pack_forget())
        sel.pack()
    return Decision

Static = tkinter.Label(text=Q[Next][0])
Static.pack()
for i in range(1,5):
    Button = tkinter.Button(text="1:"+Q[Next][i],width=50,command=nest(Q[Next].index(Q[Next][i])))
    Button.pack()

root.mainloop()

