import tkinter as tk

def mostrar_selecoes():
    for i, var in enumerate(vars):
        print(f"Texto: {texts[i]}, Selecionado: {var.get()}")

root = tk.Tk()
root.geometry('300x200')
root.title("Caixas de Seleção")

texts = ["Opção 1", "Opção 2", "Opção 3", "Opção 4"]  # Lista de textos
vars = []  # Lista para armazenar as variáveis das caixas de seleção

# Criar e empacotar caixas de seleção para cada texto na lista
for text in texts:
    var = tk.BooleanVar()  # Variável de controle para a caixa de seleção
    check_button = tk.Checkbutton(root, text=text, variable=var)
    check_button.pack(anchor=tk.W)  #Significa que ele será colocado o mais à esquerda possível dentro do espaço disponível.
    vars.append(var)  # Adicionar a variável à lista

# Botão para mostrar as seleções feitas
show_button = tk.Button(root, text="Mostrar seleções", command=mostrar_selecoes)
show_button.pack(pady=10)

root.mainloop()
