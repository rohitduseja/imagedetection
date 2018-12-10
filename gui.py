from tkinter import *

window=Tk()

def km_to_miles():
    print(e1_val.get())
    print(e2_val.get())
    ans=float(e1_val.get())+float(e2_val.get())
    t1.insert(END,ans)


l1=Label(window,text="Enter no1")
l1.grid(row=0,column=0)
e1_val=StringVar()
e1=Entry(window,textvariable=e1_val)
e1.grid(row=0,column=1)

l2=Label(window,text="Enter no1")
l2.grid(row=0,column=2)
e2_val=StringVar()
e2=Entry(window,textvariable=e2_val)
e2.grid(row=0,column=3)

l3=Label(window,text="Answer is")
l3.grid(row=1,column=0)
t1=Text(window,height=1,width=15)
t1.grid(row=1,column=1)

b1=Button(window,text="Add",command=km_to_miles)
b1.grid(row=1,column=2,columnspan=2)

window.mainloop()
