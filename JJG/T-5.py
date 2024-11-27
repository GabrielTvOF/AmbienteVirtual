import random
import time

# Função para simular uma pausa no jogo
def pause(message):
    print(message)
    time.sleep(2)

# Função para iniciar a escolha de classe
def escolher_classe():
    print("Bem-vindo ao RPG - A Jornada das Almas Perdidas!")
    nome = input("Qual o nome do seu personagem? ")
    
    print(f"\nOlá, {nome}! Agora escolha uma classe para sua aventura:")
    print("1 - Guerreiro")
    print("2 - Mago")
    print("3 - Ladrão")
    print("4 - Clérigo")
    print("5 - Druida")
    
    classe = input("Escolha o número correspondente à sua classe: ")
    
    if classe == '1':
        classe_nome = "Guerreiro"
        subclasses = ["Cavaleiro de Aço", "Berserker"]
    elif classe == '2':
        classe_nome = "Mago"
        subclasses = ["Feiticeiro do Fogo", "Mago das Sombras"]
    elif classe == '3':
        classe_nome = "Ladrão"
        subclasses = ["Assassino", "Arqueiro"]
    elif classe == '4':
        classe_nome = "Clérigo"
        subclasses = ["Padroeiro da Luz", "Necromante de Luz"]
    elif classe == '5':
        classe_nome = "Druida"
        subclasses = ["Guardião da Floresta", "Xamã do Vento"]
    else:
        print("Opção inválida. Escolha novamente.")
        return escolher_classe()
    
    print(f"\nVocê escolheu a classe: {classe_nome}.")
    print(f"Você começará sua aventura como um {classe_nome} sem subclasse por enquanto.")
    
    return nome, classe_nome, None, subclasses  # Retorna o nome e a classe sem subclasse inicial

# Função para inicializar os atributos do jogador
def inicializar_jogador(nome, classe, subclasses):
    jogador = {
        'nome': nome,
        'classe': classe,
        'subclasse': None,  # Nenhuma subclasse inicialmente
        'vida': 100,
        'ataque': 20,
        'defesa': 10,
        'experiencia': 0,
        'nivel': 1,
        'itens': [
            {'nome': 'Poção de Cura', 'tipo': 'cura', 'valor': 20},
            {'nome': 'Elixir de Força', 'tipo': 'forca', 'valor': 10},
            {'nome': 'Escudo de Madeira', 'tipo': 'escudo', 'valor': 5}
        ],
        'habilidade': None,
        'habilidade_uso': 1,  # A habilidade especial pode ser usada uma vez por combate
    }
    
    return jogador

# Função para escolher a subclasse no nível 15
def escolher_subclasse(jogador, subclasses):
    if jogador['nivel'] >= 15:
        print(f"\nParabéns, {jogador['nome']}! Você alcançou o nível 15 e agora pode escolher uma subclasse.")
        print("Escolha uma subclasse para sua aventura:")
        for i, subclass in enumerate(subclasses, 1):
            print(f"{i} - {subclass}")
        
        subclass_choice = input("Escolha o número correspondente à sua subclasse: ")
        jogador['subclasse'] = subclasses[int(subclass_choice)-1]
        
        # Adiciona habilidade única para a subclasse escolhida
        if jogador['subclasse'] == "Cavaleiro de Aço":
            jogador['habilidade'] = "Golpe de Aço"
        elif jogador['subclasse'] == "Berserker":
            jogador['habilidade'] = "Fúria Selvagem"
        elif jogador['subclasse'] == "Feiticeiro do Fogo":
            jogador['habilidade'] = "Chama Infernal"
        elif jogador['subclasse'] == "Mago das Sombras":
            jogador['habilidade'] = "Sombra Devastadora"
        elif jogador['subclasse'] == "Assassino":
            jogador['habilidade'] = "Ataque Silencioso"
        elif jogador['subclasse'] == "Arqueiro":
            jogador['habilidade'] = "Tiro Perfurante"
        elif jogador['subclasse'] == "Padroeiro da Luz":
            jogador['habilidade'] = "Cura Divina"
        elif jogador['subclasse'] == "Necromante de Luz":
            jogador['habilidade'] = "Toque da Morte"
        elif jogador['subclasse'] == "Guardião da Floresta":
            jogador['habilidade'] = "Chama da Natureza"
        elif jogador['subclasse'] == "Xamã do Vento":
            jogador['habilidade'] = "Vento Cortante"
        
        print(f"\nVocê escolheu a subclasse: {jogador['subclasse']} e ganhou a habilidade {jogador['habilidade']}.")
        return True
    else:
        print(f"\nVocê precisa alcançar o nível 15 para escolher sua subclasse. Nível atual: {jogador['nivel']}")
        return False

