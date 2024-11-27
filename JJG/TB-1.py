import random
import time

# Função para simular uma pausa no jogo
def pause(message):
    print(message)
    time.sleep(2)

# Função para calcular dano
def calcular_dano(ataque, defesa):
    dano = ataque - defesa
    if dano < 0:
        dano = 0
    return dano

# Função para o combate
def combate(jogador, inimigo):
    print(f"\nVocê enfrentará {inimigo['nome']}!")
    while jogador['vida'] > 0 and inimigo['vida'] > 0:
        print(f"\n{jogador['nome']} (Nível {jogador['nivel']}) | Vida: {jogador['vida']} | Ataque: {jogador['ataque']} | Defesa: {jogador['defesa']}")
        print(f"{inimigo['nome']} | Vida: {inimigo['vida']} | Ataque: {inimigo['ataque']} | Defesa: {inimigo['defesa']}")
        
        # Exibe itens do jogador
        print(f"\nItens disponíveis: {', '.join([item['nome'] for item in jogador['itens']])}")
        
        # Turno do jogador
        print("\nEscolha uma ação:")
        print("1 - Atacar")
        print("2 - Usar poção (cura 20 de vida)")
        if jogador['habilidade']:
            print(f"3 - Usar habilidade especial: {jogador['habilidade']}")
        print("4 - Usar item")
        escolha = input("Escolha uma opção (1, 2, 3 ou 4): ")
        
        if escolha == '1':
            dano = calcular_dano(jogador['ataque'], inimigo['defesa'])
            inimigo['vida'] -= dano
            print(f"\nVocê atacou {inimigo['nome']} e causou {dano} de dano!")
        elif escolha == '2':
            if jogador['poções'] > 0:
                jogador['vida'] += 20
                jogador['poções'] -= 1
                print("\nVocê usou uma poção de cura e recuperou 20 de vida!")
            else:
                print("\nVocê não tem poções restantes!")
        elif escolha == '3' and jogador['habilidade']:
            if jogador['habilidade_uso'] > 0:
                print(f"\nVocê usou sua habilidade especial: {jogador['habilidade']}!")
                dano = calcular_dano(jogador['ataque'] + 30, inimigo['defesa'])
                inimigo['vida'] -= dano
                jogador['habilidade_uso'] -= 1
            else:
                print("\nVocê não pode usar sua habilidade especial agora!")
        elif escolha == '4':
            usar_item(jogador)
            continue
        else:
            print("Opção inválida. Tente novamente.")
            continue
        
        # Verifica se o inimigo foi derrotado
        if inimigo['vida'] <= 0:
            print(f"\nVocê derrotou {inimigo['nome']}!")
            jogador['experiencia'] += 20
            break
        
        # Turno do inimigo
        print(f"\n{inimigo['nome']} está atacando...")
        dano_inimigo = calcular_dano(inimigo['ataque'], jogador['defesa'])
        jogador['vida'] -= dano_inimigo
        print(f"\n{inimigo['nome']} causou {dano_inimigo} de dano em você!")
        
        # Verifica se o jogador foi derrotado
        if jogador['vida'] <= 0:
            print(f"\nVocê foi derrotado por {inimigo['nome']}!")
            break

    # Após o combate, verifique o nível
    if jogador['experiencia'] >= 100:
        jogador['nivel'] += 1
        jogador['experiencia'] = 0
        print(f"\nParabéns! Você subiu para o nível {jogador['nivel']}!")

        # Permite escolher uma subclasse ao atingir nível 15
        if jogador['nivel'] == 15:
            escolher_subclasse(jogador)

