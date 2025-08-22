from personagem import Personagem

personagem1 = Personagem()
estilo = int(input("Escolha o estilo\n"
                "1\t-\tClássico\n"
                "2\t-\tAventureiro\n"
                "3\t-\tHeróico\n-> "))
personagem1.determinar_atributos('2')

print(personagem1)
# print(personagem1.atributos)
