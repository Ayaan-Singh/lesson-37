from tkinter import *
root = Tk()
root.title("Number Entry")
root.geometry("226x500")
nums = ([1,2,3],[4,5,6],[7,8,9],[0,"#","*"])
for i in range(4):
    root.columnconfigure(i, weight=1,minsize = 75)
    root.rowconfigure(i, weight=1,minsize = 50)
for i in range (4):
    for j in range(3):
        frame = Frame(
            master = root,
            relief = SUNKEN,
            borderwidth = 1,
            bg = "black"
        )
        frame.grid(row = i, column = j, sticky = "nsew")
        label = Label(master = frame, text = nums[i][j],bg = "white", font = ("Arial", 18), fg = "black")
        label.pack ( expand = True , fill = "both", padx =5, pady = 5)
root.mainloop()