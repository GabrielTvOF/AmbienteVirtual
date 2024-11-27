import time
import random
import personagem
r1 = Avalora = 0
r2 = Thaldar = 0
r3 = Selrith = 0
r4 = Mirandor = 0
reinos = [r1,r2,r3,r4]

    
    def aumentar_coragem(self):
        self.coragem += 1
        print(f"{self.nome} ganhou coragem! Coragem: {self.coragem}")
        
    def aumentar_sabedoria(self):
        self.sabedoria += 1
        print(f"{self.nome} ganhou sabedoria! Sabedoria: {self.sabedoria}")
        
    def aumentar_sacrifio(self):
        self.sacrifio += 1
        print(f"{self.nome} aumentou seu espírito de sacrifício! Sacrifício: {self.sacrifio}")
    
    def exibir_status(self):
        print(f"\nStatus do personagem: \nNome: {self.nome}\nReino: {self.reino}\nCoragem: {self.coragem}\nSabedoria: {self.sabedoria}\nSacrifício: {self.sacrifio}\n")


def introducao():
    print("Bem-vindo a Eryndor, um mundo à beira do colapso.")
    time.sleep(1)
    print("\nVocê é um jovem aventureiro de um reino destruido,atras de respostas de um sobre a profecia que diz que 'o escolhido do Cristal será a chave para o destino de Eryndor'.")
    time.sleep(1)
    nome = input("\nQual o nome do seu personagem?\n ")
    reino = random.shuffle(reinos)
    print(nome,",apos mais um pessadelo decide sair atras de respostas rumo a grande biblioteca de Gardenboir.")

def escolhas_iniciais(personagem):
    print("\nSua viagem começa indo rumo a aldeia no pé da montanha")
    time.sleep(1)
    print("Você pensa por um instante e Decide olhar seu equipamento.")
    time.sleep(1)
    while True:
    print("""Oque você ira levar? 
             1- bolsa com moedas
             2- bolsa de comida
             3- nenhuma""")
    
    escolha = int(input('''\033[1;30mEscolha uma Opção: '''))
                        
    time.sleep(1)
    print("\nO Cristal, em um pesadelo, lhe revela que está escondido em algum lugar nas terras antigas, mas há um preço a pagar.")
    
    while True:
        escolha = input("\nO que você deseja fazer? \n1. Aumentar sua coragem e partir para encontrar o Cristal. \n2. Aumentar sua sabedoria e buscar respostas sobre a lenda do Cristal. \n3. Decidir que é melhor não se envolver e buscar uma vida tranquila.\nEscolha (1, 2 ou 3): ")
        
        if escolha == '1':
            personagem.aumentar_coragem()
            break
        elif escolha == '2':
            personagem.aumentar_sabedoria()
            break
        elif escolha == '3':
            personagem.aumentar_sacrifio()
            break
        else:
            print("\nEscolha inválida. Tente novamente.")
    
    return personagem


def caminho_final(personagem):
    print("\nVocê se aproxima do Cristal de Eternidade e encontra um impasse moral.")
    time.sleep(1)
    print("\nVocê sabe que pode restaurar a paz, mas será que o poder do Cristal é demais para um único ser controlar?")
    time.sleep(1)
    
    while True:
        escolha = input("\nO que você fará? \n1. Restaurar o Cristal para trazer paz, com a certeza de que a magia será controlada. \n2. Destruir o Cristal para evitar que qualquer um o use. \n3. Liberar o poder do Cristal, acreditando que ele pode restaurar o equilíbrio de Eryndor. \nEscolha (1, 2 ou 3): ")
        
        if escolha == '1':
            print("\nVocê restaurou o Cristal e trouxe a paz de volta, mas um novo desafio começa. O poder da magia estará agora mais estável.")
            personagem.aumentar_sabedoria()
            break
        elif escolha == '2':
            print("\nVocê destruiu o Cristal, mas a terra foi devastada por uma magia descontrolada. Eryndor nunca mais será o mesmo.")
            personagem.aumentar_coragem()
            break
        elif escolha == '3':
            print("\nVocê liberou todo o poder do Cristal. O mundo se purifica, mas você se sacrificou para que isso fosse possível.")
            personagem.aumentar_sacrifio()
            break
        else:
            print("\nEscolha inválida. Tente novamente.")
    
    return personagem


def epilogo(personagem):
    print(f"\n{personagem.nome} foi lembrado como um herói, mas o legado de suas escolhas será eternamente debatido entre os reinos.")
    time.sleep(1)
    print("\nO que você fez não será esquecido, mas o mundo de Eryndor nunca será o mesmo.")
    time.sleep(1)
    personagem.exibir_status()
    print("\nFIM DA JORNADA.")

def main():
    personagem = introducao()
    personagem = escolhas_iniciais(personagem)
    personagem = caminho_final(personagem)
    epilogo(personagem)


if __name__ == "__main__":
    main()
