import tkinter as tk
from tkinter import messagebox
import random

# Classe Item
class Item:
    def __init__(self, nome, tipo, valor):
        self.nome = nome
        self.tipo = tipo  # Tipo de atributo: 'forca', 'inteligencia', 'agilidade', 'resistencia', 'vida'
        self.valor = valor
    
    def aplicar(self, personagem):
        """Aplica o efeito do item no personagem"""
        if self.tipo == 'forca':
            personagem.forca += self.valor
        elif self.tipo == 'inteligencia':
            personagem.inteligencia += self.valor
        elif self.tipo == 'agilidade':
            personagem.agilidade += self.valor
        elif self.tipo == 'resistencia':
            personagem.resistencia += self.valor
        elif self.tipo == 'vida':
            personagem.vida += self.valor
        print(f"{personagem.nome} usou o item {self.nome}! {self.tipo.capitalize()} aumentada em {self.valor} pontos.")

# Classe Personagem
class Personagem:
    def __init__(self, nome, classe, vida, forca, inteligencia, agilidade, resistencia):
        self.nome = nome
        self.classe = classe
        self.vida = vida
        self.forca = forca
        self.inteligencia = inteligencia
        self.agilidade = agilidade
        self.resistencia = resistencia
        self.experiencia = 0
        self.nivel = 1
        self.itens = []  # Lista de itens que o personagem possui

    def __str__(self):
        return (f"{self.nome} - Nível {self.nivel} ({self.classe})\n"
                f"Vida: {self.vida} | Força: {self.forca} | Inteligência: {self.inteligencia} | "
                f"Agilidade: {self.agilidade} | Resistência: {self.resistencia}\n"
                f"Experiência: {self.experiencia}\n"
                f"Itens: {', '.join([item.nome for item in self.itens]) if self.itens else 'Nenhum item'}")

    def atacar(self):
        """Calcula o dano do ataque baseado na força"""
        dano = random.randint(1, 10) + self.forca
        return dano

    def defender(self):
        """Calcula a defesa do personagem baseado em inteligência e resistência"""
        defesa = random.randint(1, 5) + self.inteligencia + self.resistencia
        return defesa

    def esquivar(self):
        """Calcula a chance de esquiva baseado na agilidade"""
        chance_esquiva = random.randint(1, 100)
        if chance_esquiva <= self.agilidade:
            return True
        return False

    def receber_dano(self, dano):
        """Subtrai a vida do personagem após receber dano, levando em consideração a resistência"""
        dano_recebido = max(dano - self.resistencia, 0)  # Dano mínimo é 0
        self.vida -= dano_recebido
        if self.vida <= 0:
            self.vida = 0
            self.morte()
        return dano_recebido

    def morte(self):
        """Exibe uma mensagem de morte grandiosa quando a vida chega a 0"""
        print(f"{self.nome} foi derrotado!")

# Classe Inimigo
class Inimigo:
    def __init__(self, nome, vida, forca, resistencia, agilidade):
        self.nome = nome
        self.vida = vida
        self.forca = forca
        self.resistencia = resistencia
        self.agilidade = agilidade

    def __str__(self):
        return f"Inimigo: {self.nome} | Vida: {self.vida} | Força: {self.forca} | Resistência: {self.resistencia} | Agilidade: {self.agilidade}"

    def atacar(self):
        """Calcula o dano do ataque baseado na força"""
        return random.randint(5, 15) + self.forca

    def defender(self):
        """Calcula a defesa do inimigo baseado na resistência"""
        return random.randint(1, 5) + self.resistencia

    def esquivar(self):
        """Calcula a chance de esquiva do inimigo"""
        chance_esquiva = random.randint(1, 100)
        return chance_esquiva <= self.agilidade

