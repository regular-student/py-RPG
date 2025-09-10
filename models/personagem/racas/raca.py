
from enum import Enum
from abc import ABC, abstractmethod

class Visao(Enum):
    NO = "No"
    YES = "18m"
    
class Alinhamento(Enum):
    NEUTRAL = "Neutral"
    ALL = "Todos os alinhamentos"
    ORDER = "Ordem"

class RacaBase(ABC):
    def __init__(self, nome: str, mobilidade, int, alinhamento: Alinhamento, visao: Visao):
        self.nome = nome
        self.mobilidade = mobilidade
        self.alinhamento = alinhamento
        self.visao = visao
