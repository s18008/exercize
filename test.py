import tkinter,random
quiz = [('1+1=','1','2','3','4',2),('2+2=','4','6','8','10',1)]
q = random.sample(quiz,len(quiz))
Next = 0

root = tkinter.Tk()
root.title(u"Software Title")
root.geometry("400x300")

def nest1(number):
    def Decision():
        global Next
        if number == q[Next][5]:
            Static.config(text="正解")
        else:
            Static.config(text="不正解")
        Next += 1
        start.config(text="次の問題へ",width=50,command=nest2())
    return Decision

def nest2():
    def question():
        Static.config(text=q[Next][0])
        for i in range(1,5):
           Button = tkinter.Button(text="1:"+q[Next][i],width=50,command=nest1(q[Next].index(q[Next][i])))
           Button.pack()
    return question

Static = tkinter.Label(text='')
Static.pack()
start = tkinter.Button(text="問題を始める",width=50,command=nest2())
start.pack()
#for i in Choices:
#    i = tkinter.Button(text="")
#    i.pack()
root.mainloop()

