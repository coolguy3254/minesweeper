from tkinter import *


root = Tk()
# Override the settings of the window
root.configure(bg="black")
root.geometry('1200x600')
root.title("Minesweeper by Jonah :)")
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='blue', # Change later to turquoise
    width=1200,
    height=150
)
top_frame.place(x=0, y=0)



# run the window
root.mainloop()
