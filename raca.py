from abc import ABC, abstractmethod

#Ainda falta implementar bonus de xp e outros bonus nos personagens como o bonus de dano nos elfos
#Como esses sistemas ainda não existem, eu preferi não implementar eles ainda
#esse bonus talvez poderiam ser implementados com bool ou simples somas/lambda

class Raca(ABC):
    @abstractmethod
    def bonus(self):
        pass

class Humano(Raca):
    def bonus(self):
        return {
            "mobilidade": 9,
            "infravisão": "no",
            "alinhamento": "all"
        }

class Elfo(Raca):
    def bonus(self):
        return {
            "mobilidade": 9,
            "infravisão": 18,
            "alinhamento": "neutral"
        }

class Halfling(Raca):
    def bonus(self):
        return {
            "mobilidade": 6,
            "infravisão": "no",
            "alinhamento": "neutral"
        }
