class BankAccount:
    def __init__(self, owner: str, initial_balance: float = 0.0) -> None:
        if initial_balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным")
        
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        
        self.balance += amount
        print(f"Пополнение на {amount} руб. Новый баланс: {self.balance} руб.")

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        
        if amount > self.balance:
            raise ValueError(
                f"Недостаточно средств. Баланс: {self.balance} руб., "
                f"запрос: {amount} руб."
            )
        
        self.balance -= amount
        print(f"Снятие {amount} руб. Новый баланс: {self.balance} руб.")

    def get_balance(self) -> float:
        return self.balance

    def __str__(self) -> str:
        return f"Счёт {self.owner}: {self.balance} руб."


if __name__ == "__main__":
    account = BankAccount("Иван Петров", 1000.0)
    print(f"\n{account}")
    
    print("\n1. Пополнение счёта")
    account.deposit(500.0)
    account.deposit(250.0)
    
    print(f"\nТекущий баланс: {account.get_balance()} руб.")
    
    print("\n2. Снятие денег")
    account.withdraw(300.0)
    account.withdraw(1000.0)
    
    print(f"\nИтоговый баланс: {account.get_balance()} руб.")
    
    print("\n3. Попытка некорректных операций")
    
    try:
        print("\n3.1. Попытка снять больше, чем есть:")
        account.withdraw(5000.0)
    except ValueError as e:
        print(f"Ошибка: {e}")
    
    try:
        print("\n3.2. Попытка пополнить на отрицательную сумму:")
        account.deposit(-100.0)
    except ValueError as e:
        print(f"Ошибка: {e}")
    
    try:
        print("\n3.3. Попытка снять ноль:")
        account.withdraw(0)
    except ValueError as e:
        print(f"Ошибка: {e}")
    
    print(f"\n{account}")
