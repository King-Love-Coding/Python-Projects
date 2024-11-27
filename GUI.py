from tkinter import *
# the tkinter is a module by which we can perform a task on GUI in Python
root = Tk()  #Constructor - Constructs the page
root.title("My Web Form")
# root.resizable(False,1)
root.minsize(100,100)
root.maxsize(500,500)
# root.resizable(0,0) # Fix the Size of Page.
l1 = Label(root,text="MY NAME IS VIJAY SONI", bg="red", fg="white", font="Arial 20 bold",padx=20,pady=40,bd=5,relief=RAISED)
l1.pack(pady=20)

l2 = Label(root,text="MY NAME IS RAM", bg="red", fg="white", font="Arial 20 bold")
l2.pack()

root.mainloop()
print("My Name Is Vivek")
