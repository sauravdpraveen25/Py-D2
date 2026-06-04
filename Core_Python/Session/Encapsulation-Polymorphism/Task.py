class LimitException(Exception):
    pass


class HDFCBank:

    def __init__(self):
        self.__amount_limit = 20000
        self.__transaction_limit = 3

    def withdraw(self, amount):

        if self.__transaction_limit <= 0:
            raise LimitException("Maximum Transaction Limit Exceeded")

        if amount > self.__amount_limit:
            raise LimitException("Maximum Amount Limit Exceeded")

        self.__amount_limit -= amount
        self.__transaction_limit -= 1

        print("Transaction Successful")
        print("Remaining Amount Limit:", self.__amount_limit)
        print("Remaining Transactions:", self.__transaction_limit)


class AXISBank:

    def __init__(self):
        self.__amount_limit = 30000
        self.__transaction_limit = 5

    def withdraw(self, amount):

        if self.__transaction_limit <= 0:
            raise LimitException("Maximum Transaction Limit Exceeded")

        if amount > self.__amount_limit:
            raise LimitException("Maximum Amount Limit Exceeded")

        self.__amount_limit -= amount
        self.__transaction_limit -= 1

        print("Transaction Successful")
        print("Remaining Amount Limit:", self.__amount_limit)
        print("Remaining Transactions:", self.__transaction_limit)


print("1. HDFC")
print("2. AXIS")

choice = int(input("Enter Choice: "))

if choice == 1:
    bank = HDFCBank()

elif choice == 2:
    bank = AXISBank()

else:
    print("Invalid Choice")
    exit()


while True:

    try:

        amount = float(input("\nEnter Amount to Withdraw: "))

        bank.withdraw(amount)

    except LimitException as e:
        print(e)
        print("Process Terminated")
        break

    ch = input("Next Transaction (yes/no): ")

    if ch.lower() == "no":
        print("Process Terminated")
        break