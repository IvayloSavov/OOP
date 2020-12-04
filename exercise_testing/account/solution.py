class Account:
    def __init__(self, owner: str, amount: int = 0, transactions=None):
        self.owner = owner
        self.amount = amount
        if transactions is None:
            self._transactions = []
        else:
            self._transactions = transactions

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        self.validate_transaction(account=self, amount_to_add=amount)

    @property
    def balance(self):
        return sum([t for t in self._transactions]) + self.amount

    @staticmethod
    def validate_transaction(account: "Account", amount_to_add):
        if account.balance + amount_to_add < 0:
            raise ValueError("sorry cannot go in debt!")
        account._transactions.append(amount_to_add)
        return f"New balance: {account.balance}"

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"  # Here it may be good to use another self

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, item):
        return self._transactions[item]

    def __gt__(self, other):
        return self.balance > other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __add__(self, other):
        return Account(owner=str(self.owner + "&" + other.owner), amount=self.amount + other.amount,
                       transactions=self._transactions + other._transactions)

    def __ge__(self, other):
        return self.balance >= other.balance

    def __le__(self, other):
        return self.balance <= other.balance


if __name__ == "__main__":
    acc = Account('bob', 10)
    acc2 = Account('john')
    print(acc)
    print(repr(acc))
    acc.add_transaction(20)
    acc.add_transaction(-20)
    acc.add_transaction(30)
    print(acc.balance)
    print(len(acc))
    for transaction in acc:
        print(transaction)
    print(acc[1])
    print(list(acc))
    print(list(reversed(acc)))
    acc2.add_transaction(10)
    acc2.add_transaction(60)
    print(acc > acc2)
    print(acc >= acc2)
    print(acc < acc2)
    print(acc <= acc2)
    print(acc == acc2)
    print(acc != acc2)
    acc3 = acc + acc2
    print(acc3)
    print(acc3._transactions)
