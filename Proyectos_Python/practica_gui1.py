#tkinter
import tkinter as tk
from tkinter import messagebox, ttk
def saludar():
    messagebox.showinfo(message="MI BOTON FUNCIONA", title="Mensajito")
root=tk.Tk()
#Generar frame o ventanita
frm=ttk.Frame(root, padding=10)
#Agregar texto o label
ttk.Label(frm,text="Holis").grid(column=0, row=0)
#Agregar caja donde el usuario pueda escribir
ttk.Entry(frm).grid(column=1,row=0)
#Agregar boton
ttk.Button(frm,text="Mensaje", command=saludar).grid(column=0, row=1)
frm.grid()
root.mainloop()
