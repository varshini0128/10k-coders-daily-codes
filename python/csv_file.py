
# # csv module = provides functions to read and write csv files.
# # pip install csv
 

# with open('class73_75.csv','a') as h:
#     write = csv.writer(h)

#     n = int(input('No/of students:'))

#     for x in range(n): I
#     std_id = int(input('Enter student id:'))
#     std_name = input('Enter student name:')
#     std_age = int(input('Enter student age:'))
#     write.writerow([std_id,std_name,std_age])



# import csv
# with open('class73_75.csv','r')as k:
#     read = csv.reader(k)
#     print(next(read))
#     print(next(read))
#     print(next(read))

#             # or
import csv
with open('class73_75.csv','r')as k:
    read = csv.DictReader(k)
    # print(next(read))
            # or
    for x in read:
        print(x['std_id'],x['std_name'],x['std_age'])

  
# with open('students.csv','r') as h:
#     read = csv. DictReader(h)

#     n = input('Enter std pin:')
#     for x in read:
#      if x['std_id' ] == n:
#          print(x)

    
