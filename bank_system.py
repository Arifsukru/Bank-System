import random
import os


class Customer:
    def __init__(self, name, age, account_no, balance, account_number):
        self.name = name
        self.age = age
        self.account_no = account_no
        self.balance = balance
        self.account_number = account_number
    def print(self):
        print(" Name: ", self.name, "Age: ", self.age, "Account number: ", self.account_no, "Balance:", self.balance)


def getCustomerDataFromTxt():
    file = open("bank.txt", "r+")
    data_list = file.readlines()
    file.close()
    return data_list


def cleaningCustomerData(data_list):
    data_first = " ".join(data_list)
    clean_list = data_first.split(" ")
    for x in clean_list:
        if x == "------------------------------\n":
            clean_list.remove(x)
    return clean_list


def getCustomerInfo(clean_list):
    customer_list = []
    k = 0
    number_of_customer = 7
    for x in range(number_of_customer):
        a = clean_list[(0 + k)]
        b = clean_list[(1 + k)]
        c = clean_list[(2 + k)]
        d = clean_list[(3 + k)]
        e = clean_list[(4 + k)]
        k += 5
        customer_list.append(Customer(a, b, c, d, e))
    return customer_list


data_list = getCustomerDataFromTxt()
clean_list = cleaningCustomerData(data_list)
customer_list = getCustomerInfo(clean_list)

print("Welcome\n")

while True:
    print("1. Open new account\n2. Login to account\n3. Exit")
    opening_choice = input("\nWhat would you like to do? ")
    if opening_choice == "3":
        print("Have a nice day.\nHope you come again.")
        break
    elif opening_choice == "1":
        name = input("Enter name: ")
        data_list.append("{}".format(name))
        age = input("Enter age: ")
        data_list.append("\n{}".format(age))
        account_no = str(random.randint(10000000000, 99999999999))
        data_list.append("\n{}".format(account_no))
        data_list.append("\n0") # balance = 0
        number_of_customer = int(data_list[-6])
        data_list.append("\n{}".format(str(number_of_customer + 1)))
        data_list.append("\n------------------------------\n")
        print("Operation completed.\nAccount created successfully.\n")
        continue_operation = input("\nWould you like to do another operation? ")
        positive = ["Yes", "yes", "YES", "I do", "ı do"]
        negative = ["No", "no", "NO", "I don't", "I do not", "ı dont", "ı do not"]
        if continue_operation in positive:
            pass
        elif continue_operation in negative:
            print("Have a nice day.\nHope you come again.")
            break
    elif opening_choice == "2":
        account_number = int(input("\nEnter account number? "))
        welcoming = data_list[0 + (6 * (account_number - 1))]
        welcoming_name = welcoming.split(" ")
        print("\n{} logged in.".format(welcoming_name[-1]))
        while True:
            print("\n1. My balance\n2. Deposit\n3. Withdraw\n4. Transfer\n5. Log out")
            account_choice = input("\nWhat would you like to do? ")
            if account_choice == "1":
                print("\nBalance in your account: {}".format(data_list[3 + (6 * (account_number - 1))]))
                print("1. Do another operation\n2. Go back")
                continue_operation = input("\nWhat would you like to do ? ")
                if continue_operation == "1":
                    pass
                elif continue_operation == "2":
                    print("\nYou logged out of your account.\n")
                    break
            if account_choice == "2":
                deposit_amount = int(input("Enter amount of money: "))
                balance_line = data_list[3 + (6 * (account_number - 1))]
                actual_balance = [int(balance_line) + deposit_amount]
                data_list[3 + (6 * (account_number - 1))] = "{}\n".format(actual_balance[0])
                print("\nTransaction completed.\nActual balance: {}".format(actual_balance[0]))
                print("1. Do another operation\n2. Go back")
                continue_operation = input("\nWhat would you like to do ? ")
                if continue_operation == "1":
                    pass
                elif continue_operation == "2":
                    print("\nYou logged out of your account.\n")
                    break
            if account_choice == "3":
                withdraw_amount = int(input("Enter amount of money: "))
                balance_line = data_list[3 + (6 * (account_number - 1))]
                actual_balance = [int(balance_line) - withdraw_amount]
                data_list[3 + (6 * (account_number - 1))] = "{}\n".format(actual_balance[0])
                print("Transaction completed.\nActual balance: {}".format(actual_balance[0]))
                print("1. Do another operation\n2. Go back")
                continue_operation = input("\nWhat would you like to do ? ")
                if continue_operation == "1":
                    pass
                elif continue_operation == "2":
                    print("\nYou logged out of your account.\n")
                    break
            if account_choice == "4":
                account_number_2 = int(input("Enter account number of related customer: "))
                related_customer_name = data_list[0 + (6 * (account_number_2 - 1))]
                print("\nYou will transfer your money to: {}".format(related_customer_name))
                transfer_amount = int(input("Enter amount of money: "))
                balance_line_transfer = data_list[3 + (6 * (account_number - 1))]
                balance_line_transfer_to = data_list[3 + (6 * (account_number_2 - 1))]
                actual_balance_line_transfer = [int(balance_line_transfer) - transfer_amount]
                actual_balance_line_transfer_to = [int(balance_line_transfer_to) + transfer_amount]
                data_list[3 + (6 * (account_number - 1))] = "{}\n".format(actual_balance_line_transfer[0])
                data_list[3 + (6 * (account_number_2 - 1))] = "{}\n".format(actual_balance_line_transfer_to[0])
                print("\nTransaction completed.\nActual balance: {}".format(actual_balance_line_transfer[0]))
                print("1. Do another operation\n2. Go back")
                continue_operation = input("\nWhat would you like to do ? ")
                if continue_operation == "1":
                    pass
                elif continue_operation == "2":
                    print("\nYou logged out of your account.\n")
                    break
            if account_choice == "5":
                print("\nYou logged out of your account.\n")
                break


os.remove("bank.txt")
file = open("bank.txt", "a")

for write_again in data_list:
    file.write(write_again)

file.close()
