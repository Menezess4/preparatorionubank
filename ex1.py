contas={}

def criar_contas(login,senha):
    
    if login in contas:
        print('Conta ja existe')
        return (False)
    
    contas[login]={
        "senha": senha,
        "saldo": 0
    }

    print('Conta criada com sucesso')
    return(True)

def depositar(login, valor):
    if login in contas:
        if valor <= 0 or login not in contas :
            print('Nao permitimos valores de 0 ou menor que ele ou ocorreu um erro na criacao de sua conta ')
            return(False)
        else:
            contas[login]["saldo"] += valor
            print('Deposito Feito')
            return(True)
print(criar_contas('Gustavo','1234'))
print(depositar('Gustavo',300))
print(contas)
