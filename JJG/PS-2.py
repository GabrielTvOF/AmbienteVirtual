import random

class Item:
    def __init__(self, nome, tipo, valor):
        self.nome = nome
        self.tipo = tipo  # Tipo de atributo: 'forca', 'inteligencia', 'agilidade', 'resistencia', 'vida', 'armadura'
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
        elif self.tipo == 'armadura':
            personagem.armadura += self.valor
        print(f"{personagem.nome} usou o item {self.nome}! {self.tipo.capitalize()} aumentada em {self.valor} pontos.")

class Personagem:
    def __init__(self, nome, classe, vida, forca, inteligencia, agilidade, resistencia):
        self.nome = nome
        self.classe = classe
        self.vida = vida
        self.forca = forca
        self.inteligencia = inteligencia
        self.agilidade = agilidade
        self.resistencia = resistencia
        self.armadura = 0  # Nova característica: armadura
        self.experiencia = 0
        self.nivel = 1
        self.itens = []  # Lista de itens que o personagem possui
        self.habilidades = {
            'Ataque Poderoso': self.ataque_poderoso,
            'Escudo Mágico': self.escudo_magico
        }

    def __str__(self):
        return (f"{self.nome} - Nível {self.nivel} ({self.classe})\n"
                f"Vida: {self.vida} | Força: {self.forca} | Inteligência: {self.inteligencia} | "
                f"Agilidade: {self.agilidade} | Resistência: {self.resistencia} | Armadura: {self.armadura}\n"
                f"Experiência: {self.experiencia}\n"
                f"Itens: {', '.join([item.nome for item in self.itens]) if self.itens else 'Nenhum item'}")

    def ganhar_experiencia(self, pontos):
        """Adicionar experiência ao personagem e evoluir de nível"""
        self.experiencia += pontos
        while self.experiencia >= self.nivel * 100:
            self.experiencia -= self.nivel * 100
            self.subir_nivel()

    def ganhar_item(self):
        """Ganha um item que melhora algum atributo"""
        itens_possiveis = [
            Item("Poção de Força", "forca", 2),
            Item("Poção de Inteligência", "inteligencia", 2),
            Item("Poção de Agilidade", "agilidade", 2),
            Item("Poção de Resistência", "resistencia", 2),
            Item("Elixir de Vida", "vida", 10),
            Item("Armadura de Ferro", "armadura", 5)
        ]
        
        item_ganho = random.choice(itens_possiveis)  # Escolhe um item aleatório da lista
        self.itens.append(item_ganho)  # Adiciona o item à lista de itens do personagem
        item_ganho.aplicar(self)  # Aplica o efeito do item no personagem

    def subir_nivel(self):
        """Aumenta o nível do personagem"""
        self.nivel += 1
        self.vida += 10
        self.forca += 2
        self.inteligencia += 1
        self.agilidade += 1
        self.resistencia += 2
        print(f"{self.nome} subiu para o nível {self.nivel}!")

    def atacar(self):
        """Calcula o dano do ataque baseado na força"""
        dano = random.randint(1, 10) + self.forca
        return dano

    def defender(self):
        """Calcula a defesa do personagem baseado em inteligência e resistência"""
        defesa = random.randint(1, 5) + self.inteligencia + self.resistencia + self.armadura
        return defesa

    def esquivar(self):
        """Calcula a chance de esquiva baseado na agilidade"""
        chance_esquiva = random.randint(1, 100)
        if chance_esquiva <= self.agilidade:
            return True
        return False

    def ataque_poderoso(self):
        """Realiza um ataque especial que causa mais dano"""
        dano = random.randint(10, 20) + self.forca * 2
        print(f"{self.nome} usou Ataque Poderoso! Causou {dano} de dano!")
        return dano

    def escudo_magico(self):
        """Realiza uma defesa especial que reduz o dano recebido"""
        defesa = random.randint(5, 10) + self.inteligencia
        print(f"{self.nome} usou Escudo Mágico! Reduziu o dano recebido em {defesa} pontos!")
        return defesa

    def receber_dano(self, dano):
        """Subtrai a vida do personagem após receber dano, levando em consideração a resistência"""
        dano_recebido = max(dano - self.resistencia - self.armadura, 0)  # Dano mínimo é 0
        self.vida -= dano_recebido
        if self.vida <= 0:
            self.vida = 0
            self.morte()
        return dano_recebido

    def morte(self):
        """Exibe uma mensagem de morte grandiosa quando a vida chega a 0"""
        print("\n" + "="*50)
        print(f"{'A ENTIDADE MORTE TE LEVOU!':^50}")
        print("="*50)
        print(f"{self.nome} foi derrotado!")
        print("="*50)

