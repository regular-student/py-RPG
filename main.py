# main.py

from models.personagem import Personagem, Guerreiro, Mago, Clerigo, Humano, Elfo, Halfling
from services.distribuicao_atributos import determinar_atributos # Importa a nova função

# --- Esta parte é a VIEW (exibição de menus) e o CONTROLLER (captura de input) ---

# Função para escolher a classe
def escolher_classe():
    while True:
        print("Escolha sua classe: ")
        print("1\t-\tGuerreiro")
        print("2\t-\tMago")
        print("3\t-\tClérigo")
        escolha = input("-> ")
        if escolha == "1":
            return Guerreiro
        elif escolha == "2":
            return Mago
        elif escolha == "3":
            return Clerigo
        else:
            print("Opção inválida, tente novamente.\n")

# Função para escolher a raça
def escolher_raca():
    while True:
        print("\nEscolha a raça: ")
        print("1\t-\tHumano")
        print("2\t-\tElfo")
        print("3\t-\tHalfling")
        escolha = input("-> ")
        if escolha == "1":
            return Humano
        elif escolha == "2":
            return Elfo
        elif escolha == "3":
            return Halfling
        else:
            print("Opção inválida, tente novamente.\n")

# Função para escolher o estilo de atributos
def escolher_estilo_atributos():
    while True:
        print("\nEscolha o estilo de geração de atributos: ")
        print("1\t-\tClássico (3d6)")
        print("2\t-\tAventureiro (escolha onde alocar)")
        print("3\t-\tHeróico (4d6, descarta o menor)")
        escolha = input("-> ")
        if escolha in ["1", "2", "3"]:
            return escolha
        else:
            print("Opção inválida, tente novamente.\n")

# --- Lógica principal do Controller ---
def main():
    classe_escolhida = escolher_classe()
    raca_escolhida = escolher_raca()
    estilo_escolhido = escolher_estilo_atributos()

    # Controller chama o serviço para obter os atributos
    atributos_base = determinar_atributos(estilo_escolhido)

    # Controller cria o Model (Personagem) com os dados coletados
    personagem_criado = Personagem(raca_escolhida, classe_escolhida, atributos_base)

    # Controller interage com a View para exibir o resultado
    print("\n•\t•\t•\t Personagem Criado\t•\t•\t•\t")
    print(personagem_criado)
    personagem_criado.classe.exibir_habilidades()

if __name__ == "__main__":
    main()