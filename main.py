from tkinter import *
from time import strftime

# funçao para atualizar o relógio

def atualizar_relogio():
    horario_atual = strftime("%H:%M:%S %p")
    rotulo_relogio.config(text=horario_atual)
    rotulo_relogio.after(1000, atualizar_relogio)


# criar a janela principal

janela = Tk()
janela.title("Relogio Digital Simples")

# Criação do rótulo para exibir o relógio

rotulo_relogio = Label(
    janela,
    font=("Helvetica", 40, "bold"),
    background="purple",
    foreground="white"
)

# Posicione o rotulo no centro da janela

rotulo_relogio.pack(anchor="center")

# Inicia a atualização do relogio
atualizar_relogio()

# Inicia o loop principal da interface gráfica
janela.mainloop()


