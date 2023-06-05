class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    
    def deposit(self, amount):
        self.balance += amount
        print("Баланс пополнен на", amount, "рублей.")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств на счете.")
        else:
            self.balance -= amount
            print("Снято", amount, "рублей.")
    
    def check_balance(self):
        print("Текущий баланс:", self.balance, "рублей.")


# Пример использования
account = BankAccount(1000)  # Создаем банковский аккаунт с начальным балансом 1000 рублей
account.check_balance()  # Проверяем баланс (1000 рублей)
account.deposit(500)  # Пополняем баланс на 500 рублей
account.check_balance()  # Проверяем баланс (1500 рублей)
account.withdraw(200)  # Снимаем 200 рублей
account.check_balance()  # Проверяем баланс (1300 рублей)
account.withdraw(1500)  # Пытаемся снять больше, чем есть на счете