# Função para escolher uma subclasse quando atingir o nível 15
def escolher_subclasse(jogador):
    print("\nVocê atingiu o nível 15! Escolha uma nova subclasse!")
    print("1 - Cavaleiro de Aço (Defesa e Controle)")
    print("2 - Berserker (Aumento de força e dano)")
    print("3 - Feiticeiro do Fogo (Controle de Fogo)")
    print("4 - Mago das Sombras (Magias de Ilusão e Sombras)")
    print("5 - Assassino (Ataques furtivos e rápidos)")
    print("6 - Arqueiro (Ataques à distância e precisão)")
    print("7 - Padroeiro da Luz (Curas e proteção)")
    print("8 - Necromante de Luz (Controle dos mortos e feitiçaria)")
    print("9 - Guardião da Floresta (Transformação em animais e controle da natureza)")
    print("10 - Xamã do Vento (Controle do vento e agilidade)")

    escolha = input("Escolha uma subclasse (1-10): ")

    subclasses = [
        "Cavaleiro de Aço", "Berserker", "Feiticeiro do Fogo", "Mago das Sombras",
        "Assassino", "Arqueiro", "Padroeiro da Luz", "Necromante de Luz", 
        "Guardião da Floresta", "Xamã do Vento"
    ]
    habilidades = {
        "Cavaleiro de Aço": "Corte de Aço",
        "Berserker": "Fúria Selvagem",
        "Feiticeiro do Fogo": "Chama Infernal",
        "Mago das Sombras": "Ilusão Sombria",
        "Assassino": "Golpe Mortal",
        "Arqueiro": "Tiro Perfeito",
        "Padroeiro da Luz": "Luz Divina",
        "Necromante de Luz": "Ressurreição Sombria",
        "Guardião da Floresta": "Forma de Lobo",
        "Xamã do Vento": "Rajada de Vento"
    }
    
    jogador['subclasse'] = subclasses[int(escolha)-1]
    jogador['habilidade'] = habilidades[jogador['subclasse']]
    jogador['habilidade_uso'] = 1  # Habilidade especial pode ser usada uma vez por combate
    print(f"\nVocê escolheu a subclasse {jogador['subclasse']} com a habilidade {jogador['habilidade']}!")

# Função para usar um item
def usar_item(jogador):
    print("\nEscolha um item para usar:")
    for i, item in enumerate(jogador['itens']):
        print(f"{i+1} - {item['nome']}")
    escolha = int(input("Escolha o número do item: ")) - 1
    
    if escolha < 0 or escolha >= len(jogador['itens']):
        print("\nItem inválido!")
        return
    
    item = jogador['itens'][escolha]
    if item['tipo'] == 'cura':
        jogador['vida'] += item['valor']
        jogador['itens'].remove(item)
        print(f"\nVocê usou a {item['nome']} e recuperou {item['valor']} de vida!")
    elif item['tipo'] == 'forca':
        jogador['ataque'] += item['valor']
        jogador['itens'].remove(item)
        print(f"\nVocê usou a {item['nome']} e seu ataque aumentou em {item['valor']}!")
    elif item['tipo'] == 'escudo':
        jogador['defesa'] += item['valor']
        jogador['itens'].remove(item)
        print(f"\nVocê usou a {item['nome']} e sua defesa aumentou em {item['valor']}!")
    elif item['tipo'] == 'habilidade':
        if item['habilidade']:
            jogador['habilidade'] = item['habilidade']
            jogador['habilidade_uso'] = 1
            jogador['itens'].remove(item)
            print(f"\nVocê usou o {item['nome']} e agora pode usar a habilidade {item['habilidade']}!")
    elif item['tipo'] == 'magia':
        if item['nome'] == 'Pergaminho de Fogo':
            dano = 30
            inimigo['vida'] -= dano
            inimigo['defesa'] -= 5
            print(f"\nVocê usou o {item['nome']} e causou {dano} de dano ao inimigo, além de reduzir sua defesa!")

# Função para iniciar a jornada
def iniciar_jornada():
    jogador = {
        'nome': 'Herói',
        'vida': 100,
        'ataque': 20,
        'defesa': 10,
        'experiencia': 0,
        'nivel': 1,
        'poções': 3,
        'subclasse': None,
        'habilidade': None,
        'habilidade_uso': 0,
        'itens': [
            {'nome': 'Poção de Cura', 'tipo': 'cura', 'valor': 20},
            {'nome': 'Elixir de Força', 'tipo': 'forca', 'valor': 10},
            {'nome': 'Escudo de Madeira', 'tipo': 'escudo', 'valor': 5},
            {'nome': 'Poção de Velocidade', 'tipo': 'habilidade', 'habilidade': 'Aumento de Velocidade', 'valor': 0},
            {'nome': 'Espada Mágica de Fogo', 'tipo': 'forca', 'valor': 15},
            {'nome': 'Cristal da Cura', 'tipo': 'cura', 'valor': 50}
        ]
    }
    
    inimigos = [
        {'nome': 'Arauto das Sombras', 'vida': 150, 'ataque': 25, 'defesa': 15},
        {'nome': 'Lobisomem Selvagem', 'vida': 100, 'ataque': 20, 'defesa': 10},
        {'nome': 'Esqueleto Guerreiro', 'vida': 80, 'ataque': 15, 'defesa': 5}
    ]
    
    print("\nVocê está entrando no Vale Sombrio...")
    inimigo = random.choice(inimigos)  # Inimigo aleatório
    combate(jogador, inimigo)

# Função principal
def main():
    iniciar_jornada()

# Iniciar o jogo
if __name__ == "__main__":
    main()
