import random

def _rolar_dados(n_dados, n_lados):
    return sum(random.randint(1, n_lados) for _ in range(n_dados))

def distribuir_classico():
    nomes_atributos = ["forca", "destreza", "constituicao", "inteligencia", "sabedoria", "carisma"]
    atributos = {}
    
    for atributo in nomes_atributos:
        atributos[atributo] = _rolar_dados(3, 6)
    return atributos

def distribuir_aventureiro():
    nomes_atributos = ["força", "destreza", "constituicao", "inteligencia", "sabedoria", "carisma"]
    atributos = {}
    valores_rolados = [_rolar_dados(3, 6) for _ in range(len(nomes_atributos))]
    
    print("Valores rolados:", valores_rolados)
    
    escolhidos = []
    
    for i, nome_atributo in enumerate(nomes_atributos):
        while True:
            try:
                valor_escolhido = int(input(f"Escolhido um valor para {nome_atributo}: "))
                if valor_escolhido in valores_rolados and valor_escolhido not in escolhidos:
                    atributos[nome_atributo] = valor_escolhido
                    escolhidos.append(valor_escolhido)
                    break
                else:
                    print("Valor inválido ou já foi escolhido.")
            except ValueError:
                print("Por favor, insira um número")
                
        return atributos
    
def distribuir_heroico():
    nomes_atributos = ["força", "destreza", "constituicao", "inteligencia", "sabedoria", "carisma"]
    atributos = {}
        
    for atributo in nomes_atributos:
        rolagens = [random.randint(1, 6) for _ in range(4)]
        rolagens.sort()
        soma_dos_maiores = sum(rolagens[1:])
        atributos[atributo] = soma_dos_maiores
            
    return atributos
    
def determinar_atributos(estilo):
    if estilo == "1":
        return distribuir_classico()
    elif estilo == "2":
        return distribuir_aventureiro()
    elif estilo == "3":
        return distribuir_heroico()
    else:
        return {}
    
