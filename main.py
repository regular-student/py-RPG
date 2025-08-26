from personagem import Personagem
from raca import Humano, Elfo, Halfling


estilo = input("Escolha o estilo\n"
                "1\t-\tClássico\n"
                "2\t-\tAventureiro\n"
                "3\t-\tHeróico\n-> ")
personagem1 = Personagem(Elfo, estilo)
personagem2 = Personagem(Elfo, estilo)

print(personagem1)
print(personagem2)
# print(personagem1.atributos)
