def calculate_bill():
    science_books = int(input("Enter the number of Science books: "))
    commerce_books = int(input("Enter the number of Commerce books: "))
    arts_books = int(input("Enter the number of Arts books: "))

    science_price = science_books * 100  # Assuming each Science book costs Rs.100
    commerce_price = commerce_books * 150  # Assuming each Commerce book costs Rs.150
    arts_price = arts_books * 200  # Assuming each Arts book costs Rs.200

    total_price = science_price + commerce_price + arts_price

    discount_science = 0.02 * science_price
    discount_commerce = 0.03 * commerce_price
    discount_arts = 0.04 * arts_price

    total_discount = discount_science + discount_commerce + discount_arts
    net_amount = total_price - total_discount

    if net_amount > 200:
        additional_discount = 0.025 * net_amount
        net_amount -= additional_discount
    else:
        additional_discount = 0

    print(f"Total Price: Rs. {total_price:.2f}")
    print(f"Total Discount: Rs. {total_discount:.2f}")
    print(f"Additional Discount: Rs. {additional_discount:.2f}")
    print(f"Final Bill Amount: Rs. {net_amount:.2f}")


if __name__ == "__main__":
    calculate_bill()