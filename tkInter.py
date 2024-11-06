import tkinter as tk
import tkinter as tk
from datetime import datetime

def atualizar_hora():
    agora = datetime.now().strftime("%H:%M:%S")
    label_hora.config(text=agora)
    label_hora.after(1000, atualizar_hora)  # Atualiza a cada 1000ms (1 segundo)

# Criação da janela
janela = tk.Tk()
janela.title("Relógio Atual")

# Criação do label para mostrar a hora
label_hora = tk.Label(janela, font=("Helvetica", 48), fg="black")
label_hora.pack()

# Inicia a atualização da hora
atualizar_hora()

# Loop principal da janela
janela.mainloop()