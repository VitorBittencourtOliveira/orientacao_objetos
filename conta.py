
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def depositar(self, valor):
        self.__saldo += valor
        print("Foi depositado R${} na conta do titular {}".format(valor, self.__titular))

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_para_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_para_sacar

    def sacar(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
            print("Foi sacado R${} da conta do titular {}".format(valor, self.__titular))
        else:
            print("O valor R${} passou o limite.".format(valor))

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
        print("Foi transferido R${} da conta do titular {} para o {}".format(valor, self.__titular, destino.__titular))

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"
    
    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}