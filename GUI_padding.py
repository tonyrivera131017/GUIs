import tkinter as tk

def update_padding(event=None):
    padx_value = int(horizontal_padding_slider.get())
    pady_value = int(vertical_padding_slider.get())
    button.config(padx=padx_value, pady=pady_value)

# Criar janela principal
root = tk.Tk()
root.title("Exemplo de Padding em Tkinter")

# Criar e posicionar o botão
button = tk.Button(root, text="Botão com Padding", padx=10, pady=10)
button.pack(pady=20)

# Criar controles deslizantes para ajustar o padding
horizontal_padding_slider = tk.Scale(root, from_=0, to=50, orient="horizontal", label="Padding Horizontal",
                                     command=update_padding)
horizontal_padding_slider.pack()

vertical_padding_slider = tk.Scale(root, from_=0, to=50, orient="horizontal", label="Padding Vertical",
                                   command=update_padding)
vertical_padding_slider.pack()

# Atualizar o padding quando os controles deslizantes são movidos
horizontal_padding_slider.bind("<Motion>", update_padding)
vertical_padding_slider.bind("<Motion>", update_padding)

# Iniciar o loop principal
root.mainloop()
