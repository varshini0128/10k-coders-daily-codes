s=[1,2,3,4]   #[1,3,6]
s1=[]
for x in s:
    x+=s1[-1] if s1 else 0
    s1.append(x)
print(s1)

         



n=int(input('enter n value: '))
count=0
num=2
while count<n:
    is_prime=True
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break
    if is_prime:
        print(num)
        count+=1
    num+=1

# for i in range(2,2):
#     print('ith')

m = 'ab2'
print(m[:-1] * int(m[-1]))





### **1. Find LCM (a = 10, b = 20)

a = 10
b = 20

lcm = max(a, b)
while True:
    if lcm % a == 0 and lcm % b == 0:
        print(lcm)
        break
    lcm += 1

### **2. Find HCF (GCD) of 10 and 20**

a = 10
b = 20

while b != 0:
    a, b = b, a % b

print(a)


### **3. Cumulative Sum**




r = [1,2,3,4,5]
result = []
total = 0

for i in r:
    total += i
    result.append(total)

print(result)

### **4. k = [1,2,5] → [7,6,3] (if x != y)**

k = [1,2,5]
total = sum(k)

result = []
for i in k:
    result.append(total - i)

print(result)


### **5. k = 'a3' → aaa

k = 'a3'
print(k[0] * int(k[1]))


### **6. m = 'ab2' → abab**


m = 'ab2'
print(m[:-1] * int(m[-1]))

### **7. k = 'a[3]' → aaa
k = 'a[3]'
char = k[0]
num = int(k[2])

print(char * num)


### 8. n = 'ac[2]' → acac

n = 'ac[2]'
string = n[:2]
num = int(n[3])

print(string * num)



#9. Concatenation without `+`


a = "Hello"
b = "World"

print("{}{}".format(a, b))



print(a.join(["", b]))
print(a, b, sep="")


### **10. Print n Prime Numbers**

n = int(input("Enter n: "))
count = 0
num = 2

while count < n:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)
        count += 1

    num += 1
