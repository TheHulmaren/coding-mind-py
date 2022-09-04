#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 12 16:18:17 2022

@author: igyumin
"""

import tkinter

window=tkinter.Tk()

window.title("LEE KYU MIN")
window.geometry("640x400+100+100")
window.resizable(False, False)
window.configure(bg='blue')

label=tkinter.Label(window, text="안녕하세요.")
label.pack()

print(tkinter.TkVersion)

window.mainloop()