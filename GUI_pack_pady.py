import tkinter as tk

def aumentar_pady():
    pady_value = pady_slider.get()
    button1.pack_forget()  # Remover os botões anteriores
    button2.pack_forget()

    # Criar botões com o novo valor de pady
    button1.pack(pady=pady_value)
    button2.pack(pady=pady_value)

root = tk.Tk()
root.geometry('300x200')
root.title("Exemplo de pady")

# Slider para ajustar o valor de pady dinamicamente
pady_slider = tk.Scale(root, from_=0, to=50, orient=tk.HORIZONTAL, label="Valor de pady",
                        length=200, resolution=1)
pady_slider.pack(pady=0)

# Botões de exemplo
button1 = tk.Button(root, text="Botão 1")
button2 = tk.Button(root, text="Botão 2")
button1.pack(pady=10)  # Empacotar botões com um valor inicial de pady
button2.pack(pady=10)

# Botão para aplicar o valor de pady dinamicamente
apply_button = tk.Button(root, text="Aplicar pady", command=aumentar_pady)
apply_button.pack(pady=10)

root.mainloop()
