input_value = 6
result = input_value * input_value
print("The area of square is:", result)


length = 5
breadth = 10
area = length * breadth
print("The area of rectangle is:", area)

base = 4
height = 8
area = 0.5 * base * height
print("The area of triangle is:", area)


side = 7
perimeter_square = 4 * side
print("The perimeter of square is:", perimeter_square)

len = 6
brd = 12
perimeter_of_rec = 2 * (len + brd)
print("The perimeter of rectangle is:", perimeter_of_rec)

side1 = 3
side2 = 4
side3 = 5
perimeter_triangle = side1 + side2 + side3
print("The perimeter of triangle is:", perimeter_triangle)


#break the amount into 1000s, 500s, 100s, 50s, 20s, 10s, 5s, 2s and 1s
amount = 5763
thousands = amount // 1000
amount %= 1000
five_hundreds = amount // 500
amount %= 500
hundreds = amount // 100
amount %= 100
fifties = amount // 50
amount %= 50
twenties = amount // 20
amount %= 20
tens = amount // 10
amount %= 10
fives = amount // 5
amount %= 5
twos = amount // 2
amount %= 2
ones = amount // 1
amount %= 1
print("1000s:", thousands, "500s:", five_hundreds, "100s:", hundreds, "50s:", fifties, "20s:", twenties, "10s:", tens, "5s:", fives, "2s:", twos, "1s:", ones)


#convert seconds to hours, minutes and seconds
total_seconds = 36560
hours = total_seconds // 3600
total_seconds %= 3600       
minutes = total_seconds // 60
seconds = total_seconds % 60
print("Hours:", hours, "Minutes:", minutes, "Seconds:", seconds)


#sum of marks
maths = 85
physics = 90
chemistry = 78
total_marks = maths + physics + chemistry
print("Total marks:", total_marks)


#average of marks
average_marks = total_marks / 3
print("Average marks:", average_marks)