# Função de combate
def combate(personagem, inimigo):
    while personagem.vida > 0 and inimigo.vida > 0:
        # Atualizar as labels de status
        label_status_personagem.config(text=f"{personagem.nome}: {personagem.vida} HP")
        label_status_inimigo.config(text=f"{inimigo.nome}: {inimigo.vida} HP")

        # Ação do jogador
        if escolha_acao.get() == "Atacar":
            dano_player = personagem.atacar()
            inimigo.vida -= dano_player
            texto_combate.insert(tk.END, f"{personagem.nome} atacou e causou {dano_player} de dano.\n")
        elif escolha_acao.get() == "Defender":
            defesa_player = personagem.defender()
            texto_combate.insert(tk.END, f"{personagem.nome} se defendeu e absorveu {defesa_player} de dano.\n")
        elif escolha_acao.get() == "Esquivar":
            if personagem.esquivar():
                texto_combate.insert(tk.END, f"{personagem.nome} esquivou com sucesso!\n")
            else:
                dano_inimigo = inimigo.atacar()
                personagem.receber_dano(dano_inimigo)
                texto_combate.insert(tk.END, f"{personagem.nome} falhou ao esquivar e tomou {dano_inimigo} de dano.\n")

        # Ação do inimigo
        if inimigo.vida > 0:
            if inimigo.esquivar():
                texto_combate.insert(tk.END, f"{inimigo.nome} esquivou do ataque!\n")
            else:
                dano_inimigo = inimigo.atacar()
                personagem.receber_dano(dano_inimigo)
                texto_combate.insert(tk.END, f"{inimigo.nome} atacou e causou {dano_inimigo} de dano.\n")
        
        # Atualizar a interface após cada rodada
        label_status_personagem.config(text=f"{personagem.nome}: {personagem.vida} HP")
        label_status_inimigo.config(text=f"{inimigo.nome}: {inimigo.vida} HP")

        # Verifica o fim do combate
        if personagem.vida <= 0:
            texto_combate.insert(tk.END, f"{personagem.nome} foi derrotado!\n")
            break
        elif inimigo.vida <= 0:
            texto_combate.insert(tk.END, f"{inimigo.nome} foi derrotado!\n")
            break

# Função para selecionar a ação do jogador
def selecionar_acao():
    combate(personagem, inimigo)

# Função para iniciar o combate
def iniciar_combate():
    global personagem, inimigo
    nome_personagem = entry_nome.get()
    personagem = Personagem(nome_personagem, "Guerreiro", 100, 10, 5, 5, 10)
    inimigo = Inimigo("Goblin", 30, 5, 3, 4)

    label_status_personagem.config(text=f"{personagem.nome}: {personagem.vida} HP")
    label_status_inimigo.config(text=f"{inimigo.nome}: {inimigo.vida} HP")
    texto_combate.insert(tk.END, f"Você está enfrentando {inimigo.nome}!\n")

# Criando a interface gráfica
root = tk.Tk()
root.title("Jogo de Combate")

# Informações do personagem
label_nome = tk.Label(root, text="Nome do Personagem:")
label_nome.pack()

entry_nome = tk.Entry(root)
entry_nome.pack()

button_iniciar = tk.Button(root, text="Iniciar Combate", command=iniciar_combate)
button_iniciar.pack()

# Status de combate
label_status_personagem = tk.Label(root, text="")
label_status_personagem.pack()

label_status_inimigo = tk.Label(root, text="")
label_status_inimigo.pack()

# Área de texto para o combate
texto_combate = tk.Text(root, height=10, width=50)
texto_combate.pack()

# Botões de ação
escolha_acao = tk.StringVar(value="Atacar")
button_atacar = tk.Button(root, text="Atacar", command=lambda: escolha_acao.set("Atacar"))
button_atacar.pack()

button_defender = tk.Button(root, text="Defender", command=lambda: escolha_acao.set("Defender"))
button_defender.pack()

button_esquivar = tk.Button(root, text="Esquivar", command=lambda: escolha_acao.set("Esquivar"))
button_esquivar.pack()

button_executar_acao = tk.Button(root, text="Executar Ação", command=selecionar_acao)
button_executar_acao.pack()

root.mainloop()
