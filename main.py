from personagem import Personagem
from raca import Humano, Elfo, Halfling
from Classes.guerreiro import Guerreiro
from Classes.mago import Mago
from Classes.clerigo import Clerigo


estilo = input("Escolha o estilo\n"
                "1\t-\tClássico\n"
                "2\t-\tAventureiro\n"
                "3\t-\tHeróico\n-> ")
personagem1 = Personagem(Halfling, estilo)
# personagem2 = Personagem(Elfo, estilo)

print(personagem1)
# print(personagem2)
# print(personagem1.atributos)
