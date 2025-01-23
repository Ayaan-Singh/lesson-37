from tkinter import *
root = Tk()
root.title("login")
root.geometry("500x500")
frame = Frame(
    master = root,
    width= 300,
    height=200,
    relief = SUNKEN,
    borderwidth = 1,
    bg = "black"
    )
lbl1=Label(master = frame, text = "Username",bg = "grey", font = ("Arial", 18), fg = "white")
lbl2 = Label(master = frame, text = "Email",bg = "grey", font = ("Arial", 18), fg = "white")
lbl3 = Label(master = frame, text = "Password",bg = "grey", font = ("Arial", 18), fg = "white")
namee = Entry(frame)
email = Entry(frame)
password = Entry(frame, show = "*")
def display():
    name = namee.get()
    greet = f"hello {name} "
    message = "congratulations you have successfully logged in"
    textbox.insert(END, greet)
    textbox.insert(END, message)
textbox = Text(bg = "white" , fg = "black")
btn = Button( text = "create account", command = display, bg = "red")
frame.place(x= 20, y = 0)
lbl1.place(x = 20,y=20)
namee.place(x = 150, y = 20)
lbl2.place(x = 20, y = 80)
email.place(x = 150, y = 80)
lbl3.place(x = 20, y = 140)
password.place(x = 150, y = 140)
btn.place(x = 130, y = 210)
textbox.place( y = 250)
mainloop()




