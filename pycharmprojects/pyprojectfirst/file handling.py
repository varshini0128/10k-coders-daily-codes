file = open("demo.txt", 'r')
content = file.read()
print(content)
context = file.read(10)
print(context)
contet = file.readline()
print(contet)
file.close()

file = open("demo.txt", 'w')
file.write('this is varsh')
file.close()

file = open("demo.txt", 'r')
content = file.read()
print(content)

file = open("demo.txt", 'a')
file.write('this is 3rd line')
file.close()


