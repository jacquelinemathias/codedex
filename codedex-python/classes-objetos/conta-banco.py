# Create a file called bank_accounts.py.

# Let's define a BankAccount class. Then, let's use the __init__() method to set the following attributes:

#     first_name (string)
#     last_name (string)
#     account_id (integer)
#     account_type (string)
#     pin (integer)
#     balance (float)

# Next, let's create three methods:

#     .deposit(): Add money into the account and return the new balance.
#     .withdraw(): Take money out by subtracting from balance and returning the withdrawn amount.
#     .display_balance(): Print the current value of balance.

# Lastly, initialize a new object from the BankAccount class and use these methods to do the following:

#     Deposit $96 in the account.
#     Withdraw $25 from the account.
#     Print the current account balance.

class Banco:
    def __init__(self, nome, sobrenome, id_conta, tipo_conta, senha, saldo):
        self.nome = nome
        self.sobrenome = sobrenome
        self.id_conta = id_conta
        self.tipo_conta = tipo_conta
        self.senha = senha
        self.saldo = saldo
    
    def depositar(self):
        valor_deposito = float(input('Quanto você deseja depositar na conta? '))
        self.saldo = self.saldo + valor_deposito
        return self.saldo
    
    def sacar(self):
        valor_sacado = float(input('Quanto dinheiro você deseja sacar? '))
        self.saldo = self.saldo - valor_sacado
        return self.saldo
    
    def display(self):
        print(self.saldo)

jac = Banco('Jacqueline', 'Mathias', 1234, 'Conta Corrente', 5678, 0.0)
jac.depositar()
jac.sacar()
jac.display()