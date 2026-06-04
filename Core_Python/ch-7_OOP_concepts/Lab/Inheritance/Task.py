import random


class BankInfo:

    def __init__(self, fn, ln, gender, address):
        self.fn = fn
        self.ln = ln
        self.gender = gender
        self.address = address


class BankAccount:

    def __init__(self, amount, info):
        self.acno = random.randint(
            1000000000000,
            9999999999999
        )
        self.amount = amount
        self.info = info


class Saving(BankAccount):

    min_amount = 10000
    rate = 6

    def calculate_interest(self, months):

        interest = (
            self.amount *
            self.rate *
            months
        ) / (100 * 12)

        return interest

    def display_profile(self, months):

        print("\n----- CUSTOMER PROFILE -----")

        print("First Name :", self.info.fn)
        print("Last Name  :", self.info.ln)
        print("Gender     :", self.info.gender)
        print("Address    :", self.info.address)

        print("Account No :", self.acno)
        print("Amount     :", self.amount)

        print("\nAccount Type      : Saving")
        print("Months            :", months)
        print("Rate of Interest  :", self.rate, "%")
        print("Interest          :", self.calculate_interest(months))


class Current(BankAccount):

    min_amount = 5000

    def display_profile(self):

        print("\n----- CUSTOMER PROFILE -----")

        print("First Name :", self.info.fn)
        print("Last Name  :", self.info.ln)
        print("Gender     :", self.info.gender)
        print("Address    :", self.info.address)

        print("Account No :", self.acno)
        print("Amount     :", self.amount)

        print("\nAccount Type : Current")
        print("Rate        : No Interest")


# MAIN

fn = input("Enter First Name: ")
ln = input("Enter Last Name: ")
gender = input("Enter Gender: ")
address = input("Enter Address: ")

info = BankInfo(fn, ln, gender, address)

account_type = input(
    "Select Account Type (Saving/Current): "
)

account = None

for attempt in range(3):

    amount = float(
        input("Enter Amount: ")
    )

    if account_type.lower() == "saving":

        if amount >= Saving.min_amount:

            account = Saving(amount, info)
            break

        else:
            print(
                "Minimum Amount for Saving Account is 10000"
            )

    elif account_type.lower() == "current":

        if amount >= Current.min_amount:

            account = Current(amount, info)
            break

        else:
            print(
                "Minimum Amount for Current Account is 5000"
            )

else:

    print(
        "\nMaximum 3 Attempts Exceeded."
    )
    exit()


if account_type.lower() == "saving":

    months = int(
        input("Enter Number of Months: ")
    )

    account.display_profile(months)

else:

    account.display_profile()