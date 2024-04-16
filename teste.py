def criar_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def depositar(conta, valor):
    conta["saldo"] += valor

def saque(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("Saldo é {} e o limite de {}.".format(conta["saldo"],conta["limite"]))