import random

class Item:
    def __init__(self, nome, tipo, efeito):
        self.nome = nome
        self.tipo = tipo  # Por exemplo, 'força', 'resistência', 'vida'
        self.efeito = efeito  # Efeito do item, como +10 de força ou +5 de resistência

    def aplicar(self, personagem):
        if self.tipo == 'força':
            personagem.forca += self.efeito
        elif self.tipo == 'resistencia':
            personagem.resistencia += self.efeito
        elif self.tipo == 'vida':
            personagem.vida += self.efeito
        elif self.tipo == 'mana':
            personagem.mana += self.efeito
        print(f"{personagem.nome} usou {self.nome} e ganhou {self.efeito} de {self.tipo}.")

class Personagem:
    def __init__(self, nome, classe, forca=10, resistencia=10, inteligencia=10, agilidade=10, vida=100, mana=50):
        self.nome = nome
        self.classe = classe
        self.forca = forca
        self.resistencia = resistencia
        self.inteligencia = inteligencia
        self.agilidade = agilidade
        self.vida = vida
        self.mana = mana
        self.experiencia = 0
        self.nivel = 1
        self.itens = []
    
    def subir_nivel(self):
        self.nivel += 1
        self.experiencia = 0
        self.forca += 2
        self.resistencia += 2
        self.inteligencia += 2
        self.agilidade += 2
        self.vida += 20
        self.mana += 10
        print(f"{self.nome} subiu para o nível {self.nivel}!")

    def ganhar_item(self):
        itens_possiveis = [
            Item("Espada Mágica", "força", 5),
            Item("Escudo de Ferro", "resistencia", 5),
            Item("Poção de Vida", "vida", 30),
            Item("Poção de Mana", "mana", 20)
        ]
        item = random.choice(itens_possiveis)
        self.itens.append(item)
        print(f"{self.nome} encontrou o item {item.nome}!")
    
    def ganhar_experiencia(self, experiencia):
        self.experiencia += experiencia
        print(f"{self.nome} ganhou {experiencia} de experiência.")
        if self.experiencia >= 10 * self.nivel:
            self.subir_nivel()
    
    def receber_dano(self, dano):
        dano_final = max(dano - self.resistencia, 0)
        self.vida -= dano_final
        print(f"{self.nome} recebeu {dano_final} de dano. Vida atual: {self.vida}")
        if self.vida <= 0:
            self.morrer()

    def morrer(self):
        print(f"{self.nome} morreu. Fim de jogo.")
        exit(0)

    def atacar(self, inimigo):
        dano = self.forca + random.randint(0, 5)
        inimigo.receber_dano(dano)

    def mostrar_status(self):
        print(f"\nStatus de {self.nome}:")
        print(f"Classe: {self.classe} | Nível: {self.nivel} | Vida: {self.vida} | Mana: {self.mana}")
        print(f"Força: {self.forca} | Resistência: {self.resistencia} | Inteligência: {self.inteligencia} | Agilidade: {self.agilidade}")
        print(f"Experiência: {self.experiencia} / {10 * self.nivel} para próximo nível")
        print("Itens: ", [item.nome for item in self.itens])

    def usar_item(self, item_nome):
        item = next((item for item in self.itens if item.nome == item_nome), None)
        if item:
            item.aplicar(self)
            self.itens.remove(item)
        else:
            print(f"Item {item_nome} não encontrado no seu inventário.")

class Inimigo:
    def __init__(self, nome, forca, resistencia, vida):
        self.nome = nome
        self.forca = forca
        self.resistencia = resistencia
        self.vida = vida

    def atacar(self, personagem):
        dano = self.forca + random.randint(0, 5)
        personagem.receber_dano(dano)

    def receber_dano(self, dano):
        dano_final = max(dano - self.resistencia, 0)
        self.vida -= dano_final
        print(f"{self.nome} recebeu {dano_final} de dano. Vida atual: {self.vida}")
        if self.vida <= 0:
            print(f"{self.nome} foi derrotado!")

class Mago(Inimigo):
    def __init__(self, nome, forca, resistencia, vida, mana):
        super().__init__(nome, forca, resistencia, vida)
        self.mana = mana

    def atacar(self, personagem):
        if self.mana >= 10:
            dano = self.forca + random.randint(5, 10)
            personagem.receber_dano(dano)
            self.mana -= 10
            print(f"{self.nome} lançou uma magia causando {dano} de dano. Mana restante: {self.mana}")
        else:
            super().atacar(personagem)

# Função para iniciar uma batalha
def batalha(personagem, inimigo):
    while personagem.vida > 0 and inimigo.vida > 0:
        personagem.mostrar_status()
        print("\nO que você deseja fazer?")
        print("1. Atacar")
        print("2. Usar item")
        print("3. Ver status")
        escolha = input("Escolha a ação (1/2/3): ")

        if escolha == '1':
            personagem.atacar(inimigo)
            if inimigo.vida <= 0:
                print(f"{inimigo.nome} foi derrotado!")
                personagem.ganhar_experiencia(10)
                personagem.ganhar_item()
                break
        elif escolha == '2':
            item_nome = input("Qual item deseja usar? ")
            personagem.usar_item(item_nome)
        elif escolha == '3':
            personagem.mostrar_status()
        else:
            print("Opção inválida!")

        if inimigo.vida > 0:
            inimigo.atacar(personagem)
            if personagem.vida <= 0:
                print(f"{personagem.nome} foi derrotado!")
                break

# Criando personagem e inimigo para teste
jogador = Personagem("Aragorn", "Guerreiro")
inimigo = Inimigo("Goblin", 5, 2, 30)

# Começando o jogo
print("Bem-vindo ao jogo!")
batalha(jogador, inimigo)
