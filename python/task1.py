# Task 1: Sum of Mixed Types
# Create one integer variable and one float variable.
# Add them and print the result and its type.

int1 = 5
float1 = 9.03
print(int1+float1)
print(type(int1))
print(type(float1))
print(type(int1+float1))



# Task 2: String to Number Conversion
# Create a string variable representing a number.
# Convert it to integer and float.
# Print the results and their types.

str_var1 = '142'
print(str_var1)
cint = int(str_var1)
cfloat = float(str_var1)
print(cint, cfloat)
print(type(str_var1), type(cfloat), type(cint))



# Task 3: Swap Two Numbers Using Arithmetic
# Create two integer variables.
# Swap their values using arithmetic operations (no third variable).
# Print swapped values.

inta = 33
intb = 90

inta = inta + intb #123
intb = inta - intb #123-90 = 33
inta = inta - intb #123-33 = 90

print("swapped values:", "inta =",inta, ", intb =",intb)


# Task 4: Average of Three Numbers
# Create three numeric variables (int or float).
# Calculate their average and print value and type.

var1 = 12
var2 = 32.53
var3 = 51
avg_result = (var1+var2+var3)/3
print(avg_result)
print(type(avg_result))

# Task 5: Floor Division and Modulus
# Create two integer variables.
# Calculate quotient (//) and remainder (%) and print values with types.


intc = 60
intd = 30
print(intc // intd)        #prints quotient 
print(intc % intd)         #prints remainder   
print(type(intc // intd))
print(type(intc % intd)) 

print(intc // intd, intc % intd, type(intc // intd), type(intc % intd) )    # we can also print all the result in one line 


mydata_list= ['varshini','Sri Indu Institute',7.0]
print(mydata_list)
mydata_list.append("Dilsukhnagar")
print(mydata_list)