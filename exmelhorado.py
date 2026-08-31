
contas = {}
def criar_contas(nome):
    if nome in contas:
        print('Conta ja existe')
        return (False)
    contas[nome] = 0
criar_contas('Alice')
criar_contas('bob')
print(contas)
def depositar(nome,valor):
    if nome in contas:
        if valor <= 0:
            print('N existe deposito abaixo de 0')
            return (False)
        else:
            contas[nome] += valor
            print(f'O valor de {valor} atribuido com sucesso')
    else:
        print('Conta n existe na tabela')
        return (False)
depositar('Alice',1000)
depositar('bob',1000)
print(contas)
def sacar(nome,valor):
    if nome in contas:
        if valor <= 0 :
            print('N existe conta abaixo de 0')
            return (False)
        else:
            print(f'O valor de {valor} foi sacado com sucesso')
    else:
        print('Conta n existe na tabela')
        return (False)
    if valor > contas[nome] :
            print('Valor inexistente')
            return(False)
    contas[nome] -= valor
sacar('Alice',500)
print(contas)
def consultar_saldo(nome):
    if nome not in contas:
        print('conta nao existe')
        return(False)
    
    print(f'Saldo de {nome}: {contas[nome]}')
    return(contas[nome])
def transferir(ori, dest, valor):
    if ori not in contas:
        print('Contas nao existem')
        return(False)
        
    if dest not in contas:
        print('Contas nao existem')
        return(False)
        
    if contas[ori]  < valor or valor <=0 :
        return (False)  
    contas[ori]-=valor
    contas[dest]+=valor
    return(True)

transferir("Alice", "bob", 200)
print(contas)
