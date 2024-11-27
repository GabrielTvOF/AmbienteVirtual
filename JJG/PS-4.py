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
    def __init__(self, nome, classe, vida, forca, inteligencia, agilidade, resistencia, habilidade_especial):
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
        self.habilidade_especial = habilidade_especial  # Habilidade especial da classe
        self.pontos_para_distribuir = 0  # Pontos disponíveis para distribuir ao subir de nível

    def __str__(self):
        return (f"{self.nome} - Nível {self.nivel} ({self.classe})\n"
                f"Vida: {self.vida} | Força: {self.forca} | Inteligência: {self.inteligencia} | "
                f"Agilidade: {self.agilidade} | Resistência: {self.resistencia}\n"
                f"Experiência: {self.experiencia} | Pontos para distribuir: {self.pontos_para_distribuir}\n"
                f"Habilidade Especial: {self.habilidade_especial}\n"
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

    def usar_habilidade(self, inimigo):
        """Usa a habilidade especial do personagem"""
        if self.classe == 'Guerreiro':
            dano = random.randint(10, 20) + self.forca
            inimigo.vida -= dano
            return f"{self.nome} usou sua habilidade especial 'Corte Imponente' e causou {dano} de dano!"
        elif self.classe == 'Mago':
            cura = random.randint(10, 15) + self.inteligencia
            self.vida += cura
            return f"{self.nome} usou sua habilidade especial 'Cura Mágica' e recuperou {cura} de vida!"
        elif self.classe == 'Arqueiro':
            dano = random.randint(5, 10) + self.agilidade
            inimigo.vida -= dano
            return f"{self.nome} usou sua habilidade especial 'Flecha Rápida' e causou {dano} de dano!"

    def ganhar_experiencia(self, xp):
        """Ganha experiência e sobe de nível quando atinge o limite de XP"""
        self.experiencia += xp
        while self.experiencia >= self.nivel * 100:  # Cada nível precisa de 100*nível de XP
            self.experiencia -= self.nivel * 100
            self.subir_nivel()

    def subir_nivel(self):
        """Sobe o nível do personagem, aumentando os atributos e distribuindo pontos"""
        self.nivel += 1
        self.pontos_para_distribuir += 5  # Pontos para distribuir a cada novo nível
        self.vida += 10  # Aumento de vida a cada nível
        print(f"{self.nome} subiu para o nível {self.nivel}!")

    def distribuir_pontos(self, forca=0, inteligencia=0, agilidade=0, resistencia=0):
        """Distribui os pontos de atributos entre os parâmetros fornecidos"""
        if forca + inteligencia + agilidade + resistencia > self.pontos_para_distribuir:
            print("Você não tem pontos suficientes para distribuir.")
            return

        self.forca += forca
        self.inteligencia += inteligencia
        self.agilidade += agilidade
        self.resistencia += resistencia
        self.pontos_para_distribuir -= (forca + inteligencia + agilidade + resistencia)

        print(f"Pontos distribuídos! Força: {forca}, Inteligência: {inteligencia}, Agilidade: {agilidade}, Resistência: {resistencia}")
        print(f"Pontos restantes: {self.pontos_para_distribuir}")

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
                texto_combate.insert(tk.END, f"{personagem.nome} esquivou do ataque!\n")
            else:
                texto_combate.insert(tk.END, f"{personagem.nome} não conseguiu esquivar!\n")
        elif escolha_acao.get() == "Habilidade Especial":
            texto_combate.insert(tk.END, f"{personagem.usar_habilidade(inimigo)}\n")

        if inimigo.vida > 0:
            # Ataque do inimigo
            if inimigo.esquivar():
                texto_combate.insert(tk.END, f"{inimigo.nome} esquivou do ataque!\n")
            else:
                dano_inimigo = inimigo.atacar()
                dano_recebido = personagem.receber_dano(dano_inimigo)
                texto_combate.insert(tk.END, f"{inimigo.nome} atacou e causou {dano_recebido} de dano.\n")
        else:
            texto_combate.insert(tk.END, f"{inimigo.nome} foi derrotado!\n")
            personagem.ganhar_experiencia(50)  # Ganho de XP por derrotar o inimigo
            break

        root.update()

# Função para começar o combate
def iniciar_combate():
    nome_personagem = entry_nome.get()
    classe_personagem = classe_var.get()

    # Definir os atributos iniciais baseados na classe
    if classe_personagem == "Guerreiro":
        personagem = Personagem(nome_personagem, classe_personagem, 100, 15, 5, 5, 10, "Corte Imponente")
    elif classe_personagem == "Mago":
        personagem = Personagem(nome_personagem, classe_personagem, 80, 5, 15, 5, 8, "Cura Mágica")
    elif classe_personagem == "Arqueiro":
        personagem = Personagem(nome_personagem, classe_personagem, 90, 10, 10, 12, 7, "Flecha Rápida")

    # Criar inimigo
    inimigo = Inimigo("Goblin", 50, 8, 5, 10)

    # Exibir informações iniciais
    texto_combate.insert(tk.END, f"{personagem.nome} de classe {personagem.classe} entrou em combate com {inimigo.nome}!\n")
    combate(personagem, inimigo)

# Função para distribuir pontos
def distribuir_pontos():
    try:
        forca = int(entry_forca.get())
        inteligencia = int(entry_inteligencia.get())
        agilidade = int(entry_agilidade.get())
        resistencia = int(entry_resistencia.get())
        personagem.distribuir_pontos(forca, inteligencia, agilidade, resistencia)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos para distribuir os pontos.")

# Criar a interface com tkinter
root = tk.Tk()
root.title("Jogo de Combate")

# Nome do personagem
tk.Label(root, text="Nome do Personagem:").pack()
entry_nome = tk.Entry(root)
entry_nome.pack()

# Classe do personagem
tk.Label(root, text="Escolha sua classe:").pack()
classe_var = tk.StringVar()
classe_var.set("Guerreiro")
tk.Radiobutton(root, text="Guerreiro", variable=classe_var, value="Guerreiro").pack()
tk.Radiobutton(root, text="Mago", variable=classe_var, value="Mago").pack()
tk.Radiobutton(root, text="Arqueiro", variable=classe_var, value="Arqueiro").pack()

# Botão para iniciar combate
button_iniciar_combate = tk.Button(root, text="Iniciar Combate", command=iniciar_combate)
button_iniciar_combate.pack()

# Texto para mostrar o combate
texto_combate = tk.Text(root, height=10, width=50)
texto_combate.pack()

# Status do personagem e do inimigo
label_status_personagem = tk.Label(root, text="Status do Personagem")
label_status_personagem.pack()

label_status_inimigo = tk.Label(root, text="Status do Inimigo")
label_status_inimigo.pack()

# Ações do jogador
escolha_acao = tk.StringVar()
escolha_acao.set("Atacar")
button_atacar = tk.Button(root, text="Atacar", command=lambda: escolha_acao.set("Atacar"))
button_atacar.pack()

button_defender = tk.Button(root, text="Defender", command=lambda: escolha_acao.set("Defender"))
button_defender.pack()

button_esquivar = tk.Button(root, text="Esquivar", command=lambda: escolha_acao.set("Esquivar"))
button_esquivar.pack()

button_habilidade_especial = tk.Button(root, text="Habilidade Especial", command=lambda: escolha_acao.set("Habilidade Especial"))
button_habilidade_especial.pack()

button_executar_acao = tk.Button(root, text="Executar Ação", command=distribuir_pontos)
button_executar_acao.pack()

root.mainloop()
