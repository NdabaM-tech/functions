def  calculate_discount():
    price = int(input("what is the original price (R): "))
    discount_percent = float(input("what is the discount (%): "))

    if (discount_percent >= 20):
        new_amount = price - (price * (discount_percent/100)) 
        print(f"Your new price is R{new_amount}")
    else:
        print(f"your price is still R{price}")
calculate_discount()
    
