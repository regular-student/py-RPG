import random

def _rolar_dados(n_dados, n_lados):
    return sum(random.randint(1, n_lados) for _ in range(n_dados))

def _rolar_4d6_descartar_menor():
    rolagens = [random.randint(1, 6) for _ in range(4)]
    rolagens.sort()
    return sum(rolagens[1:])

def rolar_dados_aventureiro():
    nomes_atributos = ["forca", "destreza", "constituicao", "inteligencia", "sabedoria", "carisma"]
    return [_rolar_dados(3, 6) for _ in range(len(nomes_atributos))]

def rolar_dados_heroico():
    return [_rolar_4d6_descartar_menor() for _ in range(6)]

def distribuir_classico():
    nomes_atributos = ["forca", "destreza", "constituicao", "inteligencia", "sabedoria", "carisma"]
    atributos = {}
    for atributo in nomes_atributos:
        atributos[atributo] = _rolar_dados(3, 6)
    return atributos

def determinar_atributos(estilo):
    if estilo == "1":
        # Apenas o estilo 1 é tratado aqui diretamente.
        return distribuir_classico()