import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

image_path = r"C:\Users\Tony-Karhub\PycharmProjects\tensorflow\imgs_py\imgs_temporarias\tmpwrg_hcm3\D_653488-MLA72743732154_112023-O.jpg"  # Caminho da imagem
image = Image.open(image_path)
# image = image.resize((500, 500))  # Redimensiona a imagem conforme necessário
image.thumbnail((600,600))
root = tk.Tk()
root.title("Imagens")
frm = ttk.Frame(root, padding=10)
frm.pack()

photo = ImageTk.PhotoImage(image)
label = tk.Label(frm, image=photo)
label.pack(padx=10, pady=10)

root.mainloop()