class Chefao:
    def __init__(self, nivel):
        """O chefão tem nível maior que o do jogador"""
        self.nivel = nivel
        self.nome = "Chefão"
        self.vida = 150 + nivel * 10
        self.forca = 20 + nivel * 3
        self.inteligencia = 10 + nivel * 2
        self.agilidade = 8 + nivel
        self.resistencia = 15 + nivel * 2

    def __str__(self):
        return (f"{self.nome} - Nível {self.nivel}\n"
                f"Vida: {self.vida} | Força: {self.forca} | Inteligência: {self.inteligencia} | "
                f"Agilidade: {self.agilidade} | Resistência: {self.resistencia}\n")

    def atacar(self):
        """Calcula o dano do chefão baseado na força"""
        dano = random.randint(1, 15) + self.forca
        return dano

    def defender(self):
        """Calcula a defesa do chefão baseado em inteligência e resistência"""
        defesa = random.randint(1, 5) + self.inteligencia + self.resistencia
        return defesa

    def esquivar(self):
        """Calcula a chance de esquiva do chefão baseado na agilidade"""
        chance_esquiva = random.randint(1, 100)
        if chance_esquiva <= self.agilidade:
            return True
        return False

    def receber_dano(self, dano):
        """Subtrai a vida do chefão após receber dano, levando em consideração a resistência"""
        dano_recebido = max(dano - self.resistencia, 0)  # Dano mínimo é 0
        self.vida -= dano_recebido
        if self.vida <= 0:
            self.vida = 0
            self.morte()
        return dano_recebido

    def morte(self):
        """Exibe uma mensagem de morte grandiosa quando a vida chega a 0"""
        print("\n" + "="*50)
        print(f"{'O CHEFÃO FOI DERROTADO!':^50}")
        print("="*50)

# Função para gerar o relatório da batalha
def gerar_relatorio(personagem, chefao, acao_personagem, acao_chefao, dano_personagem, dano_chefao):
    print("\n--- Relatório da Batalha ---")
    print(f"{personagem.nome} está enfrentando {chefao.nome}!")
    print(f"\nAção do {personagem.nome}: {acao_personagem}")
    print(f"Resultado do ataque de {personagem.nome}: {dano_personagem} de dano")
    print(f"Vida restante do {chefao.nome}: {chefao.vida}\n")
    
    print(f"Ação do {chefao.nome}: {acao_chefao}")
    print(f"Resultado do ataque de {chefao.nome}: {dano_chefao} de dano")
    print(f"Vida restante de {personagem.nome}: {personagem.vida}")
    print("\n--- Fim do Relatório ---\n")

# Função para criar um personagem
def criar_personagem():
    nome = input("Digite o nome do personagem: ")
    classe = input("Escolha a classe do personagem (Guerreiro, Mago, Arqueiro): ")
    vida_inicial = 100
    forca_inicial = 10
    inteligencia_inicial = 5
    agilidade_inicial = 5
    resistencia_inicial = 10

    if classe.lower() == "guerreiro":
        forca_inicial += 5
        resistencia_inicial += 5
    elif classe.lower() == "mago":
        inteligencia_inicial += 5
        agilidade_inicial += 3
    elif classe.lower() == "arqueiro":
        agilidade_inicial += 5
        inteligencia_inicial += 3
    else:
        print("Classe inválida! Usando classe 'Guerreiro' por padrão.")
        classe = "Guerreiro"

    return Personagem(nome, classe, vida_inicial, forca_inicial, inteligencia_inicial, agilidade_inicial, resistencia_inicial)

