produtos={}

def criar_produto(nome, preco):
    if nome in produtos:
        return(False)
    produtos[nome]=preco
        
    
criar_produto("ana", 120)


def add_quantidade(nome, quantidade):
    if quantidade <=0:
        return(False)
    produtos[nome] += quantidade
    return(True)
add_quantidade("ana",2)  
print(produtos)
