import tkinter as tk
from tkinter import messagebox
import random

# Classe para representar o jogador
class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100
        self.experiencia = 0
        self.nivel = 1

    def atacar(self, inimigo):
        dano = random.randint(5, 15)
        inimigo.vida -= dano
        return dano

    def ganhar_experiencia(self, pontos):
        self.experiencia += pontos
        if self.experiencia >= self.nivel * 20:  # Para subir de nível
            self.nivel += 1
            self.experiencia = 0
            return True
        return False

    def esta_vivo(self):
        return self.vida > 0

    def curar(self, pontos):
        self.vida += pontos
        if self.vida > 100:
            self.vida = 100

# Classe para representar os inimigos
class Inimigo:
    def __init__(self, nome):
        self.nome = nome
        self.vida = random.randint(30, 70)
        self.dano = random.randint(5, 10)

    def atacar(self, jogador):
        dano = random.randint(1, self.dano)
        jogador.vida -= dano
        return dano

    def esta_vivo(self):
        return self.vida > 0

# Função para gerar o mapa
def gerar_mapa():
    salas = []
    for i in range(10):
        salas.append(f"Sala {i+1}")
    random.shuffle(salas)  # Embaralha as salas para que fiquem em posições aleatórias
    return salas

# Função para atualizar a interface com os status do jogador
def atualizar_interface():
    label_vida.config(text=f"Vida: {jogador.vida}")
    label_experiencia.config(text=f"Experiência: {jogador.experiencia}")
    label_nivel.config(text=f"Nível: {jogador.nivel}")
    label_sala.config(text=f"Sala atual: {salas[0]}")

    if not jogador.esta_vivo():
        messagebox.showinfo("Game Over", f"{jogador.nome} foi derrotado! Game Over!")
        root.quit()

# Função para iniciar a batalha
def batalhar():
    if not salas:
        messagebox.showinfo("Fim de Jogo", f"{jogador.nome} completou o jogo com nível {jogador.nivel}!")
        root.quit()
        return
    
    sala = salas.pop(0)
    inimigo = Inimigo(f"Inimigo {random.randint(1, 100)}")

    # Atualiza a sala atual
    label_sala.config(text=f"Sala atual: {sala}")
    label_inimigo.config(text=f"Inimigo: {inimigo.nome} | Vida: {inimigo.vida}")

    # Habilitar o botão de atacar e curar
    button_atacar.config(state=tk.NORMAL)
    button_curando.config(state=tk.NORMAL)
    button_proxima.config(state=tk.DISABLED)

    def ataque_jogador():
        dano = jogador.atacar(inimigo)
        label_batalha.config(text=f"{jogador.nome} ataca {inimigo.nome} e causa {dano} de dano.")
        
        if inimigo.esta_vivo():
            dano_inimigo = inimigo.atacar(jogador)
            label_batalha.config(text=f"{label_batalha.cget('text')}\n{inimigo.nome} ataca {jogador.nome} e causa {dano_inimigo} de dano.")
            if not jogador.esta_vivo():
                atualizar_interface()
                return

        jogador.ganhar_experiencia(10)
        if jogador.ganhar_experiencia(10):
            messagebox.showinfo("Novo Nível!", f"{jogador.nome} subiu para o nível {jogador.nivel}!")
        
        atualizar_interface()

        if not inimigo.esta_vivo():
            label_batalha.config(text=f"{inimigo.nome} foi derrotado!")
            if salas:
                button_proxima.config(state=tk.NORMAL)

    def curar():
        jogador.curar(20)
        label_batalha.config(text=f"{jogador.nome} se curou em 20 pontos.")
        atualizar_interface()
        if salas:
            button_proxima.config(state=tk.NORMAL)

    # Desabilitar o botão de ataque até a próxima
    button_atacar.config(command=ataque_jogador)
    button_curando.config(command=curar)

# Função para ir para a próxima sala
def proxima_sala():
    if not salas:
        messagebox.showinfo("Fim de Jogo", f"{jogador.nome} completou o jogo com nível {jogador.nivel}!")
        root.quit()
        return
    button_atacar.config(state=tk.DISABLED)
    button_curando.config(state=tk.DISABLED)
    button_proxima.config(state=tk.DISABLED)
    batalhar()

# Função para iniciar o jogo
def iniciar_jogo():
    nome = entry_nome.get()
    if nome == "":
        messagebox.showwarning("Nome", "Por favor, insira um nome antes de começar.")
        return
    
    global jogador
    jogador = Jogador(nome)
    global salas
    salas = gerar_mapa()

    # Esconde o campo de nome e botão de iniciar
    frame_inicio.pack_forget()

    # Mostra a interface de jogo
    frame_jogo.pack(pady=10)
    batalhar()

# Configuração da interface
root = tk.Tk()
root.title("Aventura no Labirinto")

# Interface de início (onde o jogador coloca seu nome)
frame_inicio = tk.Frame(root)
label_nome = tk.Label(frame_inicio, text="Digite seu nome para começar:", font=('Arial', 14))
label_nome.pack(pady=5)

entry_nome = tk.Entry(frame_inicio, font=('Arial', 14))
entry_nome.pack(pady=5)

button_iniciar = tk.Button(frame_inicio, text="Iniciar Jogo", font=('Arial', 14), command=iniciar_jogo)
button_iniciar.pack(pady=10)

frame_inicio.pack(pady=50)

# Interface de jogo
frame_jogo = tk.Frame(root)

# Labels
label_vida = tk.Label(frame_jogo, text="Vida: 100", font=('Arial', 14))
label_vida.pack(pady=5)

label_experiencia = tk.Label(frame_jogo, text="Experiência: 0", font=('Arial', 14))
label_experiencia.pack(pady=5)

label_nivel = tk.Label(frame_jogo, text="Nível: 1", font=('Arial', 14))
label_nivel.pack(pady=5)

label_sala = tk.Label(frame_jogo, text="Sala atual: ", font=('Arial', 14))
label_sala.pack(pady=5)

label_inimigo = tk.Label(frame_jogo, text="Inimigo: ", font=('Arial', 14))
label_inimigo.pack(pady=5)

label_batalha = tk.Label(frame_jogo, text="Prepare-se para a batalha!", font=('Arial', 12), wraplength=300)
label_batalha.pack(pady=10)

# Botões
button_atacar = tk.Button(frame_jogo, text="Atacar!", font=('Arial', 14), state=tk.DISABLED)
button_atacar.pack(pady=5)

button_curando = tk.Button(frame_jogo, text="Curar (20 Vida)", font=('Arial', 14), state=tk.DISABLED)
button_curando.pack(pady=5)

button_proxima = tk.Button(frame_jogo, text="Ir para próxima sala", font=('Arial', 14), state=tk.DISABLED, command=proxima_sala)
button_proxima.pack(pady=20)

# Iniciar o Tkinter loop
root.mainloop()
