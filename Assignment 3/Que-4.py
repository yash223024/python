def calculate_rebate():
    customer_id = input("Enter Customer ID: ")
    purchase_amount = float(input("Enter Purchase Amount: "))

    if purchase_amount >= 10000:
        rebate = 0.12 * purchase_amount
    elif purchase_amount > 5000:
        rebate = 0.09 * purchase_amount
    else:
        rebate = 0.03 * purchase_amount

    print(f"Customer ID: {customer_id}")
    print(f"Purchase Amount: Rs. {purchase_amount:.2f}")
    print(f"Rebate: Rs. {rebate:.2f}")


if __name__ == "__main__":
    calculate_rebate()