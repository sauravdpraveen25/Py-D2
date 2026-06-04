class LimitException(Exception):
    pass


class HDFCBank:

    def __init__(self):
        self.__transaction_limit = 3
        self.__amount_limit = 20000

    def withdraw(self, amount):

        if self.__transaction_limit <= 0:
            raise LimitException(
                "Maximum Transaction Limit Exceeded"
            )

        if amount > self.__amount_limit:
            raise LimitException(
                "Maximum Amount Limit Exceeded"
            )

        self.__amount_limit -= amount
        self.__transaction_limit -= 1

        print("\nTransaction Successful")
        print("Withdrawn Amount:", amount)
        print("Remaining Amount Limit:",
              self.__amount_limit)
        print("Remaining Transaction Limit:",
              self.__transaction_limit)


class AXISBank:

    def __init__(self):
        self.__transaction_limit = 5
        self.__amount_limit = 30000

    def withdraw(self, amount):

        if self.__transaction_limit <= 0:
            raise LimitException(
                "Maximum Transaction Limit Exceeded"
            )

        if amount > self.__amount_limit:
            raise LimitException(
                "Maximum Amount Limit Exceeded"
            )

        self.__amount_limit -= amount
        self.__transaction_limit -= 1

        print("\nTransaction Successful")
        print("Withdrawn Amount:", amount)
        print("Remaining Amount Limit:",
              self.__amount_limit)
        print("Remaining Transaction Limit:",
              self.__transaction_limit)


class ATM:

    def inputAmount(self):

        print("1. HDFC")
        print("2. AXIS")

        choice = int(input("Enter Choice: "))

        if choice == 1:
            bank = HDFCBank()

        elif choice == 2:
            bank = AXISBank()

        else:
            print("Invalid Choice")
            return

        while True:

            try:

                amount = float(
                    input("\nEnter Amount To Withdraw: ")
                )

                bank.withdraw(amount)

            except LimitException as e:

                print(e)
                print("Process Terminated")
                break

            ch = input(
                "\nNext Transaction (yes/no): "
            )

            if ch.lower() == "no":
                print("Process Terminated")
                break


obj = ATM()
obj.inputAmount()