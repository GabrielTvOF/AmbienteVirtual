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
        print(f"{self.nome} ataca {inimigo.nome} causando {dano} de dano.")

    def ganhar_experiencia(self, pontos):
        self.experiencia += pontos
        if self.experiencia >= self.nivel * 20:  # Para subir de nível
            self.nivel += 1
            self.experiencia = 0
            print(f"{self.nome} subiu para o nível {self.nivel}!")

    def esta_vivo(self):
        return self.vida > 0

    def curar(self, pontos):
        self.vida += pontos
        print(f"{self.nome} se curou em {pontos} pontos. Vida atual: {self.vida}")

# Classe para representar os inimigos
class Inimigo:
    def __init__(self, nome):
        self.nome = nome
        self.vida = random.randint(30, 70)
        self.dano = random.randint(5, 10)

    def atacar(self, jogador):
        dano = random.randint(1, self.dano)
        jogador.vida -= dano
        print(f"{self.nome} ataca {jogador.nome} causando {dano} de dano.")

    def esta_vivo(self):
        return self.vida > 0

# Função para gerar o mapa
def gerar_mapa():
    salas = []
    for i in range(10):
        salas.append(f"Sala {i+1}")
    random.shuffle(salas)  # Embaralha as salas para que fiquem em posições aleatórias
    return salas

# Função para simular uma batalha entre o jogador e o inimigo
def batalha(jogador, inimigo):
    print(f"\nBatalha começando! {jogador.nome} vs {inimigo.nome}")
    while jogador.esta_vivo() and inimigo.esta_vivo():
        jogador.atacar(inimigo)
        if inimigo.esta_vivo():
            inimigo.atacar(jogador)
        if jogador.esta_vivo():
            jogador.ganhar_experiencia(10)  # O jogador ganha experiência por derrotar inimigos
        else:
            print(f"{jogador.nome} foi derrotado!")
            return False
    return True

# Função para explorar o mapa
def explorar_mapa(jogador, salas):
    for sala in salas:
        print(f"\nEntrando na {sala}...")
        # O inimigo será gerado aleatoriamente em cada sala
        inimigo = Inimigo(f"Inimigo {random.randint(1, 100)}")
        print(f"{inimigo.nome} apareceu! Vida: {inimigo.vida}, Dano: {inimigo.dano}")
        continuar = input("Deseja enfrentar o inimigo? (s/n): ").lower()
        if continuar == 's':
            if not batalha(jogador, inimigo):
                break
        else:
            print(f"{jogador.nome} decidiu não lutar.")
            jogador.curar(20)  # O jogador se cura um pouco se não lutar
        if not jogador.esta_vivo():
            break

# Função principal para rodar o jogo
def iniciar_jogo():
    nome = input("Qual o seu nome, aventureiro? ")
    jogador = Jogador(nome)
    print(f"Bem-vindo ao jogo, {jogador.nome}!")
    
    salas = gerar_mapa()
    explorar_mapa(jogador, salas)

    if jogador.esta_vivo():
        print(f"\nParabéns, {jogador.nome}! Você completou o jogo com {jogador.vida} de vida restante e chegou ao nível {jogador.nivel}.")
    else:
        print(f"\nGame Over, {jogador.nome}. Melhor sorte da próxima vez!")

# Rodando o jogo
if __name__ == "__main__":
    iniciar_jogo()
