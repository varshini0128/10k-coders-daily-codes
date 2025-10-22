# Function to calculate total bill
def total_bill(no_of_items, quantity, price, tax=5, discount=0, delivery_charge=0):
    subtotal = 0
  
    for i in range(no_of_items):
        subtotal += quantity[i] * price[i]
    
    tax_amount = (tax / 100) * subtotal
    subtotal += tax_amount
    
    discount_amount = (discount / 100) * subtotal
    subtotal -= discount_amount
    
    total = subtotal + delivery_charge
    
    return total


final_bill = total_bill(
    3,                  # no_of_items
    [2, 1, 3],          # quantities
    [150, 200, 50],     # prices
    tax=5, 
    discount=10, 
    delivery_charge=50
)
print("Total Bill: ", final_bill)
