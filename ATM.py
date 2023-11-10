class TransactionHistory:
    def __init__(self):
        self.history = []

    def add_transaction(self, transaction):
        self.history.append(transaction)

    def display_history(self):
        print("Transaction History:")
        for transaction in self.history:
            print(transaction)

class Withdraw:
    def __init__(self, balance):
        self.balance = balance

    def withdraw_amount(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrawn ${amount}"
        else:
            return "Insufficient balance"

class Deposit:
    def __init__(self, balance):
        self.balance = balance

    def deposit_amount(self, amount):
        self.balance += amount
        return f"Deposited ${amount}"

class Transfer:
    def __init__(self, balance, recipient_balance):
        self.balance = balance
        self.recipient_balance = recipient_balance

    def transfer_amount(self, amount, recipient):
        if amount <= self.balance:
            self.balance -= amount
            recipient.receive_transfer(amount)
            return f"Transferred ${amount} to User {recipient.user_id}"
        else:
            return "Insufficient balance"

class Quit:
    def quit(self):
        return "Thank you for using the ATM. Goodbye!"

class User:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin
        self.balance = 1000000 
        self.transaction_history = TransactionHistory()

    def authenticate(self, entered_pin):
        return self.pin == entered_pin

    def receive_transfer(self, amount):
        self.balance += amount

    def run(self):
        while True:
            print("\nWelcome to the ATM")
            user_pin = input("Please enter your PIN: ")
            if self.authenticate(user_pin):
                print("Authentication successful!")
                while True:
                    print("\nChoose an option:")
                    print("1. Transaction History")
                    print("2. Withdraw")
                    print("3. Deposit")
                    print("4. Transfer")
                    print("5. Quit")

                    option = input("Enter your choice: ")

                    if option == "1":
                        self.transaction_history.display_history()
                    elif option == "2":
                        amount = int(input("Enter the withdrawal amount: "))
                        withdraw = Withdraw(self.balance)
                        result = withdraw.withdraw_amount(amount)
                        self.transaction_history.add_transaction(result)
                        print(result)
                    elif option == "3":
                        amount = int(input("Enter the deposit amount: "))
                        deposit = Deposit(self.balance)
                        result = deposit.deposit_amount(amount)
                        self.transaction_history.add_transaction(result)
                        print(result)
                    elif option == "4":
                        recipient_id = input("Enter recipient's User ID: ")
                        recipient = get_user_by_id(recipient_id)
                        if recipient:
                            amount = int(input("Enter the transfer amount: "))
                            transfer = Transfer(self.balance, recipient.balance)
                            result = transfer.transfer_amount(amount, recipient)
                            self.transaction_history.add_transaction(result)
                            print(result)
                        else:
                            print("Recipient not found.")
                    elif option == "5":
                        quit_option = Quit()
                        print(quit_option.quit())
                        return
                    else:
                        print("Invalid option. Please try again.")

def get_user_by_id(user_id):
    users = {
        "user1": User("user1", "1234"),
        "user2": User("user2", "5678"),
    }
    return users.get(user_id)

if __name__ == "__main__":
    user_id = input("Please enter your User ID: ")
    user = get_user_by_id(user_id)
    if user:
        user.run()
    else:
        print("User not found.")