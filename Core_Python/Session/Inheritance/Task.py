class BankInfo:

    def __init__(self, fn, ln, gender, address):
        self.fn = fn
        self.ln = ln
        self.gender = gender
        self.address = address


class BankAccount:

    def __init__(self, acno, amount, info):
        self.acno = acno
        self.amount = amount
        self.info = info


class Saving(BankAccount):

    minAmount = 10000
    rate = 6

    def calculate_interest(self, months):
        interest = (self.amount * self.rate * months) / (100 * 12)
        print("Interest:", interest)


class Current(BankAccount):

    minAmount = 5000

    def calculate_interest(self, months):
        print("No Interest for Current Account")


# Main Program

fn = input("Enter First Name: ")
ln = input("Enter Last Name: ")
gender = input("Enter Gender: ")
address = input("Enter Address: ")

info = BankInfo(fn, ln, gender, address)

choice = input("Enter Account Type (Saving/Current): ")

for attempt in range(3):

    acno = input("Enter Account Number: ")
    amount = float(input("Enter Amount: "))

    if choice.lower() == "saving":
        if amount >= Saving.minAmount:
            account = Saving(acno, amount, info)
            break
        else:
            print("Minimum balance should be 10000")

    elif choice.lower() == "current":
        if amount >= Current.minAmount:
            account = Current(acno, amount, info)
            break
        else:
            print("Minimum balance should be 5000")

else:
    print("Maximum attempts exceeded")
    exit()

months = int(input("Enter Number of Months: "))

print("\nCustomer Details")
print("Name:", info.fn, info.ln)
print("Gender:", info.gender)
print("Address:", info.address)
print("Account Number:", account.acno)
print("Amount:", account.amount)

account.calculate_interest(months)