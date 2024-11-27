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
    print(f"Agora, escolha uma subclass:")
    for i, subclass in enumerate(subclasses, 1):
        print(f"{i} - {subclass}")
    
    subclass_choice = input("Escolha o número correspondente à sua subclass: ")
    subclass_nome = subclasses[int(subclass_choice)-1]
    
    print(f"\nVocê escolheu a subclass: {subclass_nome}.")
    return classe_nome, subclass_nome

# Função para iniciar a aventura
def iniciar_aventura(classe, subclass):
    pause(f"\nVocê, um {classe} {subclass}, chega à vila de Ravena. As pessoas estão desesperadas.")
    pause("Você encontra um mapa antigo que aponta para o Vale Sombrio, onde o Arauto das Sombras reside.")
    
    print("\nEscolha o que fazer:")
    print("1 - Investigar a Taverna")
    print("2 - Seguir para o Vale Sombrio")
    print("3 - Procurar por aliados na Guilda dos Aventureiros")
    
    escolha = input("Escolha uma opção (1, 2 ou 3): ")
    
    if escolha == '1':
        investigar_taverna()
    elif escolha == '2':
        seguir_para_vale()
    elif escolha == '3':
        procurar_aliados()
    else:
        print("Opção inválida. Tentando novamente.")
        iniciar_aventura(classe, subclass)

# Função para investigar a taverna
def investigar_taverna():
    pause("\nVocê vai até a taverna e encontra um velho misterioso sentado em um canto.")
    print("Ele diz: 'Ouvi rumores sobre um Arauto das Sombras. Dizem que ele só pode ser derrotado por um herói escolhido.'")
    print("Você pode: ")
    print("1 - Perguntar mais sobre a criatura e a profecia.")
    print("2 - Ignorar o velho e sair da taverna.")
    
    escolha = input("Escolha uma opção (1 ou 2): ")
    
    if escolha == '1':
        print("\nO velho sorri e lhe entrega um amuleto. 'Esse amuleto pode te ajudar contra o Arauto.'")
        pause("Você agora está mais preparado para enfrentar o Arauto das Sombras.")
        # Você ganha um item ou bônus aqui
    elif escolha == '2':
        print("\nVocê decide sair da taverna e seguir seu caminho.")
        pause("Você se prepara para a jornada ao Vale Sombrio.")
    else:
        print("Opção inválida. Tentando novamente.")
        investigar_taverna()

# Função para seguir para o Vale Sombrio
def seguir_para_vale():
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
            combate()
        else:
            print("\nVocê se perde na floresta e precisa voltar para a vila.")
            pause("Você decide tentar novamente em outro momento.")
    elif escolha == '2':
        print("\nO caminho pelas montanhas é longo e cansativo, mas você chega ao Vale Sombrio.")
        pause("Agora, a batalha contra o Arauto das Sombras começa.")
        combate()
    else:
        print("Opção inválida. Tentando novamente.")
        seguir_para_vale()

# Função para procurar aliados
def procurar_aliados():
    pause("\nVocê vai até a Guilda dos Aventureiros.")
    print("Há alguns aventureiros dispostos a se juntar à sua causa, mas eles exigem algo em troca.")
    print("Você pode: ")
    print("1 - Aceitar a oferta e completar uma tarefa para a guilda.")
    print("2 - Recusar a oferta e seguir sozinho.")
    
    escolha = input("Escolha uma opção (1 ou 2): ")
    
    if escolha == '1':
        print("\nVocê aceita a tarefa e sai em busca de um artefato perdido.")
        pause("Após completar a tarefa, você volta para a Guilda e recruta seus aliados.")
    elif escolha == '2':
        print("\nVocê decide seguir sozinho, confiando em sua força e habilidades.")
        pause("Agora, você está pronto para enfrentar o Arauto das Sombras.")
    else:
        print("Opção inválida. Tentando novamente.")
        procurar_aliados()

# Função de combate
def combate():
    pause("\nA batalha começa contra o Arauto das Sombras!")
    resultado = random.choice(["vitória", "derrota"])
    
    if resultado == "vitória":
        print("\nVocê derrotou o Arauto das Sombras e salvou o mundo!")
    else:
        print("\nO Arauto das Sombras é muito forte. Você não sobreviveu à batalha.")
    pause("Fim da aventura!")

# Função principal
def main():
    classe, subclass = escolher_classe()
    iniciar_aventura(classe, subclass)

# Iniciar o jogo
if __name__ == "__main__":
    main()
