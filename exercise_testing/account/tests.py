from .solution import Account
import unittest


class AccountTest(unittest.TestCase):
    def setUp(self) -> None:
        self.account = Account("Ivaylo", 100)

    def test_init(self):
        self.assertEqual(self.account.owner, "Ivaylo")
        self.assertEqual(self.account.amount, 100)
        self.assertEqual(len(self.account._transactions), 0)  # TODO: Might be too much

    def test_add_transaction_value_error(self):
        self.assertRaises(ValueError, self.account.add_transaction, "baba")

    def test_add_transaction_correct(self):
        self.account.add_transaction(10)
        self.assertEqual(self.account._transactions, [10])

    def test_validate_transaction_value_error(self):
        self.assertRaises(ValueError, Account.validate_transaction, self.account, -200)

    def test_validate_transaction_correct(self):
        res = Account.validate_transaction(self.account, 100)
        self.assertEqual(res, "New balance: 200")

    def test_balance(self):
        self.assertEqual(self.account.balance, 100)
        self.account.add_transaction(10)  # TODO: Might be a problem
        self.assertEqual(self.account.balance, 110)

    def test_str(self):
        res = self.account.__str__()
        self.assertEqual(res, "Account of Ivaylo with starting amount: 100")

    def test_repr(self):
        res = self.account.__repr__()
        self.assertEqual(res, "Account(Ivaylo, 100)")

    def test_len(self):
        self.assertEqual(len(self.account), 0)

    def test_get_item(self):
        self.account.add_transaction(10)
        self.assertEqual(self.account[0], 10)

    def test_eq(self):
        account_2 = Account("Bogomila", 100)
        self.assertTrue(self.account == account_2)

    def test_gt(self):
        account_2 = Account("Bogomila", 10)
        self.assertTrue(self.account > account_2)

    def test_lt(self):
        account_2 = Account("Bogomila", 200)
        self.assertTrue(self.account < account_2)

    def test_ge(self):
        account_2 = Account("Bogomila", 100)
        account_3 = Account("Maria", 90)
        self.assertTrue(self.account >= account_2)
        self.assertTrue(self.account >= account_3)

    def test_add(self):
        account_2 = Account("Bogomila", 100)
        new_account = self.account + account_2
        self.assertEqual(new_account.owner, "Ivaylo&Bogomila")
        self.assertEqual(new_account.amount, 200)
        self.assertEqual(new_account._transactions, [])
        self.assertEqual(repr(new_account), 'Account(Ivaylo&Bogomila, 200)')

    def test_le(self):
        account_2 = Account("Bogomila", 100)
        account_3 = Account("Maria", 120)
        self.assertTrue(self.account <= account_2)
        self.assertTrue(self.account < account_3)

    def test_not_eq(self):
        account_2 = Account("Bogomila", 50)
        self.assertTrue(self.account != account_2)

    def test_validateTransaction_staticMethod(self):
        import inspect
        self.assertTrue(isinstance(inspect.getattr_static(self.account, 'validate_transaction'), staticmethod))

    def test_list(self):
        self.account.add_transaction(10)
        self.account.add_transaction(20)
        self.account.add_transaction(30)
        self.assertEqual(list(self.account), [10, 20, 30])

    def test_reversed(self):
        self.account.add_transaction(10)
        self.account.add_transaction(20)
        self.account.add_transaction(30)
        res = list(reversed(self.account))
        self.assertEqual(res, [30, 20, 10])


if __name__ == "__main__":
    unittest.main()