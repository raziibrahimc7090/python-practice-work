class Payment:
    def pay(self, amount):
        print(f"Processing payment of {amount}")


class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")


class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI.")


class WalletPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Wallet.")


payments = [CreditCardPayment(), UPIPayment(), WalletPayment()]

for payment in payments:
    payment.pay(500)