# Função para iniciar a aventura
def iniciar_aventura(jogador, subclasses):
    pause(f"\nVocê, {jogador['nome']}, um {jogador['classe']}, começa sua jornada. As pessoas estão desesperadas.")
    pause("Você encontra um mapa antigo que aponta para o Vale Sombrio, onde o Arauto das Sombras reside.")
    
    print("\nEscolha uma missão para realizar:")
    print("1 - Missão da Caverna Abandonada")
    print("2 - Missão da Cidade Assombrada")
    print("3 - Missão do Bosque das Fadas")
    print("4 - Missão do Dragão Negro")
    print("5 - Missão do Tesouro Perdido")
    
    escolha = input("Escolha uma missão (1, 2, 3, 4 ou 5): ")
    
    if escolha == '1':
        missao_caverna(jogador)
    elif escolha == '2':
        missao_cidade_assombrada(jogador)
    elif escolha == '3':
        missao_bosque_fadas(jogador)
    elif escolha == '4':
        missao_dragao_negro(jogador)
    elif escolha == '5':
        missao_tesouro_perdido(jogador)
    else:
        print("Opção inválida. Tentando novamente.")
        iniciar_aventura(jogador, subclasses)

# Função para a Missão da Caverna Abandonada
def missao_caverna(jogador):
    print("\nVocê entra na Caverna Abandonada. Dizem que um monstro guarda um tesouro lá dentro.")
    print("Você pode: ")
    print("1 - Enfrentar o monstro diretamente.")
    print("2 - Tentar encontrar o tesouro sem enfrentar o monstro.")
    
    escolha = input("Escolha uma opção (1 ou 2): ")
    
    if escolha == '1':
        print("\nVocê enfrenta o monstro e o derrota! Ganha 50 de experiência e um Elixir de Força.")
        jogador['experiencia'] += 50
        jogador['itens'].append({'nome': 'Elixir de Força', 'tipo': 'forca', 'valor': 10})
    elif escolha == '2':
        sucesso = random.choice([True, False])
        if sucesso:
            print("\nVocê encontra o tesouro escondido e ganha 30 de experiência!")
            jogador['experiencia'] += 30
        else:
            print("\nVocê não encontra nada. Melhor tentar da próxima vez.")
    else:
        print("Opção inválida. Tentando novamente.")
        missao_caverna(jogador)

# Função para a Missão da Cidade Assombrada
def missao_cidade_assombrada(jogador):
    print("\nVocê chega à cidade assombrada. Espíritos vagam pelas ruas e você precisa descobrir o que está acontecendo.")
    print("Você pode: ")
    print("1 - Usar magia para afastar os espíritos.")
    print("2 - Investigar a origem da maldição.")
    
    escolha = input("Escolha uma opção (1 ou 2): ")
    
    if escolha == '1':
        print("\nVocê usa magia para afastar os espíritos e encontra uma carta misteriosa.")
        jogador['experiencia'] += 40
        jogador['itens'].append({'nome': 'Carta Misteriosa', 'tipo': 'item', 'valor': 1})
    elif escolha == '2':
        print("\nVocê descobre que a cidade foi amaldiçoada por um feiticeiro. Você derrota o feiticeiro e ganha 60 de experiência.")
        jogador['experiencia'] += 60
    else:
        print("Opção inválida. Tentando novamente.")
        missao_cidade_assombrada(jogador)

