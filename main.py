from personagem import Personagem
from raca import Humano, Elfo, Halfling
from Classes.guerreiro import Guerreiro
from Classes.mago import Mago
from Classes.clerigo import Clerigo

classe = None
while classe is None:
    print("Escolha sua classe: ")
    print("1\t-\tGuerreiro")
    print("2\t-\tMago")
    print("3\t-\tClérigo")
    escolha_classe = input("-> ")

    if escolha_classe == "1":
        classe = Guerreiro
    elif escolha_classe == "2":
        classe = Mago
    elif escolha_classe == "3":
        classe = Clerigo
    else:
        print("Opção inválida, tente novamente.\n")

estilo = None
while estilo is None:
    print("\nEscolha o estilo: ")
    print("1\t-\tClássico")
    print("2\t-\tAventureiro")
    print("3\t-\tHeróico")
    estilo = input("-> ")

raca = None
while raca is None:
    print("\nEscolha a raça: ")
    print("1\t-\tHumano")
    print("2\t-\tElfo")
    print("3\t-\tHalfling")
    escolha_raca = input("-> ")

    if escolha_raca == "1":
        raca = Humano
    elif escolha_raca == "2":
        raca = Elfo
    elif escolha_raca == "3":
        raca = Halfling
    else:
        print("Opção inválida, tente novamente.\n")


personagem1 = Personagem(raca, classe, estilo)

print("\n•\t•\t•\t Personagem Criado\t•\t•\t•\t")
print(personagem1)
personagem1.classe.exibir_habilidades()
