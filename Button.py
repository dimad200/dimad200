from tkinter import *
from tkinter import ttk
root = Tk()
root1 = Tk()
frm1 = ttk.Frame(root1, padding=100)
frm = ttk.Frame(root, padding=100)
frm.grid()
ttk.Label(frm, text="Первый").grid(column=0, row=0)
ttk.Button(frm, text="первый закрыть", command=root.destroy).grid(column=0, row=1)
frm = ttk.Frame(root, padding=100)
frm1.grid()
ttk.Label(frm1, text="второй").grid(column=0, row=0)
ttk.Button(frm1, text="закрыть второй", command=root1.destroy).grid(column=0, row=1)
ttk.Entry().grid(column=0, row=2)
print(ttk.Entry)

root.mainloop()