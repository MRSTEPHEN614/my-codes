# expenses = []

# while True:
    # item = input("What item did you buy? ")
    # amount = float(input("How much was it? "))
    # category = input("What category was it? ")

    # expense = {
    #     "item":item,
    #     "amount":amount,
    #     "category":category
    # }

    # expenses.append(expense)
    
    # print("\n Expenses recorded!!")
    # print("item",expense["item"])
    # print("amount",expense["amount"])
    # print("category",expense["category"])

    # again =input("\n Add another expense? (yes/no): ")

    # if again.lower()=="no":
    #     break
    # print("\n All expenses")
    # print(expenses)

    # total = 0

    # for expense in expenses :
    #     total= total + expense["amount"]
    #     print("\n Total expenses", total)

    # category_totals = {}
    # for expense in expenses :
    #     category = expense ["category"]
    #     amount = expense ["amount"]

    # if category in category_totals:
    #     category_totals[category]+=amount
    # else:
    #     category_totals[category] =amount
    #     print ("\n Spending by category:")

    # for category, amount in category_totals.items():
    #      print(category,".", amount)


expenses = []
while True:
    print("\n======================")
    print("EXPENSE TRACKER")
    print("===================")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. View Total")
    print("4. View Spending by Category")
    print("5. Exit")

    choice = input("\n Choose an option: ")
    if choice == "1":
        print("\n <<<<<<<Add Expense>>>>>>")

        item = input("What did you spend money on? ")

        amount= float(input("How much did you spend? "))
        
        category = input("What category is it? ")

        expense = {
            "item":item,
            "amount":amount,
            "category":category
        }

        expenses.append(expense)
        print("\n Expense recorded successfully!!")


    elif choice == "2":
        print("\n !!!!Viewing expenses!!!!")

        if len(expense)==0:
            print("No expenses recorded yet!")

        else:
            for expense in expenses:
                print("<<........>>")
                print("item: ",expense["item"])
                print("amount: ",expense["amount"])
                print("category: ", expense["category"])



    elif choice == "3":
        print("\n Calculating total")

        total = 0
        for expense in expenses:
            total = total + expense ["amount"]
            print("<< Total expenses fall below >>\n")
            print("\nYour total expenses", total)

    elif choice == "4":
        print("\n  Viewing category totals")

        category_totals = {}
        for expense in expenses:
            category = expense ["category"]
            amount = expense ["amount"]

            if category in category_totals:
                category_totals[category]+= amount
            else:
                category_totals[category] = amount 
                print("\n ----Spending recorded yet----")
                if len(category_totals) == 0:
                    print("No expenses recorded yet.")
                    
                else:
                    for category, amount in category_totals.items():
                        print(category, ".", amount)

    elif choice == "5":
        print("\n Goodbye!!")
        break

    else:
        print("\n invalid option.Choose 1-5")
