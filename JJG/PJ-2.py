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

    button_atacar.config(state=tk.DISABLED)
    button_curando.config(state=tk.DISABLED)
    
    button_atacar.config(command=ataque_jogador)
    button_curando.config(command=curar)

# Função para ir para a próxima sala
def proxima_sala():
    button_atacar.config(state=tk.NORMAL)
    button_curando.config(state=tk.NORMAL)
    button_proxima.config(state=tk.DISABLED)
    batalhar()

# Configuração da interface gráfica
root = tk.Tk()
root.title("Aventura no Labirinto")

# Criação dos objetos do jogador e mapa
nome_jogador = input("Qual o seu nome, aventureiro? ")
jogador = Jogador(nome_jogador)
salas = gerar_mapa()

# Labels
label_vida = tk.Label(root, text=f"Vida: {jogador.vida}", font=('Arial', 14))
label_vida.pack(pady=5)

label_experiencia = tk.Label(root, text=f"Experiência: {jogador.experiencia}", font=('Arial', 14))
label_experiencia.pack(pady=5)

label_nivel = tk.Label(root, text=f"Nível: {jogador.nivel}", font=('Arial', 14))
label_nivel.pack(pady=5)

label_sala = tk.Label(root, text=f"Sala atual: ", font=('Arial', 14))
label_sala.pack(pady=5)

label_inimigo = tk.Label(root, text="Inimigo: ", font=('Arial', 14))
label_inimigo.pack(pady=5)

label_batalha = tk.Label(root, text="Prepare-se para a batalha!", font=('Arial', 12), wraplength=300)
label_batalha.pack(pady=10)

# Botões
button_atacar = tk.Button(root, text="Atacar!", font=('Arial', 14))
button_atacar.pack(pady=5)

button_curando = tk.Button(root, text="Curar (20 Vida)", font=('Arial', 14))
button_curando.pack(pady=5)

button_proxima = tk.Button(root, text="Ir para próxima sala", font=('Arial', 14), state=tk.DISABLED, command=proxima_sala)
button_proxima.pack(pady=20)

# Inicia o jogo
batalhar()

root.mainloop()
