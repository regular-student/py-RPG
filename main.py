from personagem import Personagem
from raca import Humano, Elfo, Halfling
from Classes.guerreiro import Guerreiro
from Classes.mago import Mago
from Classes.clerigo import Clerigo

print("Escolha sua classe: ")
print("1 - Guerreiro")
print("2 - Mago")
print("3 - Clérigo")
escolha_classe = input("-> ")

while classe == None:
    escolha_classe = input("-> ")

    if escolha_classe == "1":
        classe = Guerreiro
    elif escolha_classe == "2":
        classe = Mago
    elif escolha-classe == "3":
        classe = Clerigo

estilo = input("Escolha o estilo\n"
                "1\t-\tClássico\n"
                "2\t-\tAventureiro\n"
                "3\t-\tHeróico\n-> ")
personagem1 = Personagem(Halfling, classe, estilo)
# personagem2 = Personagem(Elfo, estilo)

print(personagem1)
# print(personagem2)
# print(personagem1.atributos)
