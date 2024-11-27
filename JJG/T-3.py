import random
import time

# Função para simular uma pausa no jogo
def pause(message):
    print(message)
    time.sleep(2)

# Função para iniciar a escolha de classe
def escolher_classe():
    print("Bem-vindo ao RPG - A Jornada das Almas Perdidas!")
    print("Escolha uma classe para sua aventura:")
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
    
    return classe_nome, None, subclasses  # Não há subclasse escolhida inicialmente

# Função para inicializar os atributos do jogador
def inicializar_jogador(classe, subclasses):
    jogador = {
        'nome': 'Herói',
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
        print("\nParabéns! Você alcançou o nível 15 e agora pode escolher uma subclasse.")
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
    pause(f"\nVocê, um {jogador['classe']}, começa sua jornada. As pessoas estão desesperadas.")
    pause("Você encontra um mapa antigo que aponta para o Vale Sombrio, onde o Arauto das Sombras reside.")
    
    print("\nEscolha o que fazer:")
    print("1 - Investigar a Taverna")
    print("2 - Seguir para o Vale Sombrio")
    print("3 - Procurar por aliados na Guilda dos Aventureiros")
    print("4 - Aceitar uma missão paralela")
    
    escolha = input("Escolha uma opção (1, 2, 3 ou 4): ")
    
    if escolha == '1':
        investigar_taverna(jogador)
    elif escolha == '2':
        seguir_para_vale(jogador, subclasses)
    elif escolha == '3':
        procurar_aliados(jogador)
    elif escolha == '4':
        missao_paralela(jogador)
    else:
        print("Opção inválida. Tentando novamente.")
        iniciar_aventura(jogador, subclasses)

# Função para missão paralela
def missao_paralela(jogador):
    pause("\nVocê encontra um NPC que lhe oferece uma missão paralela.")
    print("A missão é: 'Vá até a caverna próxima e traga a gema da verdade.'")
    sucesso = random.choice([True, False])
    
    if sucesso:
        jogador['experiencia'] += 30
        print("\nVocê completou a missão e ganhou 30 de experiência!")
    else:
        print("\nA missão foi fracassada. Você perdeu tempo, mas ainda segue na jornada.")
    
    pause("Você volta para a estrada principal.")

# Função para investigar a taverna
def investigar_taverna(jogador):
    pause("\nVocê vai até a taverna e encontra um velho misterioso sentado em um canto.")
    print("Ele diz: 'Ouvi rumores sobre um Arauto das Sombras. Dizem que ele só pode ser derrotado por um herói escolhido.'")
    print("Você pode: ")
    print("1 - Perguntar mais sobre a criatura e a profecia.")
    print("2 - Ignorar o velho e sair da taverna.")
    
    escolha = input("Escolha uma opção (1 ou 2): ")
    
    if escolha == '1':
        print("\nO velho sorri e lhe entrega um amuleto. 'Esse amuleto pode te ajudar contra o Arauto.'")
        jogador['itens'].append({'nome': 'Amuleto da Sorte', 'tipo': 'buff', 'valor': 1})
        pause("Você agora está mais preparado para enfrentar o Arauto das Sombras.")
    elif escolha == '2':
        print("\nVocê decide sair da taverna e seguir seu caminho.")
        pause("Você se prepara para a jornada ao Vale Sombrio.")
    else:
        print("Opção inválida. Tentando novamente.")
        investigar_taverna(jogador)

# Função para seguir para o Vale Sombrio
def seguir_para_vale(jogador, subclasses):
    pause("\nVocê começa sua jornada rumo ao Vale Sombrio.")
    print("O caminho é traiçoeiro e você encontra uma bifurcação.")
    print("Você pode: ")
    print("1 - Tomar o caminho pela floresta, mais rápido, mas arriscado.")
    print("2 - Tomar o caminho pelas montanhas, mais seguro, mas mais longo.")
    
    escolha = input("Escolha uma opção (1 ou 2): ")
    
    if escolha == '1':
        sucesso = random.choice([True, False])
        if sucesso:
            print("\nVocê atravessa a floresta com sucesso, mas encontra um bando de lobos!")
            combate(jogador)
        else:
            print("\nVocê se perde na floresta e precisa voltar para a vila.")
            pause("Você decide tentar novamente em outro momento.")
    elif escolha == '2':
        print("\nO caminho pelas montanhas é longo e cansativo, mas você chega ao Vale Sombrio.")
        pause("Agora, a batalha contra o Arauto das Sombras começa.")
        combate(jogador)
    else:
        print("Opção inválida. Tentando novamente.")
        seguir_para_vale(jogador, subclasses)

# Função de combate
def combate(jogador):
    pause(f"\nA batalha começa contra um inimigo no Vale Sombrio! Nível do jogador: {jogador['nivel']}")
    
    if jogador['habilidade']:
        print(f"\nVocê pode usar sua habilidade especial: {jogador['habilidade']}")
    
    inimigo_vida = random.randint(50, 100)
    jogador_vida = jogador['vida']
    while jogador_vida > 0 and inimigo_vida > 0:
        ataque_jogador = random.randint(5, 15) + jogador['ataque']
        ataque_inimigo = random.randint(5, 15)
        
        inimigo_vida -= ataque_jogador
        jogador_vida -= ataque_inimigo
        
        print(f"\nVocê atacou o inimigo com {ataque_jogador} de dano!")
        print(f"O inimigo atacou você com {ataque_inimigo} de dano!")
        print(f"Inimigo Vida: {inimigo_vida} | Sua Vida: {jogador_vida}")
        
        if inimigo_vida <= 0:
            print("\nVocê derrotou o inimigo!")
            jogador['experiencia'] += 50
            print(f"Você ganhou 50 de experiência!")
            break
        elif jogador_vida <= 0:
            print("\nVocê foi derrotado... Fim da aventura.")
            break

# Função principal
def main():
    classe, subclass, subclasses = escolher_classe()
    jogador = inicializar_jogador(classe, subclasses)
    while jogador['nivel'] < 15:
        iniciar_aventura(jogador, subclasses)
    
    if jogador['nivel'] >= 15:
        escolher_subclasse(jogador, subclasses)

# Iniciar o jogo
if __name__ == "__main__":
    main()