# Função para a Missão do Bosque das Fadas
def missao_bosque_fadas(jogador):
    print("\nVocê chega ao Bosque das Fadas. Elas pedem sua ajuda para salvar sua árvore sagrada.")
    print("Você pode: ")
    print("1 - Ajudar as fadas a proteger a árvore.")
    print("2 - Procurar a árvore sagrada por conta própria.")
    
    escolha = input("Escolha uma opção (1 ou 2): ")
    
    if escolha == '1':
        print("\nVocê ajuda as fadas e ganha a confiança delas. Como recompensa, você ganha uma Poção de Cura.")
        jogador['itens'].append({'nome': 'Poção de Cura', 'tipo': 'cura', 'valor': 20})
    elif escolha == '2':
        sucesso = random.choice([True, False])
        if sucesso:
            print("\nVocê encontra a árvore sagrada e ganha 50 de experiência!")
            jogador['experiencia'] += 50
        else:
            print("\nVocê se perde no bosque e não encontra a árvore.")
    else:
        print("Opção inválida. Tentando novamente.")
        missao_bosque_fadas(jogador)

# Função para a Missão do Dragão Negro
def missao_dragao_negro(jogador):
    print("\nVocê chega ao covil do Dragão Negro, que está aterrorizando a região.")
    print("Você pode: ")
    print("1 - Enfrentar o dragão diretamente.")
    print("2 - Tentar encontrar uma forma de derrotá-lo sem combate.")
    
    escolha = input("Escolha uma opção (1 ou 2): ")
    
    if escolha == '1':
        sucesso = random.choice([True, False])
        if sucesso:
            print("\nVocê derrota o Dragão Negro em uma batalha épica! Ganha 100 de experiência e um Escudo de Madeira.")
            jogador['experiencia'] += 100
            jogador['itens'].append({'nome': 'Escudo de Madeira', 'tipo': 'escudo', 'valor': 5})
        else:
            print("\nO Dragão Negro é muito poderoso. Você não sobreviveu ao combate.")
    elif escolha == '2':
        print("\nVocê encontra uma fraqueza no Dragão Negro e o derrota sem batalha direta! Ganha 80 de experiência.")
        jogador['experiencia'] += 80
    else:
        print("Opção inválida. Tentando novamente.")
        missao_dragao_negro(jogador)

# Função para a Missão do Tesouro Perdido
def missao_tesouro_perdido(jogador):
    print("\nVocê chega a uma antiga tumba onde se diz que um grande tesouro está escondido.")
    print("Você pode: ")
    print("1 - Explorar a tumba em busca do tesouro.")
    print("2 - Procurar armadilhas e evitar um possível perigo.")
    
    escolha = input("Escolha uma opção (1 ou 2): ")
    
    if escolha == '1':
        print("\nVocê encontra o tesouro perdido e ganha 70 de experiência!")
        jogador['experiencia'] += 70
    elif escolha == '2':
        sucesso = random.choice([True, False])
        if sucesso:
            print("\nVocê encontra e desativa as armadilhas, ficando com o tesouro! Ganha 90 de experiência.")
            jogador['experiencia'] += 90
        else:
            print("\nAs armadilhas são mais difíceis do que você imaginava e você se machuca.")
            jogador['vida'] -= 20
    else:
        print("Opção inválida. Tentando novamente.")
        missao_tesouro_perdido(jogador)

# Função principal
def main():
    nome, classe, subclass, subclasses = escolher_classe()
    jogador = inicializar_jogador(nome, classe, subclasses)
    
    while jogador['nivel'] < 15:
        iniciar_aventura(jogador, subclasses)
    
    if jogador['nivel'] >= 15:
        escolher_subclasse(jogador, subclasses)

# Iniciar o jogo
if __name__ == "__main__":
    main()
