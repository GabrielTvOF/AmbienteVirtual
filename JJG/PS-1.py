import random

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

    def ganhar_experiencia(self, pontos):
        """Adicionar experiência ao personagem e evoluir de nível"""
        self.experiencia += pontos
        while self.experiencia >= self.nivel * 100:
            self.experiencia -= self.nivel * 100
            self.subir_nivel()

        # A cada 10 pontos de experiência, há uma chance de ganhar um item
        if self.experiencia % 10 == 0:
            self.ganhar_item()

    def ganhar_item(self):
        """Ganha um item que melhora algum atributo"""
        itens_possiveis = [
            Item("Poção de Força", "forca", 2),
            Item("Poção de Inteligência", "inteligencia", 2),
            Item("Poção de Agilidade", "agilidade", 2),
            Item("Poção de Resistência", "resistencia", 2),
            Item("Elixir de Vida", "vida", 10)
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

# Função para criar um personagem
def criar_personagem():
    nome = input("Qual o nome do seu personagem? ")
    classe = input("Qual a classe do seu personagem (Guerreiro, Mago, Arqueiro)? ")
    
    # Atributos iniciais variam conforme a classe
    if classe.lower() == "guerreiro":
        vida = 100
        forca = 10
        inteligencia = 5
        agilidade = 6
        resistencia = 8
    elif classe.lower() == "mago":
        vida = 70
        forca = 4
        inteligencia = 12
        agilidade = 8
        resistencia = 4
    elif classe.lower() == "arqueiro":
        vida = 80
        forca = 8
        inteligencia = 8
        agilidade = 12
        resistencia = 6
    else:
        print("Classe inválida, criando um personagem genérico.")
        vida = 80
        forca = 7
        inteligencia = 7
        agilidade = 7
        resistencia = 7

    return Personagem(nome, classe, vida, forca, inteligencia, agilidade, resistencia)

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
    personagem = criar_personagem()
    
    print(f"\n{personagem}\n")
    
    while personagem.vida > 0:
        print("\nO que você quer fazer?")
        print("1. Atacar")
        print("2. Defender")
        print("3. Esquivar")
        print("4. Ganhar experiência (Simulação de batalha)")
        print("5. Verificar se pode enfrentar o Chefão")
        print("6. Sair do jogo")
        
        escolha = input("Escolha uma opção (1/2/3/4/5/6): ")
        
        if escolha == "1":
            dano = personagem.atacar()
            print(f"Dano causado: {dano}")
        elif escolha == "2":
            defesa = personagem.defender()
            print(f"Defesa realizada: {defesa}")
        elif escolha == "3":
            personagem.esquivar()
        elif escolha == "4":
            pontos = random.randint(50, 150)
            print(f"{personagem.nome} ganhou {pontos} pontos de experiência!")
            personagem.ganhar_experiencia(pontos)
        elif escolha == "5":
            if personagem.nivel >= 5:
                chefao = Chefao(personagem.nivel + 1)  # Chefão sempre tem nível superior ao do jogador
                batalha_com_chefao(personagem, chefao)
            else:
                print(f"Você precisa estar no nível 5 ou superior para enfrentar o chefão.")
        elif escolha == "6":
            print("Saindo do jogo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

        print(f"\n{personagem}\n")

# Executar o jogo
if __name__ == "__main__":
    main()
