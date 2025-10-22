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



#write a variable length keyword arguements function to calculate total and percentage of a student in different subjects

def marks(**marks):
    total=0
    percentage=100
    for i in marks:
        total+=int(marks[i])
        percentage= (total / (len(marks)*100))*100
    print('total: ',total)
    print('percentage: ',percentage)
marks(maths='95',phys='84',eng='63',nlp='75',chem='94')






def sentence_form(*words):
    sentence = ""  
    for word in words:
        sentence += word + " "  
    return sentence

sentence = sentence_form("My", "name", "is", "varshini", ",", "I", "am", "from", "hyd")
print("Formed Sentence:", sentence)