# Função para realizar uma batalha entre o jogador e o chefão
def batalha_com_chefao(personagem, chefao):
    print(f"\nVocê enfrentará o {chefao.nome} de nível {chefao.nivel}!\n")
    
    while personagem.vida > 0 and chefao.vida > 0:
        print(f"\n{personagem}\n")
        print(f"{chefao}\n")
        
        # Escolha do jogador
        print("Escolha uma ação:")
        print("1. Atacar")
        print("2. Defender")
        print("3. Esquivar")
        
        escolha = input("Escolha uma opção (1/2/3): ")
        
        acao_personagem = ""
        dano_personagem = 0
        acao_chefao = ""
        dano_chefao = 0
        
        if escolha == "1":
            acao_personagem = f"{personagem.nome} atacou"
            dano_personagem = personagem.atacar()
            chefao.receber_dano(dano_personagem)
        elif escolha == "2":
            acao_personagem = f"{personagem.nome} se defendeu"
            defesa_personagem = personagem.defender()
            chefao.receber_dano(defesa_personagem)
        elif escolha == "3":
            if personagem.esquivar():
                acao_personagem = f"{personagem.nome} esquivou com sucesso!"
                print(f"{personagem.nome} não tomou dano porque esquivou com sucesso!")
            else:
                acao_personagem = f"{personagem.nome} tentou esquivar, mas falhou!"
                dano_chefao = chefao.atacar()
                personagem.receber_dano(dano_chefao)
                print(f"{personagem.nome} tomou {dano_chefao} de dano!")
        else:
            print("Opção inválida!")

        if chefao.vida > 0:
            acao_chefao = f"{chefao.nome} atacou"
            dano_chefao = chefao.atacar()
            personagem.receber_dano(dano_chefao)

        # Gerar relatório da batalha
        gerar_relatorio(personagem, chefao, acao_personagem, acao_chefao, dano_personagem, dano_chefao)

    if personagem.vida <= 0:
        print(f"{personagem.nome} foi derrotado pelo {chefao.nome}.")
    elif chefao.vida <= 0:
        print(f"{chefao.nome} foi derrotado por {personagem.nome}.")
        
# Função principal do jogo
def main():
    personagem = criar_personagem()  # Corrigido aqui para criar o personagem corretamente
    
    print(f"\n{personagem}\n")
    
    while personagem.vida > 0:
        print("\nO que você quer fazer?")
        print("1. Atacar")
        print("2. Defender")
        print("3. Esquivar")
        print("4. Usar habilidade especial")
        print("5. Ganhar experiência (Simulação de batalha)")
        print("6. Verificar se pode enfrentar o Chefão")
        print("7. Sair do jogo")
        
        escolha = input("Escolha uma opção (1/2/3/4/5/6/7): ")
        
        if escolha == "1":
            dano = personagem.atacar()
            print(f"Dano causado: {dano}")
        elif escolha == "2":
            defesa = personagem.defender()
            print(f"Defesa realizada: {defesa}")
        elif escolha == "3":
            if personagem.esquivar():
                print(f"{personagem.nome} esquivou com sucesso!")
            else:
                print(f"{personagem.nome} falhou ao tentar esquivar!")
        elif escolha == "4":
            habilidade = input("Escolha uma habilidade (Ataque Poderoso/ Escudo Mágico): ")
            if habilidade in personagem.habilidades:
                habilidade_uso = personagem.habilidades[habilidade]()
                print(f"Dano causado com habilidade: {habilidade_uso}")
            else:
                print("Habilidade inválida!")
        elif escolha == "5":
            pontos = random.randint(50, 150)
            print(f"{personagem.nome} ganhou {pontos} pontos de experiência!")
            personagem.ganhar_experiencia(pontos)
        elif escolha == "6":
            if personagem.nivel >= 5:
                chefao = Chefao(personagem.nivel + 1)  # Chefão sempre tem nível superior ao do jogador
                batalha_com_chefao(personagem, chefao)
            else:
                print(f"Você precisa estar no nível 5 ou superior para enfrentar o chefão.")
        elif escolha == "7":
            print("Saindo do jogo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

        print(f"\n{personagem}\n")

# Executar o jogo
if __name__ == "__main__":
    main()
