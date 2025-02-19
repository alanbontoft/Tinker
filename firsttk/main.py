import tkinter
import customtkinter as ctk
from pyModbusTCP.client import ModbusClient

from commands import *

def readRegs(n):
    if switch._check_state:
        n = 5
    regs = client.read_holding_registers(0, n)
    print(regs)

def writeRegs(n):
    res = client.write_multiple_registers(0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(res)



ctk.set_default_color_theme("blue")
ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.geometry("720x480")
app.title("First CTk App")
# app.grid_columnconfigure(0, weight=1)
app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=1)

app.rowconfigure(0, weight=1)
app.rowconfigure(1, weight=1)
app.rowconfigure(2, weight=1)
app.rowconfigure(3, weight=1)
app.rowconfigure(4, weight=1)


title = ctk.CTkLabel(app, text="Test", height=30, font=("Roboto", 30))
title.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
# title.configure(font=)

button = ctk.CTkButton(app, text="Read checks", command=lambda: showChecks(checkbox_1._check_state, checkbox_2._check_state))
button.grid(row=1, column=0, padx=10, pady=20, sticky='ew', columnspan=2)

checkbox_1 = ctk.CTkCheckBox(app, text="checkbox 1")
checkbox_1.grid(row=2, column=0, padx=20, pady=(0, 20)) #, sticky="e")

checkbox_2 = ctk.CTkCheckBox(app, text="checkbox 2")
checkbox_2.grid(row=2, column=1, padx=20, pady=(0, 20)) #, sticky="e")

btnRead = ctk.CTkButton(app, text="Read Regs", command= lambda: readRegs(10))
btnRead.grid(row=3, column=0, padx=10, pady=(10,0), sticky='nsew')

btnWrite = ctk.CTkButton(app, text="Write Regs", command= lambda: writeRegs(2))
btnWrite.grid(row=3, column=1, padx=(0,10), pady=(10,0), sticky='nsew')

switch = ctk.CTkSwitch(app, text="Read half")
switch.grid(row=4, column=0)

# TCP auto connect on first modbus request
client = ModbusClient(host="172.31.7.125", port=502, unit_id=1, auto_open=True)

app.mainloop()