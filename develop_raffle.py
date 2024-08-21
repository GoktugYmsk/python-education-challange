import tkinter as tk
from tkinter import messagebox
import random

def ekle_katilimci():
    isim = entry_katilimci.get()
    if isim:
        katilimcilar.append(isim)
        listbox_katilimcilar.insert(tk.END, isim)
        entry_katilimci.delete(0, tk.END)

def cekilis_yap():
    if len(katilimcilar) == 0:
        messagebox.showwarning("Uyarı", "Katılımcı yok, çekiliş yapılamaz!")
    else:
        kazanan = random.choice(katilimcilar)
        messagebox.showinfo("Kazanan", f"Tebrikler! Yılbaşı çekilişini kazanan: {kazanan}")

root = tk.Tk()
root.title("Yılbaşı Çekilişi")

katilimcilar = []

label_giris = tk.Label(root, text="Katılımcı İsmi:")
label_giris.pack()

entry_katilimci = tk.Entry(root)
entry_katilimci.pack()

button_ekle = tk.Button(root, text="Ekle", command=ekle_katilimci)
button_ekle.pack()

listbox_katilimcilar = tk.Listbox(root)
listbox_katilimcilar.pack()

button_cekilis = tk.Button(root, text="Çekilişi Yap", command=cekilis_yap)
button_cekilis.pack()

root.mainloop()
