from tkinter import *
root = Tk()
root.geometry("800x290")
root.minsize(800,250)
root.title("Elite's Converter")
text = StringVar()
conver_c= StringVar()
conver_f= StringVar()
def con_to_c():
    conver_c.set("")
    conver_f.set("")
    temp_text=float(text.get())
    temp=(temp_text-32)*(5/9)
    conver_c.set(conver_c.get() + str(temp))

def con_to_f():
    conver_f.set("")
    conver_c.set("")
    temp_text=float(text.get())
    temp=((9/5)*(temp_text))+32
    conver_f.set(conver_f.get() + str(temp))


name=Label(text="Enter Temperature : ",font="calibre 20 bold")
name.grid(row=0,column=0)
text_lable=Entry(textvariable=text,font="calibre 20 normal")
text_lable.grid(row=0,column=1,pady=10,padx=10)

c_lable=Entry(textvariable=conver_c,font="calibre 20 normal")
c_lable.grid(row=1,column=1)
name=Label(text="Temperature in Celsius : ",font="calibre 20 bold")
name.grid(row=1,column=0,pady=10,padx=10)

f_lable=Entry(textvariable=conver_f,font="calibre 20 normal")
f_lable.grid(row=2,column=1)
name=Label(text="Temperature in Fahrenheit : ",font="calibre 20 bold")
name.grid(row=2,column=0,pady=10,padx=10)

conver_to_c=Button(text="Convert to Celsius",command=con_to_c)
conver_to_c.grid(row=3,column=0,pady=10)

conver_to_f=Button(text="Convert to Fahrenheit",command=con_to_f)
conver_to_f.grid(row=3,column=1,pady=10)

root.mainloop()
