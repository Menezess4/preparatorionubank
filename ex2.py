produtos={}
def criar_produto(nome, preco):
    if nome in produtos:
        return(False)
    if preco <=0:
        return(False)
    
    produtos[nome]={"preco":preco, "quantidade": 0}
        
    

def add_quantidade(nome, quantidade):
    if nome not in produtos:
        return(False)
    if quantidade <=0:
        return(False)
    produtos[nome]["quantidade"] += quantidade
    return(True)
  


def remove_quantidade(nome, quantidade):
    if quantidade <=0:
        print("remoção de quantidade, não efetuada")
        return(False)
    if nome not in produtos:
        return(False)
    if quantidade >= produtos[nome]["quantidade"]:
        print("remoção de quantidade, não efetuada")
        return(False)
    if quantidade == 0 :
        print("remoção de quantidade, não efetuada")
        return(False)

    produtos[nome]["quantidade"] -= quantidade
    return(True)


def dados(nome):
    if nome not in produtos:
        return(False)
    dados=(produtos[nome])
    return(dados)

def total(nome):
    preco=produtos[nome]["preco"]
    quant=produtos[nome]["quantidade"]
    total=preco*quant
    return(total)

def total_estoque():
    pq=0

    for i in produtos.values():
        pq+=(i["preco"]*i["quantidade"])
         
        print("preco total dos produtos",pq)
    return(pq)

    
    
    
    




criar_produto("ana", 120)
add_quantidade("ana",4)    
remove_quantidade("ana",2)
print(total("ana"))
print(dados("ana")) 
