import os
import tkinter as tk
import pyjokes
import selamlas

print(os.listdir("/var/log"))
selamlas.SayHello("Duygu")

# Install module with apt 
window = tk.Tk()

joke = pyjokes.get_joke()
text = tk.Label(text=joke)
text.pack()

window.mainloop()

# sudo apt install python3-pip

# pip3 install paket_adi

# python3 --version

# virtualenv .venv
# source .venv/bin/activate
# deactivate

# alias python='/usr/bin/python3'