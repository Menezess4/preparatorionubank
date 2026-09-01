
contas = {}
historico_contas={}
def criar_contas(nome):
    if nome in contas:
        print('Conta ja existe')
        return (False)
    contas[nome] = 0
    historico_contas[nome]=[]
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
            historico_contas[nome].append(("Deposito",valor))
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
    historico_contas[nome].append(("sacou", valor))
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
    
    historico_contas[ori].append((valor,"foi tranferido para",dest))
    historico_contas[dest].append((valor,"foi recebido de",ori))


    return(True)

transferir("Alice", "bob", 200)
print(contas)
def calcular_total():
    tudo = 0

    for saldo in contas.values():
        tudo += saldo

    print("Saldo disponivel:", tudo)
    return(tudo)
calcular_total()
def maior_saldo():
    maior=0
    contas_maior=None
    for nome,saldo in contas.items():
        if saldo>maior:
            maior=saldo
            contas_maior=nome

    print(f"O {contas_maior} tem o maior saldo de: {maior}")
    return(maior)
maior_saldo()

def historico(nome):
    if nome not in contas :
        return(False)
    return historico_contas[nome]
print(historico("Alice"))
print(historico("bob"))

def resumo_conta(nome):
    if nome not in contas :
        return(False)
    quant=len(historico_contas[nome]) 
    resumo={
    "nome":nome,
    "Saldo":contas[nome],
    "Quantidade de operacoes":quant
    }  
    print(resumo_conta("Alice"))
     
   
    return resumo
