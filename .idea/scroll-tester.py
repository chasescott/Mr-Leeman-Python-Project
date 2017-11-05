from tkinter import *
import tkinter.scrolledtext as ScrolledText

master = Tk()

st = ScrolledText.ScrolledText(master)
st.grid()

st.insert(INSERT, "Some text")
st.insert(END, " in ScrolledText")

print( st.get(1.0, END) )

master.mainloop()