a=float(input("enter value of a:"))
b=float(input("enter value of b:"))
a,b = b,a
print(f"value of a:{a}")
print(f"value of b:{b}")

#slicing
s = "Python"
print(s[1:-1])
# swap with using third variable
x = 10
y = 20      
temp = x
x = y
y = temp
print(f"x: {x}, y: {y}")